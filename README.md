# PDF-RAG-Assistant

![Python](https://img.shields.io/badge/python-3.12-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-API-brightgreen)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-orange)
![License](https://img.shields.io/github/license/xiedong2000/PDF-RAG-Assistant)
![GitHub last commit](https://img.shields.io/github/last-commit/xiedong2000/PDF-RAG-Assistant)
![GitHub issues](https://img.shields.io/github/issues/xiedong2000/PDF-RAG-Assistant)
![GitHub pull requests](https://img.shields.io/github/issues-pr/xiedong2000/PDF-RAG-Assistant)

---

## Overview

**PDF-RAG-Assistant** is a Retrieval-Augmented Generation (RAG) assistant that answers questions from **PDF, DOCX, and TXT** files (via the Streamlit app), with additional PDF-focused scripts under `code/`.  
It uses:

- **OpenAI embeddings** to convert text into numerical vectors
- **Chroma** to store and retrieve document embeddings
- **Streamlit** for interactive multi-file upload and Q&A
- **Vector database caching** in the CLI scripts to avoid repeated embedding work

This project demonstrates **real-world AI system design** and is structured for modularity and reusability.

---

## Project Structure

```
PDF-RAG-Assistant/
│
├── app/                     # Streamlit UI: PDF, DOCX, TXT upload and Q&A
├── code/                    # Python scripts
│   ├── rag_engine.py        # Embeddings, retrieval, answer generation
│   ├── rag_document_assistant.py
│   ├── pdf_rag_assistant.py
│   └── pdf_rag_chroma.py
├── docs/                    # Screenshots for README
│   ├── upload_ui.png
│   └── qa_example.png
├── documents/               # Sample PDF or text documents
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Setup Instructions

1. **Install Python 3.12+**  
2. **Create virtual environment**:

```bash
python -m venv ai-env
```

3. **Activate environment**:

```bash
# Windows
ai-env\Scripts\activate
```

4. **Install dependencies** (includes `pdfplumber`, `python-docx` for DOCX, `streamlit`, `chromadb`, etc.):

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Use the **same virtual environment** when you run `streamlit run`; otherwise you may see `ModuleNotFoundError: No module named 'docx'`—fix with `pip install python-docx` or re-run `pip install -r requirements.txt` in that environment.

5. **Create `.env` file** in the project root and add your OpenAI key:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

6. **Place PDF or text documents** in `documents/` folder.

---

## Usage

### RAG Document Assistant

`rag_document_assistant.py` demonstrates a basic RAG pipeline.

- Loads documents
- Converts them into embeddings
- Retrieves the most relevant document for a question using cosine similarity
- Generates an answer using OpenAI

### PDF Document Assistant

`pdf_rag_assistant.py` demonstrates a RAG pipeline for PDF documents.

- Extracts text from a PDF
- Splits text into chunks
- Generates embeddings and stores them in **Chroma vector database**
- Retrieves relevant chunks and generates answers
- **Vector database caching** avoids repeated embeddings for faster runs

### PDF RAG Chroma Assistant

`pdf_rag_chroma.py` is an enhanced version:

- Reads PDFs
- Splits into chunks
- Stores embeddings in **persistent ChromaDB**
- Reuses embeddings if already present
- Optimized for speed and cost
- Shows modular design calling functions from `rag_engine.py`

### Streamlit App

The `app/` folder contains a Streamlit app (`streamlit_app.py`):

- Interactive web interface for uploading **one or more PDF, DOCX, or TXT** files at once
- Text is chunked per file with `[Source: filename]` so answers can be grounded in the right document
- DOCX ingestion includes paragraphs and table cell text; TXT is read as UTF-8 (invalid bytes replaced)
- Ask questions across all indexed documents in real time
- Uses embeddings + Chroma retrieval (`user_documents` collection) and OpenAI for answers  
- If `python-docx` is missing, PDF and TXT still work; uploading a DOCX shows an install hint in the UI

Run the Streamlit app with:

```bash
streamlit run app/streamlit_app.py
```

---

## Demo

### Upload (PDF; UI also supports DOCX and TXT)

![Upload PDF](docs/upload_ui.png)

### Ask Questions About the Document

![Question Answer](docs/qa_example.png)

---

## Key Features

- Modular RAG engine (`rag_engine.py`)  
- PDF ingestion and text chunking  
- **Multi-file upload** (PDF, DOCX, TXT) in the Streamlit UI with per-file source labels in chunks  
- Embedding generation and caching  
- Persistent vector database (ChromaDB)  
- Streamlit web UI for interactive questions  
- Portfolio-ready structure for recruiters and engineers

---

## Notes

- Make sure `.env` contains your **OpenAI API key**  
- Do not commit `.env` or `ai-env/` to GitHub  
- **DOCX** requires the `python-docx` package (listed in `requirements.txt`); legacy `.doc` is not supported  
- Requires Python 3.12+ to run `pdf_rag_chroma.py` due to SQLite version requirements  

---

## Future Improvements

- Persist Chroma data across Streamlit sessions and avoid re-embedding on every rerun  
- Add user authentication and cloud deployment  
- Surface retrieved chunk sources in the UI (expandable citations)

