import pandas as pd
import subprocess

# Load the final dataset
df = pd.read_csv('negatives_150.csv')
print("Loaded CSV")
# Define the prompts
system_prompt = "You are a financial advisor programmed to respond in JSON format. Your responses are limited to 'yes' or 'no', represented by the 'answer' key, and you must provide a one-word reasoning for your decision under the 'reason' key. Be sure of your answer."
user_prompt = "Determine if the provided (summarized) text likely originates from a cryptocurrency investment scam website, characterized by promises of high returns from cryptocurrency investments. If the text suggests a low probability of being a scam, does not prompt users to log in/sign up, seems like a news site, or does not solicit users to contact the site for investing in cryptocurrency, respond 'no'."
assistant_prompt = "Sure. Please provide the text in question."

ollama_binary = '/home/cpitumpeappu/cryptoscam/llm/ollama-linux-amd64.1'

# Initialize a list to store the results
df['LLM Results'] = ''  # Add an empty column for results
print("Added column to store results")

for index, row in df.iterrows():
    # Build the conversation
    input_messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
        {"role": "assistant", "content": assistant_prompt},
        {"role": "user", "content": row["Text"]}
    ]

    # Convert messages to text
    input_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in input_messages])

    # Run Ollama
    command = [ollama_binary, 'run', 'llama3:70b', input_text]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    # Extract response
    chat_response = stdout.strip()

    # Save result to DataFrame
    df.at[index, 'LLM Results'] = chat_response

# Save the updated DataFrame to a CSV file
df.to_csv('results_neg_llama3_70b.csv', index=False)

