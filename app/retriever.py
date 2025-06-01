import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from app.config import load_config

config = load_config()
model = SentenceTransformer(config["embedding_model"])
index = faiss.read_index(config["vector_db_path"])

def retrieve_context(query, top_k=5):
    q_vec = model.encode([query])
    D, I = index.search(np.array(q_vec), top_k)
    return I[0]  # Indices of top-k vectors (dummy texts in this version)
