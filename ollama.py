import pandas as pd
import subprocess

df = pd.read_csv('ocr.csv')
new_txt = [x.strip() for x in open('true_positive_urls.txt').readlines()]

prompt = 'You are a financial advisor that responds in JSON. Could this text belong to a website that is a cryptocurrency news site? Say yes or no, nothing else.'

for index, row in df.iterrows():
    if row["URL"] not in new_txt:
        continue
    input_text = f'{prompt} {row["Text"]}'

    command = ['ollama', 'run', 'llama2', input_text]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    print(f'URL: {row["URL"]}, Response: {stdout.decode()}')

    if stderr:
        print(stderr.decode())
