# Chat Completions API Fundamentals

This module explores different ways of interacting with Large Language Models (LLMs) using Python.

The goal of this section is to understand how LLM applications communicate with different providers through:

- Direct HTTP requests
- Provider SDKs
- OpenAI-compatible APIs
- Local LLMs
- Unified LLM gateways

---

# Topics Covered

## 1. Direct HTTP Requests

Using the `requests` library to communicate directly with an LLM API through HTTP.

### Concepts Explored

- HTTP POST requests
- API endpoints
- Authorization headers
- JSON payloads
- API responses
- API authentication

---

## 2. OpenAI Python Client

Using the OpenAI Python SDK to interact with OpenAI models.

### Concepts Explored

- Python SDKs
- Creating an API client
- Environment variables
- API key management
- Chat Completions API
- SDK abstraction

This demonstrates how a Python SDK simplifies API communication compared with manually creating HTTP requests.

---

## 3. Google Gemini Client

Using Google's native Python SDK to interact with Gemini models.

### Concepts Explored

- Provider-specific SDKs
- Creating a Gemini client
- API key authentication
- Sending prompts to Gemini models
- Accessing generated responses

This demonstrates that different LLM providers can expose their own SDKs and API interfaces.

---

## 4. Anthropic Claude Client

Using Anthropic's Python SDK to interact with Claude models.

### Concepts Explored

- Anthropic Python SDK
- API key management
- Creating an Anthropic client
- Sending messages to Claude
- Understanding structured response content

This example highlights how different providers can have different request and response structures.

---

## 5. Ollama and OpenAI-Compatible APIs

Using the OpenAI Python client to communicate with a locally running Ollama model.

### Concepts Explored

- Custom `base_url`
- OpenAI-compatible APIs
- Local LLM execution
- Ollama
- Running open-source models locally

This demonstrates an important concept:

> The OpenAI Python client can be used as an API client for services that implement an OpenAI-compatible API.

---

## 6. OpenRouter

Using OpenRouter to access multiple LLM providers through a unified API.

### Concepts Explored

- Unified LLM gateways
- OpenAI-compatible APIs
- Custom API endpoints
- Model selection
- Accessing multiple model providers through a single interface

Conceptually:

```text
Your Application
       │
       ▼
   OpenRouter
       │
 ┌─────┼─────┐
 ▼     ▼     ▼
GPT  Gemini Claude
```

This introduces the concept of using a gateway layer to access models from different providers through a unified API.

---

# Files

- `http_requests.py` — Direct API call using HTTP requests.
- `openai_client.py` — Calling an OpenAI model using the OpenAI Python SDK.
- `gemini_client_api.py` — Calling a Gemini model using Google's native Python SDK.
- `anthropic_client_api.py` — Calling a Claude model using Anthropic's Python SDK.
- `ollama_request.py` — Calling a locally running Ollama model using an OpenAI-compatible API.
- `openrouter_client.py` — Accessing LLM models through OpenRouter.

---

# Key Learning: Different Ways to Access LLMs

One of the main lessons from this module is that the same general goal:

> Send a prompt to an LLM and receive a response.

can be achieved through different approaches.

## Direct HTTP API

```text
Python Application
       │
       ▼
HTTP Request
       │
       ▼
LLM API
```

---

## Provider SDK

```text
Python Application
       │
       ▼
Provider SDK
       │
       ▼
LLM Provider API
```

---

## OpenAI-Compatible API

```text
Python Application
       │
       ▼
OpenAI Python Client
       │
       ▼
Compatible API
       │
       ▼
LLM
```

---

## Unified Gateway

```text
Python Application
       │
       ▼
Unified Gateway
       │
 ┌─────┼─────┐
 ▼     ▼     ▼
GPT  Gemini Claude
```

---

# Technologies Used

- Python
- OpenAI Python SDK
- Google GenAI SDK
- Anthropic Python SDK
- OpenRouter
- Ollama
- Requests
- Python Dotenv

---

# Project Structure

```text
fundamentals/
└── chat_completions_api/
    ├── README.md
    ├── anthropic_client_api.py
    ├── gemini_client_api.py
    ├── http_requests.py
    ├── ollama_request.py
    ├── openai_client.py
    └── openrouter_client.py
```

---

# Key Takeaway

Different LLM providers expose different APIs and SDKs, but the underlying workflow is generally similar:

```text
Load Configuration
       ↓
Load API Key
       ↓
Create Client
       ↓
Select Model
       ↓
Send Prompt
       ↓
Receive Response
```

Understanding these different approaches provides the foundation for building applications that can work with multiple LLM providers and APIs.