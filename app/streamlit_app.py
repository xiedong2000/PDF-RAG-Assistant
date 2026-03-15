import streamlit as st
from openai import OpenAI
import chromadb
from pypdf import PdfReader
import os

st.title("📄 Chat with Your PDF")

client = OpenAI()

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    st.write(f"Document split into {len(chunks)} chunks")

    chroma_client = chromadb.Client()
    collection = chroma_client.get_or_create_collection(name="pdf_docs")

    for i, chunk in enumerate(chunks):
        embedding = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk
        ).data[0].embedding

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[str(i)]
        )

    question = st.text_input("Ask a question about the document")

    if question:

        q_embedding = client.embeddings.create(
            model="text-embedding-3-small",
            input=question
        ).data[0].embedding

        results = collection.query(
            query_embeddings=[q_embedding],
            n_results=2
        )

        context = "\n".join(results["documents"][0])

        prompt = f"""
        Answer the question using the context below.

        Context:
        {context}

        Question:
        {question}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.subheader("Answer")
        st.write(response.choices[0].message.content)