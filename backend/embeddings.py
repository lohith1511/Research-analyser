from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding_model():
    return model

def create_embeddings(texts: list[str]):
    return model.encode(texts)
