# Gradio LLM Interface

This module demonstrates how to build a simple web-based user interface for interacting with a Large Language Model using **Gradio**.

The application connects a Gradio interface to Google's Gemini model using the OpenAI Python client and displays the model's response directly in the browser.

## Overview

The application allows a user to:

1. Enter a prompt through a web interface.
2. Send the prompt to an LLM.
3. Handle API failures using reusable retry logic.
4. Display the LLM response in Markdown format.

## Architecture

```text
User
  │
  ▼
Gradio Web Interface
  │
  ▼
Python Function
  │
  ▼
Retry Utility
  │
  ▼
Gemini API
  │
  ▼
LLM Response
  │
  ▼
Gradio Markdown Output

## Access Gradio interface
  http://127.0.0.1:7860 

  You will see the Gradio interface.

  Using the Application
  Enter a question or prompt in the text box.
  Click the Submit button.
  The prompt is sent to the Gemini model.
  The application processes the request using the retry utility.
  The LLM response is displayed in the Markdown output area.

  Example prompts included in the interface:

  Explain the Transformer architecture to a layperson.
  Explain the Transformer architecture to an aspiring AI engineer.