from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd

sentences = [
    "The cat is sleeping on the sofa.",
    "A kitten is resting on the couch.",
    "The dog is playing in the garden.",
    "Python is a popular programming language.",
    "I like writing code in Python.",
]

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(sentences)

def cosine_similarity(vector_a, vector_b):
    return np.dot(vector_a, vector_b) / (
        np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    )

matrix = []
for embedding_a in embeddings:
    row = []
    for embedding_b in embeddings:
        score = cosine_similarity(embedding_a, embedding_b)
        row.append(round(float(score), 3))
    matrix.append(row)

df = pd.DataFrame(
    matrix,
    index=[f"S{i+1}" for i in range(len(sentences))],
    columns=[f"S{i+1}" for i in range(len(sentences))]
)

print("Sentences:")
for index, sentence in enumerate(sentences, start=1):
    print(f"S{index}: {sentence}")

print("\nCosine Similarity Matrix:")
print(df)