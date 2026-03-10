print("Program started...")

from openai import OpenAI
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# Load documents
documents = []

with open("../docs/ai_notes.txt", "r", encoding="utf-8") as f:
    documents.append(f.read())


doc_embeddings = [get_embedding(doc) for doc in documents]

query = input("Ask a question: ")

query_embedding = get_embedding(query)

similarities = [
    cosine_similarity(query_embedding, doc_embedding)
    for doc_embedding in doc_embeddings
]

best_match_index = np.argmax(similarities)

context = documents[best_match_index]


response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "Answer the question using the provided context."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
    ]
)

print("\nAI Answer:\n")
print(response.choices[0].message.content)