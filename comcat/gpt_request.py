import os
import sys
import openai
from dotenv import load_dotenv

def send_to_gpt(input_text):
    load_dotenv()

    api_base = os.getenv("OPENAI_API_BASE")
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_base or not api_key:
        return "Environment variables OPENAI_API_BASE and OPENAI_API_KEY must be set."

    openai.api_base = api_base
    openai.api_key = api_key

    try:
        response = openai.chat.completions.create(
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
    input_text = sys.stdin.read()
    response = send_to_gpt(input_text)
    print(response)

if __name__ == "__main__":
    main()
