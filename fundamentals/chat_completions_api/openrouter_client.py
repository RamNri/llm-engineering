import os

from dotenv import load_dotenv
from openrouter import OpenRouter


load_dotenv(override=True)


MODEL = "openrouter/free"


api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError(
        "OPENROUTER_API_KEY was not found in the environment."
    )


with OpenRouter(api_key=api_key) as client:

    response = client.chat.send(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": (
                    "Describe the color blue to someone who has "
                    "never been able to see it, in one sentence."
                ),
            }
        ],
    )

    print(response.choices[0].message.content)