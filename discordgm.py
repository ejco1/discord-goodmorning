import requests
import random
import json
import openai

with open(r"config.json", 'r') as config:
    config_data = json.load(config)

urls = config_data["urls"]
auth = {'authorization': config_data["authKey"]}
openai.api_key = config_data["api_key"]
question = config_data["question"]

def ask_chatgpt(question):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the appropriate GPT-3.5 engine
        prompt=question,
        max_tokens=50,  # Adjust max tokens as needed for your response length
        temperature=0.7,  # Adjust temperature for response randomness
    )
    
    return response.choices[0].text.strip()

def main():
    for url in urls:
        requests.post(url, headers = auth, data = {'content': ask_chatgpt(question)})

if __name__ == "__main__":
    main()

