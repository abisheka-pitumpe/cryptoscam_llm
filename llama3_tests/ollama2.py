import requests
import pandas as pd

# Load the final dataset
df = pd.read_csv('data/negatives.csv.txt')

# Specify the base URL of the ollama API
base_url = "http://localhost:11434/api/generate"

# Initialize a list or column in your DataFrame to store the LLM results
df['LLM Results'] = ''  # Adding an empty column for results

for index, row in df.iterrows():
    # Prepare the data payload for the POST request
    payload = {
        "model": "llama2:13b",  # Specify the model you're using
        "prompt": row["Text"],  # Use the text from your DataFrame
        "stream": False  # Adjust based on your needs; false for a single response
    }

    # Make the POST request to the ollama API
    response = requests.post(base_url, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        response_data = response.json()  # Parse the JSON response
        # Extract the response text or any other relevant data
        # This assumes 'response' is the key where the generated text is stored;
        # adjust based on actual API response structure
        generated_text = response_data.get("response", "")
        # Store the generated text or processed information in your DataFrame
        df.at[index, 'LLM Results'] = generated_text
    else:
        print(f"Error processing row {index}: {response.text}")
        df.at[index, 'LLM Results'] = 'Error'  # Mark rows that couldn't be processed

# Optionally, save the updated DataFrame to a new CSV file
df.to_csv('results_with_llm_responses.csv', index=False)
