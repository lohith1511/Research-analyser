from sentence_transformers import SentenceTransformer

model = None

def get_embedding_model():
    global model
    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model

def create_embeddings(texts):
    model = get_embedding_model()

    # ensure list input
    if isinstance(texts, str):
        texts = [texts]

    embeddings = model.encode(texts)

    # ensure 2D numpy array
    import numpy as np
    return np.array(embeddings).astype("float32")