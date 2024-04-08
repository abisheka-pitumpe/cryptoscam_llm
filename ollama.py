import pandas as pd
import json
import requests 


df = pd.read_csv('data/positives.csv.txt')

df['LLM Results'] = ''  

base_url = "http://localhost:11434/api/chat"

for index, row in df.iterrows():
    messages = [
        {
            "role": "system",
            "content": "You are a financial advisor programmed to respond in JSON format. Your responses are limited to 'yes' or 'no', represented by the 'answer' key, and you must provide a one-word reasoning for your decision under the 'reason' key. Be sure of your answer."
        },
        {
            "role": "user",
            "content": "Determine if the provided (summarized) text likely originates from a cryptocurrency investment scam website, characterized by promises of high returns from cryptocurrency investments. If the text suggests a low probability of being a scam, does not prompt users to log in/sign up, seems like a news site, or does not solicit users to contact the site for investing in cryptocurrency, respond 'no'."
        },
        {
            "role": "assistant",
            "content": "Sure. Please provide the text in question."
        },
        {"role": "user", "content": row["Text"]}
    ]

    payload = {
        "model": "llama2:13b",  
        "messages": messages,
        "stream": False  
    }

    response = requests.post(base_url, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        chat_response = response_data.get("message", {}).get("content", "")
        df.at[index, 'LLM Results'] = chat_response
    else:
        print(f"Error for row {index}: {response.text}")
        df.at[index, 'LLM Results'] = 'Error'  

df.to_csv('results_pos.csv', index=False)
