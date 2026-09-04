from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai = OpenAI()
response = openai.chat.completions.create(model="gpt-5-nano", messages=[{
  "role" : "user",
  "content": "Tell me a fun fact"
}])

response.choice[0].message.content

#we can use openai python client library to connect to gemini as well
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai"
google_api_key = os.getenv("GEMINI_API_KEY")
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
response = gemini.chat.completions.create(model="gemini-2.5-pro",
                                          messages=[{"role":"user",
                                                     "content": "Tell me a fun fact"}])
print(response.choices[0].message.content)
