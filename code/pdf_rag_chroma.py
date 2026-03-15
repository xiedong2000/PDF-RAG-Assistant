print("Program started...")

from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
from pypdf import PdfReader
import chromadb

from rag_engine import create_embedding, create_embeddings, retrieve_context, generate_answer

load_dotenv()

client = OpenAI()

# Setup ChromaDB
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="documents")

BASE_DIR = Path(__file__).resolve().parent.parent
pdf_path = BASE_DIR / "docs" / "ai_overview.pdf"

# Read PDF
reader = PdfReader(pdf_path)
text = ""

for page in reader.pages:
    text += page.extract_text()

# Chunk text
chunk_size = 500
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

print(f"Loaded {len(chunks)} chunks")

# Store chunks if database empty
if collection.count() == 0:

    print("Creating embeddings and storing in vector DB...")

    # response = client.embeddings.create(
    #     model="text-embedding-3-small",
    #     input=chunks
    # )

    # embeddings = [d.embedding for d in response.data]

    embeddings = create_embeddings(chunks)

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[str(i) for i in range(len(chunks))]
    )
else:
    print("Using existing vector database...")

query = input("Ask a question about the PDF: ")

query_embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
).data[0].embedding

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

context = "\n".join(results["documents"][0])

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "Answer using the document context."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
    ]
)

print("\nAI Answer:\n")
print(response.choices[0].message.content)