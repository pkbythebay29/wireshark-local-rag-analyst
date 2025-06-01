import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from app.config import load_config

config = load_config()
model = SentenceTransformer(config["embedding_model"])

def embed_texts(texts):
    vectors = model.encode(texts)
    store_vectors(vectors, texts)

def store_vectors(vectors, texts):
    dim = vectors.shape[1]
    index_path = config["vector_db_path"]
    if os.path.exists(index_path):
        index = faiss.read_index(index_path)
    else:
        index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors))
    faiss.write_index(index, index_path)
    print(f"[✓] Stored {len(vectors)} vectors")
