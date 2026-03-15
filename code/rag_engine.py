from openai import OpenAI

client = OpenAI()


def create_embeddings(text_chunks):
    """Create embeddings for multiple text chunks"""

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text_chunks
    )

    embeddings = [d.embedding for d in response.data]

    return embeddings

def create_embedding(text):
    """Generate embedding for text"""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding


def retrieve_context(question, collection):
    """Retrieve most relevant document chunks"""

    question_embedding = create_embedding(question)

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=2
    )

    documents = results["documents"][0]

    context = "\n".join(documents)

    return context


def generate_answer(question, context):
    """Generate final answer using retrieved context"""

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content