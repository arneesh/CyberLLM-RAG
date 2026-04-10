# CyberLLM RAG

A Retrieval-Augmented Generation (RAG) pipeline that powers an expert knowledge assistant for **CyberLLM**, an AI-powered cybersecurity platform company. Employees can ask natural-language questions about products, contracts, colleagues, and company information and receive accurate, context-grounded answers.

## Architecture

```
knowledge-base/          Markdown docs (products, contracts, employees, company)
        │
        ▼
┌──────────────┐   HuggingFace all-MiniLM-L6-v2
│   Ingestion  │ ──────────────────────────────► Chroma vector store
└──────────────┘
        │
        ▼
┌──────────────┐   similarity search   ┌────────────┐   GPT-4.1-nano   ┌──────────┐
│   Question   │ ────────────────────► │  Retriever  │ ──────────────► │  Answer  │
└──────────────┘                       └────────────┘                  └──────────┘
        │
        ▼
   Gradio Chat UI
```

**Key components:**

| Component                                | Description                                                                                                                                                          |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ingestion** (`cyberllm_rag.ingest`)    | Loads Markdown files, splits into overlapping chunks (1 000 chars / 200 overlap), embeds with HuggingFace `all-MiniLM-L6-v2`, and persists to a Chroma vector store. |
| **Retriever** (`cyberllm_rag.retriever`) | Performs similarity search against the vector store, builds a context-augmented prompt, and calls OpenAI GPT-4.1-nano.                                               |
| **Chat UI** (`cyberllm_rag.app`)         | A Gradio `ChatInterface` with example questions and a clean theme.                                                                                                   |
| **Config** (`cyberllm_rag.config`)       | Pydantic Settings — every knob is overridable via environment variables or `.env`.                                                                                   |

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- An OpenAI API key

## Quickstart

```bash
# 1. Clone the repo
git clone https://github.com/<your-user>/cyberllm-rag.git
cd cyberllm-rag

# 2. Create .env from the example
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# 3. Install dependencies with uv
uv sync

# 4. Ingest the knowledge base into the vector store
uv run cyberllm-ingest

# 5. Launch the chat UI
uv run cyberllm-serve
```

The Gradio app will be available at **http://localhost:7860**.

## CLI Reference

### `cyberllm-ingest`

Ingest the knowledge-base documents into a Chroma vector store.

```
Usage: cyberllm-ingest [OPTIONS]

Options:
  --force              Delete existing vector store and rebuild
  --knowledge-base     Path to knowledge-base directory (default: ./knowledge-base)
  --db                 Path to vector store directory (default: ./vector_db)
  -v, --verbose        Enable debug logging
```

### `cyberllm-serve`

Launch the Gradio chat UI.

```
Usage: cyberllm-serve [OPTIONS]

Options:
  --port INT           Server port (default: 7860)
  --share              Create a public Gradio share link
  -v, --verbose        Enable debug logging
```

## Configuration

All settings are configurable via environment variables (or a `.env` file):

| Variable              | Default            | Description                                      |
| --------------------- | ------------------ | ------------------------------------------------ |
| `OPENAI_API_KEY`      | —                  | **Required.** Your OpenAI API key.               |
| `LLM_MODEL`           | `gpt-4.1-nano`     | OpenAI model for answer generation.              |
| `LLM_TEMPERATURE`     | `0.0`              | Sampling temperature.                            |
| `EMBEDDING_MODEL`     | `all-MiniLM-L6-v2` | HuggingFace sentence-transformer for embeddings. |
| `VECTOR_DB_PATH`      | `./vector_db`      | Chroma persist directory.                        |
| `KNOWLEDGE_BASE_PATH` | `./knowledge-base` | Source document directory.                       |
| `CHUNK_SIZE`          | `1000`             | Max characters per chunk.                        |
| `CHUNK_OVERLAP`       | `200`              | Character overlap between chunks.                |
| `RETRIEVER_K`         | `4`                | Number of documents to retrieve per query.       |
| `GRADIO_SERVER_PORT`  | `7860`             | Port for the Gradio server.                      |
| `GRADIO_SHARE`        | `false`            | Whether to create a public share link.           |

## Knowledge Base

The `knowledge-base/` directory contains the source documents organised by category:

```
knowledge-base/
├── company/       Company overview, culture, careers, about
├── contracts/     Client contracts across all product lines
├── employees/     Employee profiles and HR records
└── products/      Product descriptions (ThreatLLM, ShieldLLM, NetLLM, …)
```

To add new documents, drop Markdown files into the appropriate folder and re-run `cyberllm-ingest --force`.

## Project Structure

```
cyberllm-rag/
├── pyproject.toml
├── .env.example
├── .gitignore
├── .python-version
├── README.md
├── knowledge-base/        Source documents
├── src/
│   └── cyberllm_rag/
│       ├── __init__.py
│       ├── config.py      Pydantic Settings configuration
│       ├── ingest.py      Document loading, chunking, embedding
│       ├── retriever.py   RAG retrieval + answer generation
│       ├── app.py         Gradio chat interface
│       └── cli.py         CLI entry-points
└── tests/
    └── __init__.py
```
