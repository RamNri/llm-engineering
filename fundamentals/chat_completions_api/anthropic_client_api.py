import os

from dotenv import load_dotenv
from anthropic import Anthropic


load_dotenv(override=True)

MODEL = "claude-sonnet-4-5-20250929"

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError(
        "ANTHROPIC_API_KEY was not found in the environment."
    )


client = Anthropic(
    api_key=api_key
)


response = client.messages.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Describe the color Blue to someone who's never been able to see in 1 sentence"}],
    max_tokens=100
)

print(response.content[0].text)