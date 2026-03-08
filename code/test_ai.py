from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize client
# Option 1: Use environment variable OPENAI_API_KEY
client = OpenAI()

# Send a simple prompt
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Explain embeddings in machine learning simply."}
    ]
)

# Print the AI response
print("AI Response:\n")
print(response.choices[0].message.content)