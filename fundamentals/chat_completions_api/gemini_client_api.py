from google import genai   #google-genai
import os
from dotenv import load_dotenv

load_dotenv(override=True)

MODEL = "gemini-3-flash-preview"
api_key=os.getenv("GEMINI_API_KEY")

if not api_key:
  raise ValueError("GEMINI_API_KEY was not found int the environment")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(model=MODEL,
  contents="Describe color  blue to someone who has never been able to see in 1 sentence")
print(response.text)

