import os
import openai
import requests
from dotenv import load_dotenv

load_dotenv()

openai.organization = "org-0Xwb0hmXVwdUGhFhYo05D2AC"
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.Model.list()


def callChatGPT(content):
    url = "https://api.openai.com/v1/chat/completions"
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": content}],
    }

    access_token = os.environ["OPENAI_API_KEY"]
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print("POST request was successful")
        print(type(response.json()))
        print(response.json()["choices"][0]["message"]["content"])
    else:
        print(f"POST request failed with status code {response.status_code}")
        print(response.text)


def callViaNative(content):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}]
    )

    print(type(completion))
    print(completion.choices[0].message.content)


callChatGPT("how are you?")
callViaNative("who are you?")
