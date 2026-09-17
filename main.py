import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None:
    raise RuntimeError("No API key found.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="AI Agent")
parser.add_argument("user_message", type=str, help="Please type a message.")
args = parser.parse_args()

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
            {
                "role": "user",
                "content": args.user_message,
            }
        ],
)

if response.usage == None:
    raise RuntimeError("API request failed.")
print(f"Prompt tokens: {response.usage.prompt_tokens}")
print(f"Response tokens: {response.usage.completion_tokens}")
print(response.choices[0].message.content)

def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
