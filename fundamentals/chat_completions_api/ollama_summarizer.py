from openai import OpenAI
from scraper import fetch_website_content

#insall ollma then pull below model using ollam pull llama3.2:1b
MODEL = "llama3.2:1b"

OLLAMA_BASE_URL = "http://localhost:11434/v1"

SYSTEM_PROMPT = """You are a professor that analyzes the contents of a website,
and provides a short summary, ignoring decorative, naviagational texts.

Do not wrap the markdown in a code block - respond just with the markdown."""

USER_PROMPT = """Here is the content of the website, provide a short summary of the website"""

def crafted_message(website_content):
  """create message list for LLM"""

  return [
    {
    "role" : "system", "content" : SYSTEM_PROMPT,
    },
    {
    "role" : "user", "content" : USER_PROMPT + website_content
    },
  ]

def summarize(url):
  "Fetch and summarize a website using LLM"
  ollama = OpenAI(base_url= OLLAMA_BASE_URL, api_key="ollma")
  website_content = fetch_website_content(url)
  response = ollama.chat.completions.create(
                                              model = MODEL,
                                              messages = crafted_message(website_content) 
                                              )
  return response.choices[0].message.content



def main():
  url = input("Enter the url")
  print("\n Fetching and summarizing \n")
  summary = summarize(url)
  print(summary)

if __name__ == "__main__":
  main()
  