"""CLI entry-points for ingestion and serving."""

from __future__ import annotations

import argparse
import logging
import sys


def _setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        format="%(asctime)s  %(levelname)-8s  %(name)s — %(message)s",
        datefmt="%H:%M:%S",
        level=level,
        stream=sys.stderr,
    )


def ingest() -> None:
    """CLI: ingest knowledge-base documents into the vector store."""
    parser = argparse.ArgumentParser(description="Ingest knowledge-base into vector store")
    parser.add_argument("--force", action="store_true", help="Delete existing vector store and rebuild")
    parser.add_argument("--knowledge-base", type=str, default=None, help="Path to knowledge-base directory")
    parser.add_argument("--db", type=str, default=None, help="Path to vector store directory")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    _setup_logging(args.verbose)

    from cyberllm_rag.ingest import run_ingestion

    run_ingestion(
        knowledge_base_path=args.knowledge_base,
        vector_db_path=args.db,
        force=args.force,
    )


def serve() -> None:
    """CLI: launch the Gradio chat UI."""
    parser = argparse.ArgumentParser(description="Launch the CyberLLM RAG chat UI")
    parser.add_argument("--port", type=int, default=None, help="Server port (default: 7860)")
    parser.add_argument("--share", action="store_true", help="Create a public Gradio share link")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    _setup_logging(args.verbose)

    from cyberllm_rag.config import settings

    if args.port:
        settings.gradio_server_port = args.port
    if args.share:
        settings.gradio_share = True

    from cyberllm_rag.app import launch

    launch()
