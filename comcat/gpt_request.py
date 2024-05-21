import os
import sys
import openai
import argparse

def send_to_gpt(api_base, api_key, input_text):
    openai.api_base = api_base
    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
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
    parser.add_argument("--api_base", required=True, help="The base URL of the GPT-4 API.")
    parser.add_argument("--api_key", required=True, help="Your API key for the GPT-4 API.")
    
    args = parser.parse_args()
    
    input_text = sys.stdin.read()
    response = send_to_gpt(args.api_base, args.api_key, input_text)
    print(response)

if __name__ == "__main__":
    main()
