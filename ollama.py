import pandas as pd
import subprocess

# Load the final dataset
df = pd.read_csv('merged_randomized.csv')

# Define the prompt
prompt = 'You are a financial advisor that responds in JSON. Could this text belong to a website that offers investment plans and guarentees high profits? Say yes or no, nothing else.'

# Initialize a list to store the results
df['LLM Results'] = ''  # Add an empty column for results

for index, row in df.iterrows():
    input_text = f'{prompt} {row["Text"]}'
    command = ['ollama', 'run', 'llama2', input_text]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    # Assuming stdout contains the desired output
    # Update the DataFrame directly with the result
    df.at[index, 'LLM Results'] = stdout.strip()

# Save the updated DataFrame to a CSV file
df.to_csv('results.csv', index=False)
