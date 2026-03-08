from openai import OpenAI

# Initialize client
client = OpenAI(api_key="***REMOVED***")

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