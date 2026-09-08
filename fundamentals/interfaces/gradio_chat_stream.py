import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

from utils.retry import call_llm_with_retry


load_dotenv(override=True)


api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found in the environment"
    )


MODEL = "gemini-3-flash-preview"

GEMINI_BASE_URL = (
    "https://generativelanguage.googleapis.com/v1beta/openai"
)


client = OpenAI(
    base_url=GEMINI_BASE_URL,
    api_key=api_key
)


SYSTEM_MESSAGE = "You are a helpful assistant."


def message_llm_stream(prompt):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_MESSAGE
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    stream = call_llm_with_retry(
        lambda: client.chat.completions.create(
            model=MODEL,
            messages=messages,
            stream = True)
          )

    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result

  
message_input = gr.Textbox(
    label="Your Message",
    info="Enter a message for Gemini",
    lines=7
)


message_output = gr.Markdown(
    label="Response"
)


view = gr.Interface(

    fn=message_llm_stream,

    title="AI Assistant",

    inputs=message_input,

    outputs=message_output,

    examples=[
        "Explain the Transformer architecture to a layperson",
        "Explain the Transformer architecture to an aspiring AI engineer",
    ],

    flagging_mode="never"
)


view.launch()