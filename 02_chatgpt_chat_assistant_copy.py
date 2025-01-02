import os
from dotenv import load_dotenv
from openai import OpenAI
import openai


load_dotenv()
open_api_key = os.getenv("API_KEY")
client = OpenAI(api_key=open_api_key,)

openai.api_key = open_api_key

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")