"""Centralised configuration loaded from environment variables and sensible defaults."""

from pathlib import Path

from pydantic_settings import BaseSettings


_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    openai_api_key: str = ""

    llm_model: str = "gpt-4.1-nano"
    llm_temperature: float = 0.0

    embedding_model: str = "all-MiniLM-L6-v2"

    vector_db_path: str = str(_PROJECT_ROOT / "vector_db")

    knowledge_base_path: str = str(_PROJECT_ROOT / "knowledge-base")

    chunk_size: int = 1000
    chunk_overlap: int = 200

    retriever_k: int = 4

    gradio_server_name: str = "0.0.0.0"
    gradio_server_port: int = 7860
    gradio_share: bool = False

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8", "extra": "ignore"}


settings = Settings()
