import os
import sys
import openai
import argparse
from dotenv import load_dotenv

def send_to_gpt(input_text):
    load_dotenv()

    api_base = os.getenv("OPENAI_API_BASE")
    api_key = os.getenv("OPENAI_API_KEY")

    openai.api_base = api_base
    openai.api_key = api_key

    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text}
            ]
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    parser = argparse.ArgumentParser(description="Send input text to GPT-4 API and print the response.")
    args = parser.parse_args()
    
    input_text = sys.stdin.read()
    response = send_to_gpt(input_text)
    print(response)

if __name__ == "__main__":
    main()
