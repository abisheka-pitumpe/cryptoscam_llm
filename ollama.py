import pandas as pd
import subprocess

positives_df = pd.read_csv('positives.csv')
negatives_df = pd.read_csv('negatives.csv')
combined_df = pd.concat([positives_df, negatives_df])
final_df = combined_df.sample(frac=1).reset_index(drop=True)
#convert final_df into a csv file and save it
final_df.to_csv('final.csv', index=False)


prompt = 'You are a financial advisor that responds in JSON. Could this text belong to a website that is a cryptocurrency news site? Say yes or no, nothing else.'

for index, row in final_df.iterrows():
    
    input_text = f'{prompt} {row["Text"]}'

    command = ['ollama', 'run', 'llama2', input_text]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    print(f'URL: {row["URL"]}, Response: {stdout.decode()}')

    if stderr:
        print(stderr.decode())
