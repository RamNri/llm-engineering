# Reasoning Effort Experiment

This experiment explores how different reasoning-effort settings can affect the behavior of a reasoning-capable Large Language Model (LLM).

The same probability puzzle is sent to the model using different reasoning-effort levels to observe how inference-time computation can influence the model's response.

---

## Concepts Explored

- Reasoning models
- Inference-time scaling
- Training-time scaling
- Reasoning effort
- OpenAI-compatible APIs
- Model capability vs inference computation

---

## Architecture

```text
Python Application
        │
        ▼
OpenAI Python Client
        │
        ▼
Gemini OpenAI-Compatible API
        │
        ▼
Gemini Model
        │
        ▼
Different Reasoning Effort Levels
        │
        ├── minimal
        │
        └── low