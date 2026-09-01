import os

import requests
from dotenv import load_dotenv


load_dotenv(override=True)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY was not found in the environment."
    )


headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}


payload = {
    "model": "gpt-5-nano",
    "messages": [
        {
            "role": "user",
            "content": "Tell me a fun fact",
        }
    ],
}


response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    json=payload,
)

response.raise_for_status()

result = response.json()

print(result["choices"][0]["message"]["content"])