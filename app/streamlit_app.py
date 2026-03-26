import streamlit as st
from openai import OpenAI
import chromadb
import pdfplumber
import os
from dotenv import load_dotenv

load_dotenv()

st.title("📄 Chat with Your PDF")

client = OpenAI()

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:

    with pdfplumber.open(uploaded_file) as pdf:
        text = ""

        for page_num, page in enumerate(pdf.pages):
            try:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            except Exception as e:
                st.warning(f"Could not extract text from page {page_num + 1}: {str(e)}")
                # Skip this page and continue
                continue

    if not text.strip():
        st.error("Could not extract any text from the PDF. Please try a different PDF file.")
        st.stop()

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