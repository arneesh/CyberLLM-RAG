"""Ingest the knowledge-base documents into a Chroma vector store.

Reads every Markdown file under ``knowledge-base/``, splits them into
overlapping chunks, embeds with HuggingFace all-MiniLM-L6-v2, and persists
the resulting vector store to disk.
"""

from __future__ import annotations

import logging
import os
import shutil
from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from cyberllm_rag.config import settings

logger = logging.getLogger(__name__)


def _load_documents(knowledge_base_path: str | Path) -> list:
    """Walk each sub-folder of the knowledge base and load all ``.md`` files."""
    kb = Path(knowledge_base_path)
    documents: list = []
    for folder in sorted(kb.iterdir()):
        if not folder.is_dir():
            continue
        doc_type = folder.name
        loader = DirectoryLoader(
            str(folder),
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"},
        )
        folder_docs = loader.load()
        for doc in folder_docs:
            doc.metadata["doc_type"] = doc_type
            documents.append(doc)
    logger.info("Loaded %d documents from %s", len(documents), kb)
    return documents


def _split_documents(documents: list) -> list:
    """Split documents into overlapping chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
    )
    chunks = splitter.split_documents(documents)
    logger.info("Split into %d chunks (size=%d, overlap=%d)",
                len(chunks), settings.chunk_size, settings.chunk_overlap)
    return chunks


def run_ingestion(
    *,
    knowledge_base_path: str | Path | None = None,
    vector_db_path: str | Path | None = None,
    force: bool = False,
) -> None:
    """End-to-end ingestion pipeline.

    Parameters
    ----------
    knowledge_base_path:
        Override the knowledge base directory (defaults to config).
    vector_db_path:
        Override the vector DB persist directory (defaults to config).
    force:
        If *True*, delete any existing vector store before ingesting.
    """
    kb_path = Path(knowledge_base_path or settings.knowledge_base_path)
    db_path = Path(vector_db_path or settings.vector_db_path)

    if force and db_path.exists():
        logger.warning("Removing existing vector store at %s", db_path)
        shutil.rmtree(db_path)

    if db_path.exists() and any(db_path.iterdir()):
        logger.info("Vector store already exists at %s — skipping ingestion (use --force to rebuild)", db_path)
        return

    documents = _load_documents(kb_path)
    chunks = _split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name=settings.embedding_model)

    logger.info("Creating vector store at %s …", db_path)
    os.makedirs(db_path, exist_ok=True)
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(db_path),
    )
    logger.info("Ingestion complete — %d chunks indexed", len(chunks))
