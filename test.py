import os
import json
import sys

def run_ollama_chat(messages):
    try:
        print('1')
        ollama_binary = '/home/cpitumpeappu/cryptoscam/llm/ollama-linux-amd64.1'

        command = [ollama_binary, 'run', 'llama2']  
        print('2')
        with open('ollama_input.json', 'w') as f:
            json.dump(messages, f)
        print('3')
        result = os.system(' '.join(command) + ' < ollama_input.json')
        print('4')

        # Check if the command was successful
        if result == 0:
            # Read the response from the temporary file
            with open('ollama_output.json', 'r') as f:
                response = json.load(f)
            return response
        else:
            print("Error:", "Ollama binary execution failed")
            return None

    except FileNotFoundError:
        print("Ollama binary not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None
    finally:
        # Clean up temporary files
        os.remove('ollama_input.json')
        os.remove('ollama_output.json')

if __name__ == "__main__":
    # Define the messages to send to Ollama
    print('5')
    messages = [
        {
            'role': 'user',
            'content': 'Why is the sky blue?',
        },
    ]

    # Run the Ollama chat
    response = run_ollama_chat(messages)

    # Print the response
    if response:
        print(response['message']['content'])
