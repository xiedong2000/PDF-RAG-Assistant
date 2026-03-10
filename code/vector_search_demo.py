print("Program started...")

from openai import OpenAI
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

documents = [
    "Embeddings convert text into numerical vectors.",
    "Python is a popular programming language for AI.",
    "RAG combines retrieval and generation for better answers.",
    "Machine learning trains models on data."
]

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


doc_embeddings = [get_embedding(doc) for doc in documents]

query = "How does RAG work?"

query_embedding = get_embedding(query)

similarities = [
    cosine_similarity(query_embedding, doc_embedding)
    for doc_embedding in doc_embeddings
]

best_match_index = np.argmax(similarities)

print("User Question:")
print(query)

print("\nBest Matching Document:")
print(documents[best_match_index])