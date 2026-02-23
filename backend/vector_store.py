import faiss
from embeddings import create_embeddings
import numpy as np

index = None
chunks_store = []

def index_text_chunks(text: str, chunk_size: int = 500):
    """Splits text into chunks and indexes them in FAISS."""
    global index, chunks_store
    
    chunks_store = []
    
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        if chunk.strip():
            chunks_store.append(chunk)
            
    if not chunks_store:
        return
        
    embeddings = create_embeddings(chunks_store)
    dimension = embeddings.shape[1]
    
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))

def get_relevant_chunks(query: str, top_k: int = 3):
    """Retrieves standard chunks relevant to the query from FAISS."""
    global index, chunks_store
    
    if index is None or not chunks_store:
        return []
        
    query_embedding = create_embeddings([query])
    distances, indices = index.search(np.array(query_embedding).astype("float32"), top_k)
    
    results = []
    for idx in indices[0]:
        if 0 <= idx < len(chunks_store):
            results.append(chunks_store[idx])
    return results

def load_faiss_index():
    pass
