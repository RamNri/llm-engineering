from dotenv import load_dotenv
from openai import OpenAI

import json
import os

from utils.scraper import (
    fetch_website_content,
    fetch_website_links
)


load_dotenv(override=True)


api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY was not found in the environment."
    )


LINK_MODEL = "gpt-5-nano"

BROCHURE_MODEL = "gpt-4.1-mini"


LINK_SYSTEM_PROMPT = """
You are provided with a list of links found on a company website.

Your task is to decide which links would be most relevant
for creating a brochure about the company.

Relevant pages may include:

- About
- Company
- Products
- Services
- Careers
- Jobs

Do not select:

- Privacy Policy
- Terms of Service
- Login pages
- Email links

Respond with JSON in the following format:

{
    "links": [
        {
            "type": "about page",
            "url": "https://example.com/about"
        }
    ]
}
"""


BROCHURE_SYSTEM_PROMPT = """
You are an assistant that analyzes content from several pages
of a company website and creates a short brochure about the company.

The brochure should be useful for:

- Customers
- Investors
- Potential recruits

Include relevant information about:

- The company
- Products or services
- Company culture
- Customers
- Careers and jobs

Only use information provided in the website content.

Respond in Markdown.

Do not wrap the response inside a Markdown code block.
"""


client = OpenAI()


def get_links_user_prompt(url):
    """Create the user prompt containing all website links."""

    links = fetch_website_links(url)

    user_prompt = f"""
Here is a list of links found on the company website:

{url}

Please identify the links most relevant for creating
a brochure about the company.

Links:

"""

    user_prompt += "\n".join(links)

    return user_prompt


def select_relevant_links(url):
    """Use an LLM to select links relevant to the company brochure."""

    print(
        f"Selecting relevant links for {url} "
        f"using {LINK_MODEL}..."
    )

    response = client.chat.completions.create(

        model=LINK_MODEL,

        messages=[
            {
                "role": "system",
                "content": LINK_SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": get_links_user_prompt(url)
            }
        ],

        response_format={
            "type": "json_object"
        }
    )

    result = response.choices[0].message.content

    return json.loads(result)


def fetch_page_and_relevant_links(url):
    """Fetch the landing page and all LLM-selected relevant pages."""

    landing_page_content = fetch_website_content(url)

    relevant_links = select_relevant_links(url)

    result = (
        f"## Landing Page\n\n"
        f"{landing_page_content}\n\n"
        f"## Relevant Pages\n"
    )

    for link in relevant_links["links"]:

        result += (
            f"\n\n### {link['type']}\n\n"
        )

        page_content = fetch_website_content(
            link["url"]
        )

        result += page_content

    return result


def get_brochure_user_prompt(company_name, url):
    """Create the prompt containing website content for the brochure."""

    user_prompt = f"""
You are looking at a company called:

{company_name}

Below is content from its landing page and other relevant pages.

Use this information to create a short company brochure.

"""

    user_prompt += fetch_page_and_relevant_links(url)

    return user_prompt[:5000]


def create_brochure(company_name, url):
    """Create a company brochure using the selected website content."""

    response = client.chat.completions.create(

        model=BROCHURE_MODEL,

        messages=[
            {
                "role": "system",
                "content": BROCHURE_SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": get_brochure_user_prompt(
                    company_name,
                    url
                )
            }
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    brochure = create_brochure(
        "Hugging Face",
        "https://huggingface.co"
    )

    print(brochure)