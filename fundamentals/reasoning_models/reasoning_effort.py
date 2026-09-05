import os

from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables from the .env file
load_dotenv(override=True)


# Get the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found in the environment."
    )


# Gemini OpenAI-compatible API endpoint
GEMINI_BASE_URL = (
    "https://generativelanguage.googleapis.com/v1beta/openai/"
)


# Model used for the experiment
MODEL = "gemini-3-flash-preview"

#To experiment pick in this combination
# small model , do not set reasoning_effort
# big model, do not set reasoning effort
# small model with different reasoning_effort, low, minimal, 
# big model with differnt reasoing_effort

"""Model capability and reasoning computation are two different factors.
A more capable model may perform better because of its training and architecture.
A reasoning-capable model may also improve its performance on some tasks by using additional inference-time computation.
However:
More reasoning does not guarantee a correct answer.
The quality of the prompt and the clarity of the problem are also important."""

# Create an OpenAI-compatible client for Gemini
client = OpenAI(
    base_url=GEMINI_BASE_URL,
    api_key=api_key
)


# A probability puzzle used to experiment with reasoning effort
PUZZLE = [
    {
        "role": "user",
        "content": (
            "You toss two coins. At least one of them is heads. "
            "What is the probability that the other coin is tails? "
            "Answer with the probability only."
        ),
    }
]


def ask_with_reasoning(reasoning_effort):
    """Send the same puzzle using a specified reasoning effort."""

    response = client.chat.completions.create(
        model=MODEL,
        messages=PUZZLE,
        reasoning_effort=reasoning_effort,
    )

    answer = response.choices[0].message.content

    print(f"\nReasoning effort: {reasoning_effort}")
    print(f"Answer: {answer}")


def main():
    """Run the reasoning effort experiment."""

    print("Running reasoning effort experiment...")

    ask_with_reasoning("minimal")
    ask_with_reasoning("low")


if __name__ == "__main__":
    main()