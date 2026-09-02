# Chat Completions API

This module explores different ways of interacting with Large Language Models using Python.

## What I learned

### 1. Direct HTTP Requests

Using the `requests` library to communicate directly with the OpenAI Chat Completions API.

Key concepts:

- HTTP POST requests
- API endpoints
- Authorization headers
- JSON payloads
- Parsing API responses

### 2. OpenAI Python Client

Using the official OpenAI Python SDK to interact with OpenAI models.

Key concepts:

- Python client libraries
- Environment variables
- `OPENAI_API_KEY`
- SDK abstraction over HTTP requests

### 3. Ollama with the OpenAI Client

Using the OpenAI Python client to communicate with a locally running Ollama model through its OpenAI-compatible API.

Key concepts:

- `base_url`
- OpenAI-compatible APIs
- Local LLM execution
- Ollama
- Llama 3.2

## Files

- `http_requests.py` — Calling the OpenAI API using the `requests` library.
- `openai_client.py` — Calling OpenAI using the official Python client.
- `ollama_request.py` — Calling a local Ollama model using the OpenAI Python client.