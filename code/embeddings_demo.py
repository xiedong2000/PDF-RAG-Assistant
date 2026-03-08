from openai import OpenAI
import numpy as np

# Initialize client
# Option 1: Use environment variable OPENAI_API_KEY
client = OpenAI(api_key="***REMOVED***")

# Sample sentences
texts = [
    "AI will transform software engineering.",
    "Artificial intelligence changes how developers work.",
    "Machine learning is widely used in software development."
]

# Generate embeddings for all sentences
embeddings = []
for t in texts:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=t
    )
    embeddings.append(response.data[0].embedding)

# Print embedding length for first sentence
print(f"Embedding vector length: {len(embeddings[0])}\n")

# Compute semantic similarity between each pair
for i in range(len(texts)):
    for j in range(i + 1, len(texts)):
        emb1 = embeddings[i]
        emb2 = embeddings[j]
        similarity = np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
        print(f"Similarity between:\n'{texts[i]}'\nand\n'{texts[j]}'\n→ {similarity:.3f}\n")