from dotenv import load_dotenv
import os

import anthropic

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")


client = anthropic.Anthropic(api_key=api_key)

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What AI Enginner are doing or implementen now with Anthropic?",
        }
    ],
)
print(message.content)
