# OpenAI-Test

**Requirements:** Python 3.12+, OpenAI API key

## Overview
This repository contains Python projects demonstrating the use of **OpenAI API** for building AI-powered tools.  
It showcases practical skills in **prompt engineering, API integration, embeddings, and semantic similarity** — foundational for AI knowledge assistants and RAG systems.

## Project Components

### 1. Prompt Testing and LLM Integration
- File: `code/test_ai.py`
- Sends prompts to a large language model (LLM) and prints responses
- Demonstrates ability to **integrate OpenAI API** and understand **prompt behavior**
- Prepares for **multi-turn AI workflows and agent simulations**

### 2. Embeddings and Semantic Understanding
- File: `code/embeddings_demo.py`
- Generates **embedding vectors** for multiple sentences using OpenAI API
- Computes **semantic similarity** between sentence pairs to show how AI captures meaning rather than exact words
- Demonstrates the foundation for **Retrieval-Augmented Generation (RAG) pipelines** and AI-powered knowledge assistants
- Output includes:
  - Length of embedding vectors
  - Similarity scores between all sentence pairs

### Semantic Search Demo

`vector_search_demo.py` demonstrates how embeddings
and cosine similarity can be used to implement a
simple semantic search engine. This is a core component
of Retrieval-Augmented Generation (RAG) systems used
in modern AI assistants.

### RAG Document Assistant

`rag_document_assistant.py` demonstrates a basic Retrieval-Augmented
Generation (RAG) pipeline.

The script loads documents, converts them into embeddings, retrieves
the most relevant document for a question using cosine similarity,
and uses an OpenAI model to generate an answer based on that context.

### PDF Document Assistant

`pdf_rag_assistant.py` demonstrates a Retrieval-Augmented
Generation (RAG) pipeline that can answer questions about
a PDF document.

### PDF RAG Assistant with Vector Database

`pdf_rag_chroma.py` demonstrates a Retrieval-Augmented
Generation (RAG) pipeline that uses a vector database
to store and retrieve document embeddings.

The script extracts text from a PDF document, splits the text into smaller chunks, generates embeddings using the OpenAI API, and stores those embeddings in ChromaDB. The vector database is reused across runs to avoid regenerating embeddings.

When a user asks a question, the script retrieves the
most relevant document chunks using semantic similarity
search and uses an OpenAI model to generate an answer
based on the retrieved context.

### Vector Database Caching

To avoid recreating embeddings every time the script runs, the application checks whether the vector database already contains stored embeddings.

If embeddings exist, the script reuses the existing vector database instead of generating new embeddings.

Benefits:

* Reduces OpenAI API calls
* Improves performance
* Demonstrates a common optimization used in production Retrieval-Augmented Generation systems


The script:
1. Extracts text from a PDF
2. Splits the document into chunks
3. Generates embeddings for each chunk
4. Finds the most relevant context using cosine similarity
5. Uses an LLM to generate an answer based on the retrieved context

### AI Document Chat Web App

`streamlit_app.py` provides a web interface for the
PDF RAG assistant using Streamlit.

Users can upload a PDF document and ask questions
about the document content. The application
retrieves relevant text using vector similarity
search and generates answers using the OpenAI API.

## Setup

This project requires Python 3.12 or later.

### Create a virtual environment
Use Python 3.12 to create a virtual environment for the project.
- py -3.12 -m venv ai-env
Activate the environment:
- ai-env\Scripts\activate
Verify the Python version:
- python --version
python --version: 
- Python 3.12.x
Install dependencies:
- pip install -r requirements.txt
Install python-dotenv if not already installed:
- pip install python-dotenv
Install chroma, streamlit if not already installed:

Set your OpenAI API key securely
- Create a .env file in the project root with the following content:
- OPENAI_API_KEY=sk-XXXX
- Make sure .env is listed in .gitignore so it is never pushed to GitHub
Run the scripts:
- python code/test_ai.py
- python code/embeddings_demo.py
- test_ai.py → tests basic LLM prompts
- embeddings_demo.py → generates embeddings and computes semantic similarity