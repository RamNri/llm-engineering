from openai import OpenAI


#ollama
#Downalod the smallest of the models
#install ollama, and then ollma pull llama3.2:1b
#api_key can be anything, since this is running on your system

OLLAMA_BASE_URL = "http://localhost:11434/v1"

ollama = OpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key="ollama",
)


response = ollama.chat.completions.create(
    model="llama3.2:1b",
    messages=[
        {
            "role": "user",
            "content": "Tell me a fun fact",
        }
    ],
)


print(response.choices[0].message.content)