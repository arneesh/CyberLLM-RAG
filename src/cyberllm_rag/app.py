"""Gradio chat interface for the CyberLLM RAG assistant."""

from __future__ import annotations

import gradio as gr

from cyberllm_rag.config import settings
from cyberllm_rag.retriever import answer_question


def build_app() -> gr.ChatInterface:
    """Construct and return the Gradio ``ChatInterface``."""
    return gr.ChatInterface(
        fn=answer_question,
        title="CyberLLM Assistant",
        description="Ask me anything about CyberLLM — products, employees, contracts, and more.",
        examples=[
            "What products does CyberLLM offer?",
            "Who is Marcus Chen?",
            "Tell me about the ThreatLLM pricing tiers.",
            "What is the company culture like?",
        ],
        # theme=gr.themes.Soft(),
    )


def launch() -> None:
    """Build and launch the Gradio app."""
    app = build_app()
    app.launch(
        server_name=settings.gradio_server_name,
        server_port=settings.gradio_server_port,
        share=settings.gradio_share,
    )
