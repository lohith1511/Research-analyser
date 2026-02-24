import faiss
import numpy as np
from embeddings import create_embeddings

index = None
chunks_store = []


def index_text_chunks(text: str, chunk_size: int = 120):
    """Split text into semantic chunks and index in FAISS."""
    global index, chunks_store

    words = text.split()

    chunks_store = [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size)
        if len(words[i:i + chunk_size]) > 20
    ]

    if not chunks_store:
        print("No chunks created")
        return

    embeddings = create_embeddings(chunks_store)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    print(f"Indexed {len(chunks_store)} chunks")


def get_relevant_chunks(query: str, top_k: int = 3):
    """Retrieve relevant chunks from FAISS."""
    global index, chunks_store

    if index is None or not chunks_store:
        print("FAISS index not initialized")
        return []

    query_embedding = create_embeddings([query])

    distances, indices = index.search(query_embedding, top_k)

    print("Search indices:", indices)

    results = []

    for idx in indices[0]:
        if idx == -1:
            continue
        if 0 <= idx < len(chunks_store):
            results.append(chunks_store[idx])

    return results


def load_faiss_index():
    pass