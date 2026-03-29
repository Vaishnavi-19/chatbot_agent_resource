# Bhagavad Gita Q&A (local Ollama)

A small [Gradio](https://www.gradio.app/) chat UI that answers questions about the Bhagavad Gita using the English text embedded in the app’s system prompt. The model runs **locally via [Ollama](https://ollama.com/)**—no OpenAI API or API key required.

## Prerequisites

- Python 3.14+ (see `pyproject.toml`)
- [Ollama](https://ollama.com/download) installed and running (default: `http://127.0.0.1:11434`)
- A chat model pulled in Ollama, for example:

  ```bash
  ollama pull llama3.2
  ```

## Setup

Install dependencies (from the project root):

```bash
pip install -e .
```

Or with [uv](https://github.com/astral-sh/uv):

```bash
uv sync
```

## Configuration (optional)

Create a `.env` file or set environment variables:

| Variable       | Default                 | Description                                      |
|----------------|-------------------------|--------------------------------------------------|
| `OLLAMA_MODEL` | `llama3.2`              | Name of the Ollama model to use (must be pulled). |
| `OLLAMA_HOST`  | `http://127.0.0.1:11434` | Ollama server URL if not local default.          |

## Run

```bash
python main.py
```

Gradio will print a local URL (typically `http://127.0.0.1:7860`). Open it in your browser and ask questions; the app keeps conversation history for follow-ups.

## Data

The full English source is loaded from `bhagavad-gita-in-english-source-file.pdf` at startup and injected into the system prompt so replies stay grounded in that text.
