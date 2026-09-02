# Chat Completions API Fundamentals

This module explores different ways of interacting with Large Language Models using Python.

## Topics Covered

### 1. Direct HTTP Requests

Using the `requests` library to communicate directly with the OpenAI API.

Concepts explored:

- HTTP POST requests
- API endpoints
- Authorization headers
- JSON payloads
- API responses

### 2. OpenAI Python Client

Using the OpenAI Python SDK to interact with LLMs.

Concepts explored:

- Python SDKs
- Environment variables
- API key management
- SDK abstraction

### 3. Ollama and OpenAI-Compatible APIs

Using the OpenAI Python client to communicate with a locally running Ollama model.

Concepts explored:

- Custom `base_url`
- OpenAI-compatible APIs
- Local LLM execution
- Ollama

### 4. Website Summarization

Building a simple AI-powered website summarizer.

The application:

1. Accepts a website URL.
2. Fetches the website using `requests`.
3. Parses HTML using BeautifulSoup.
4. Removes unnecessary content.
5. Extracts website text.
6. Sends the content to a local LLM using Ollama.
7. Returns a concise summary.

## Files

- `http_requests.py` — Direct OpenAI API call using HTTP requests.
- `openai_client.py` — OpenAI API call using the Python SDK.
- `ollama_request.py` — Local LLM call using Ollama's OpenAI-compatible API.
- `scraper.py` — Website content extraction using BeautifulSoup.
- `ollama_summarizer.py` — AI-powered website summarization application.

## Technologies Used

- Python
- OpenAI Python SDK
- Ollama
- Llama 3.2
- Requests
- BeautifulSoup