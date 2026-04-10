"""RAG retrieval and answer generation."""

from __future__ import annotations

import logging

from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI

from cyberllm_rag.config import settings

logger = logging.getLogger(__name__)

SYSTEM_PROMPT_TEMPLATE = """\
You are a knowledgeable, friendly assistant representing the company CyberLLM.
You are chatting with a user about CyberLLM.
If relevant, use the given context to answer any question.
If you don't know the answer, say so.

Context:
{context}
"""


def _get_vectorstore() -> Chroma:
    embeddings = HuggingFaceEmbeddings(model_name=settings.embedding_model)
    return Chroma(
        persist_directory=settings.vector_db_path,
        embedding_function=embeddings,
    )


def _get_llm() -> ChatOpenAI:
    return ChatOpenAI(
        api_key=settings.openai_api_key,
        temperature=settings.llm_temperature,
        model_name=settings.llm_model,
    )


_vectorstore: Chroma | None = None
_llm: ChatOpenAI | None = None


def get_vectorstore() -> Chroma:
    global _vectorstore
    if _vectorstore is None:
        _vectorstore = _get_vectorstore()
    return _vectorstore


def get_llm() -> ChatOpenAI:
    global _llm
    if _llm is None:
        _llm = _get_llm()
    return _llm


def answer_question(question: str, history: list | None = None) -> str:
    """Retrieve relevant context and generate an answer.

    Parameters
    ----------
    question:
        The user question.
    history:
        Gradio-style chat history (list of [user, assistant] pairs). Currently
        unused for retrieval but forwarded for display.

    Returns
    -------
    str
        The assistant's response.
    """
    retriever = get_vectorstore().as_retriever(search_kwargs={"k": settings.retriever_k})
    docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in docs)
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(context=context)

    logger.debug("Retrieved %d docs for question: %s", len(docs), question[:80])

    response = get_llm().invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=question),
    ])
    return response.content
