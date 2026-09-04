from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}


def fetch_website_content(url):
    """Fetch and extract meaningful text content from a website."""

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.content,
        "html.parser"
    )

    title = soup.title.string if soup.title else "No title found"

    if soup.body:

        for not_relevant in soup.body(
            ["script", "style", "img", "input"]
        ):
            not_relevant.decompose()

        text = soup.body.get_text(
            separator="\n",
            strip=True
        )

    else:
        text = ""

    return (title + "\n\n" + text)[:3000]


def fetch_website_links(url):
    """Fetch and return absolute links found on a website."""

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.content,
        "html.parser"
    )

    links = []

    for link in soup.find_all("a"):

        href = link.get("href")

        if href:
            full_url = urljoin(url, href)
            links.append(full_url)

    return links