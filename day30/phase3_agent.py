import argparse
import math
import re
from collections import Counter

DOCUMENTS = [
    "Employees may work from home on Fridays.",
    "The office kitchen closes at 6 PM.",
    "All vacation requests must be approved by a manager.",
    "Passwords must be changed every 90 days.",
]

DOCUMENT_TOPICS = {
    "employee",
    "employees",
    "work",
    "home",
    "fridays",
    "kitchen",
    "vacation",
    "request",
    "requests",
    "manager",
    "password",
    "passwords",
    "office",
    "day",
    "days",
    "approved",
    "change",
    "changed",
}

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "be",
    "for",
    "from",
    "how",
    "i",
    "in",
    "is",
    "it",
    "of",
    "on",
    "our",
    "that",
    "the",
    "to",
    "we",
    "what",
    "when",
    "where",
    "who",
    "why",
    "with",
}

GENERAL_DIRECT_PATTERNS = [
    "hello",
    "hi",
    "your name",
    "what can you do",
    "help",
]


def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())


def normalize_token(token):
    if token.endswith("ies") and len(token) > 3:
        return token[:-3] + "y"
    if token.endswith("s") and len(token) > 3 and not token.endswith("ss"):
        return token[:-1]
    return token


def content_tokens(text):
    return [normalize_token(token) for token in tokenize(text) if token not in STOPWORDS]


def vectorize(text):
    return Counter(content_tokens(text))


def cosine_similarity(vector_a, vector_b):
    shared_terms = set(vector_a) | set(vector_b)
    dot_product = sum(vector_a.get(term, 0) * vector_b.get(term, 0) for term in shared_terms)
    magnitude_a = math.sqrt(sum(value * value for value in vector_a.values()))
    magnitude_b = math.sqrt(sum(value * value for value in vector_b.values()))
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    return dot_product / (magnitude_a * magnitude_b)


class Phase3Agent:
    def __init__(self, documents):
        self.documents = documents
        self.chunk_vectors = [vectorize(document) for document in documents]

    def route(self, question):
        question_lower = question.lower()
        if any(pattern in question_lower for pattern in GENERAL_DIRECT_PATTERNS):
            return "direct", "general question"

        question_topics = set(content_tokens(question)) & DOCUMENT_TOPICS
        if question_topics:
            return "retrieve", f"document topic match: {', '.join(sorted(question_topics))}"

        return "decline", "no document topic match"

    def retrieve(self, question, top_k=2):
        question_vector = vectorize(question)
        scores = []
        for index, chunk_vector in enumerate(self.chunk_vectors):
            score = cosine_similarity(question_vector, chunk_vector)
            scores.append((index, score))

        scores.sort(key=lambda item: item[1], reverse=True)
        top_matches = scores[:top_k]
        retrieved_chunks = [self.documents[index] for index, _ in top_matches]
        return retrieved_chunks, top_matches

    def answer_direct(self, question):
        question_lower = question.lower()
        if any(pattern in question_lower for pattern in ["hello", "hi"]):
            return "Hello. I can answer questions about the sample policy documents."
        if "what can you do" in question_lower:
            return "I can decide whether to retrieve the policy documents or answer directly, then respond grounded in the docs when possible."
        return "I do not have a direct answer for that question."

    def answer_grounded(self, question):
        retrieved_chunks, top_matches = self.retrieve(question)
        best_score = top_matches[0][1] if top_matches else 0.0

        if best_score < 0.15:
            return {
                "mode": "decline",
                "answer": "I don't know based on the provided documents.",
                "retrieved_chunks": retrieved_chunks,
                "top_matches": top_matches,
            }

        prompt_context = " | ".join(retrieved_chunks)
        answer = f"Grounded answer: {prompt_context}"
        return {
            "mode": "retrieve",
            "answer": answer,
            "retrieved_chunks": retrieved_chunks,
            "top_matches": top_matches,
        }

    def run(self, question):
        route, reason = self.route(question)
        print("Router decision:", route)
        print("Router reason:", reason)

        if route == "direct":
            answer = self.answer_direct(question)
            print("Mode: direct")
            print("Answer:", answer)
            return {
                "route": route,
                "reason": reason,
                "answer": answer,
                "retrieved_chunks": [],
                "top_matches": [],
            }

        if route == "retrieve":
            result = self.answer_grounded(question)
            print("Mode:", result["mode"])
            print("Retrieved chunks:")
            for chunk in result["retrieved_chunks"]:
                print("-", chunk)
            print("Similarity scores:")
            for index, score in result["top_matches"]:
                print(f"Chunk {index + 1}: {score:.3f}")
            print("Answer:", result["answer"])
            return {
                "route": route,
                "reason": reason,
                "answer": result["answer"],
                "retrieved_chunks": result["retrieved_chunks"],
                "top_matches": result["top_matches"],
            }

        answer = "I don't know based on the provided documents."
        print("Mode: decline")
        print("Answer:", answer)
        return {
            "route": route,
            "reason": reason,
            "answer": answer,
            "retrieved_chunks": [],
            "top_matches": [],
        }


def parse_args():
    parser = argparse.ArgumentParser(description="Day 30 phase 3 checkpoint agent demo")
    parser.add_argument("--question", help="Question to ask the agent")
    return parser.parse_args()


def main():
    args = parse_args()
    question = args.question or input("Ask a question: ")
    agent = Phase3Agent(DOCUMENTS)

    print("\nDocuments used:")
    for document in DOCUMENTS:
        print("-", document)

    print("\nQuestion:", question)
    result = agent.run(question)

    print("\nFinal output:")
    print(result["answer"])


if __name__ == "__main__":
    main()
