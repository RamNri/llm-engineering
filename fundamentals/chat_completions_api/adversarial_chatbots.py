import os
from dotenv import load_dotenv
from openai import OpenAI
from utils.retry import call_llm_with_retry

load_dotenv(override=True)
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
  raise ValueError(
    "GEMINI_API_KEY was not found in the environment"
  )

GEMINI_BASE_URL= ("https://generativelanguage.googleapis.com/v1beta/openai")
MODEL = "gemini-3-flash-preview"

client = OpenAI(base_url=GEMINI_BASE_URL, api_key=api_key)


#Define 2 personalities

ARGUMENTATIVE_SYSTEM_PROMPT = """
You are an argumentative chatbot.
You tend to disagree with statements made byt he other chatbot
Challenge assumptions and express opposing viewpoints.
Be witty and slightly snarky, but o not be offensive or abusive
keep your responses conversataional and reasonably sort
"""

POLITE_SYSTEM_PROMPT = """
You are polite, friendly, and courteous chatbot.
Try to find common ground with the other chatbot.
if the other chatbot becomes argumentative, remain calm.
Respond thoughtfully and try to keep the converstation constructive.
Keep your response conversational and reasonaly short
"""

#stor conversational history

argumentative_messages = []
polite_messages = []

#call arugementative chatbot
def call_argumentative_bot(user_message):
  messages = [
    {
      "role" : "system",
      "content" : ARGUMENTATIVE_SYSTEM_PROMPT
    }
  ]

  messages.extend(argumentative_messages)
  messages.append(
    {
      "role" : "user",
      "content" : user_message
  }
  )
  response = call_llm_with_retry( 
    lambda: client.chat.completions.create(model=MODEL, messages=messages))
  
  answer = response.choices[0].message.content
  argumentative_messages.append(
    {
      "role" : "user",
      "content" : user_message
    }
  )

  argumentative_messages.append(
    {
      "role" : "assistant",
      "content" : answer
 
  })

  return answer

## call polite chatbot

def call_polite_bot(user_message):
  messages = [
    {
      "role": "system",
      "content" : POLITE_SYSTEM_PROMPT
    }
  ]
  messages.extend(polite_messages)
  messages.append(
    {
      "role" : "user",
      "content" : user_message
    }
  )
  response = call_llm_with_retry(
    lambda: client.chat.completions.create(model=MODEL, messages= messages,))

  answer = response.choices[0].message.content
  polite_messages.append(
  {
    "role" : "user",
    "content" : user_message
  })

  polite_messages.append(
    {
      "role" : "assistant",
      "content": answer
    }
  )

  return answer

#Run the conversation

def main():
 opening_message = "Hi! What do you thing is the most important invention in human histoyr?"
 print("\n==============================")
 print("POLITE BOT")
 print("\n=====================================")

 polite_response = call_polite_bot(opening_message)
 print(polite_response)

 print("\n==============================")
 print("ARGUMENTATIVE BOT")
 print("==============================")

 argumentative_response = call_argumentative_bot(polite_response)
 print(argumentative_response)

 for _ in range(5):
    print("\n==============================")
    print("POLITE BOT")
    print("==============================")
    polite_response = call_polite_bot(
            argumentative_response
        )

    print(polite_response)


    print("\n==============================")
    print("ARGUMENTATIVE BOT")
    print("==============================")

    argumentative_response = call_argumentative_bot(
            polite_response
        )

    print(argumentative_response)

 
if __name__ == "__main__":
  main()