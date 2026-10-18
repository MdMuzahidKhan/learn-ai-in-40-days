import json
import argparse
import os
import re
import math
from collections import Counter
from socket import timeout as SocketTimeout
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

try:
    from sentence_transformers import SentenceTransformer
except ModuleNotFoundError:
    SentenceTransformer = None

documents = [
    "Employees may work from home on Fridays.",
    "The office kitchen closes at 6 PM.",
    "All vacation requests must be approved by a manager.",
    "Passwords must be changed every 90 days.",
]


def chunk_whole_documents(source_documents):
    return list(source_documents)


def chunk_by_sentences(source_documents):
    sentence_chunks = []
    for document in source_documents:
        sentence_chunks.extend(
            [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", document) if sentence.strip()]
        )
    return sentence_chunks


def chunk_by_fixed_words(source_documents, chunk_size=8, overlap=0):
    words = []
    for document in source_documents:
        words.extend(tokenize(document))

    if chunk_size <= 0:
        return []

    step = max(1, chunk_size - overlap)
    chunks = []
    for start_index in range(0, len(words), step):
        window = words[start_index:start_index + chunk_size]
        if window:
            chunks.append(" ".join(window))
    return chunks


def chunk_by_sliding_window(source_documents, chunk_size=8, overlap=2):
    return chunk_by_fixed_words(source_documents, chunk_size=chunk_size, overlap=overlap)


def build_chunks(source_documents, strategy, chunk_size=8, overlap=2):
    if strategy == "whole":
        return chunk_whole_documents(source_documents)
    if strategy == "sentences":
        return chunk_by_sentences(source_documents)
    if strategy == "fixed":
        return chunk_by_fixed_words(source_documents, chunk_size=chunk_size, overlap=0)
    if strategy == "sliding":
        return chunk_by_sliding_window(source_documents, chunk_size=chunk_size, overlap=overlap)

    raise ValueError(f"Unsupported chunking strategy: {strategy}")

def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())


def cosine_similarity(vector_a, vector_b):
    shared_terms = set(vector_a) | set(vector_b)
    dot_product = sum(vector_a.get(term, 0) * vector_b.get(term, 0) for term in shared_terms)
    magnitude_a = math.sqrt(sum(value * value for value in vector_a.values()))
    magnitude_b = math.sqrt(sum(value * value for value in vector_b.values()))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def vectorize(text):
    return Counter(tokenize(text))


DEFAULT_OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
DEFAULT_OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")

def get_model_and_chunk_embeddings(chunks):
    if SentenceTransformer is not None:
        embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        return embedding_model, embedding_model.encode(chunks)

    return None, [vectorize(chunk) for chunk in chunks]


def retrieve_top_k(question, chunks, chunk_embeddings, embedding_model, top_k=2):
    if embedding_model is not None:
        question_embedding = embedding_model.encode([question])[0]
    else:
        question_embedding = vectorize(question)

    scores = []
    for index, chunk_embedding in enumerate(chunk_embeddings):
        score = cosine_similarity(question_embedding, chunk_embedding)
        scores.append((index, float(score)))

    scores.sort(key=lambda item: item[1], reverse=True)
    top_matches = scores[:top_k]

    retrieved_chunks = [chunks[index] for index, _ in top_matches]
    return retrieved_chunks, top_matches

def build_prompt(question, retrieved_chunks):
    context = "\n".join(f"- {chunk}" for chunk in retrieved_chunks)

    prompt = f"""
You are a helpful assistant.
Answer the question using only the context below.
If the context does not contain the answer, say: "I don't know based on the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""
    return prompt.strip()

def ollama_llm_answer(prompt, model_name, ollama_url):
    payload = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False,
    }

    request = Request(
        ollama_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urlopen(request, timeout=120) as response:
            response_data = json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        return f"Ollama returned HTTP {error.code}. Make sure {model_name} is installed and Ollama is running."
    except URLError:
        return f"Could not reach Ollama at {ollama_url}. Make sure Ollama is running."
    except (TimeoutError, SocketTimeout):
        return f"Timed out waiting for Ollama at {ollama_url}. Try again after the model finishes loading."
    except json.JSONDecodeError:
        return "Ollama returned an invalid JSON response."

    message = response_data.get("message", {})
    content = message.get("content")
    if not content:
        return "Ollama did not return an answer in response.message.content."

    return content.strip()

def rag_answer(question, chunking_strategy="whole", chunk_size=8, overlap=2, model_name=DEFAULT_OLLAMA_MODEL, ollama_url=DEFAULT_OLLAMA_URL):
    chunks = build_chunks(documents, chunking_strategy, chunk_size=chunk_size, overlap=overlap)
    embedding_model, chunk_embeddings = get_model_and_chunk_embeddings(chunks)
    retrieved_chunks, top_matches = retrieve_top_k(question, chunks, chunk_embeddings, embedding_model, top_k=2)
    prompt = build_prompt(question, retrieved_chunks)
    print("\n--- PROMPT TO SEND TO OLLAMA ---\n")
    print(prompt)
    print("\n--- END PROMPT ---\n")

    answer = ollama_llm_answer(prompt, model_name, ollama_url)

    print("Question:", question)
    print("Retrieved chunks:")
    for chunk in retrieved_chunks:
        print("-", chunk)

    print("\nSimilarity scores:")
    for index, score in top_matches:
        print(f"Chunk {index + 1}: {score:.3f}")

    print("\nFinal answer:")
    print(answer)


def parse_args():
    parser = argparse.ArgumentParser(description="Run the Day 25 RAG demo with Ollama.")
    parser.add_argument("--question", help="Question to ask the RAG demo.")
    parser.add_argument(
        "--chunking",
        choices=["whole", "sentences", "fixed", "sliding"],
        default="whole",
        help="Chunking strategy to use.",
    )
    parser.add_argument("--chunk-size", type=int, default=8, help="Chunk size in words for fixed or sliding chunking.")
    parser.add_argument("--overlap", type=int, default=2, help="Word overlap for sliding chunking.")
    parser.add_argument("--model", default=DEFAULT_OLLAMA_MODEL, help="Ollama model name to use.")
    parser.add_argument("--url", default=DEFAULT_OLLAMA_URL, help="Ollama chat endpoint URL.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    question = args.question or input("Ask a question: ")
    rag_answer(
        question,
        chunking_strategy=args.chunking,
        chunk_size=args.chunk_size,
        overlap=args.overlap,
        model_name=args.model,
        ollama_url=args.url,
    )