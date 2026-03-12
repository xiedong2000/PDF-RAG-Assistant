print("Program started...")

from openai import OpenAI
import numpy as np
from dotenv import load_dotenv
from pathlib import Path
from pypdf import PdfReader

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


# Locate project root
BASE_DIR = Path(__file__).resolve().parent.parent
pdf_path = BASE_DIR / "docs" / "ai_overview.pdf"


# Extract text from PDF
reader = PdfReader(pdf_path)

document_text = ""

for page in reader.pages:
    document_text += page.extract_text()


# Split text into chunks
chunk_size = 500
chunks = [
    document_text[i:i + chunk_size]
    for i in range(0, len(document_text), chunk_size)
]


print(f"Document split into {len(chunks)} chunks")


# Create embeddings
chunk_embeddings = [get_embedding(chunk) for chunk in chunks]


query = input("Ask a question about the PDF: ")

query_embedding = get_embedding(query)


similarities = [
    cosine_similarity(query_embedding, emb)
    for emb in chunk_embeddings
]

best_chunk_index = np.argmax(similarities)

context = chunks[best_chunk_index]


response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "Answer using the provided document context."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
    ]
)

print("\nAI Answer:\n")
print(response.choices[0].message.content)