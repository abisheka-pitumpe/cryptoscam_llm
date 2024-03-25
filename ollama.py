import pandas as pd
import subprocess

# Load the final dataset
final_df = pd.read_csv('final.csv')

# Define the prompt
prompt = 'You are a financial advisor that responds in JSON. Could this text belong to a website that is a cryptocurrency news site? Say yes or no, nothing else.'

# Initialize a list to store the results
final_df['Results'] = ''  # Add an empty column for results

for index, row in final_df.iterrows():
    input_text = f'{prompt} {row["Text"]}'
    command = ['ollama', 'run', 'llama2', input_text]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    # Assuming stdout contains the desired output
    # Update the DataFrame directly with the result
    final_df.at[index, 'Results'] = stdout.strip()

# Save the updated DataFrame to a CSV file
final_df.to_csv('results.csv', index=False)
