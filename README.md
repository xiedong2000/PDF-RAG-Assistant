# OpenAI-Test

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

#### How to Run
1. Ensure you have your **OpenAI API key** set as an environment variable (`OPENAI_API_KEY`)  
2. **Install Python 3.8+ and pip** 
3. Install dependencies:
- 3a. Install python-dotenv if not already installed:
4. Set your OpenAI API key securely
- Create a .env file in the project root with the following content:
- OPENAI_API_KEY=sk-XXXX
- Make sure .env is listed in .gitignore so it is never pushed to GitHub
5. Run the scripts:
- python code/test_ai.py
- python code/embeddings_demo.py

- test_ai.py → tests basic LLM prompts
- embeddings_demo.py → generates embeddings and computes semantic similarity

```bash
pip install -r requirements.txt
pip install python-dotenv