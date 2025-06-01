import json
import os
from app.retriever import retrieve_context
from app.llm_interface import ask_llm
from app.config import load_config

config = load_config()
learned_path = config["learned_store"]

def load_learned():
    if not os.path.exists(learned_path):
        return []
    with open(learned_path, "r") as f:
        return [json.loads(line) for line in f]

def save_learned(query, answer):
    with open(learned_path, "a") as f:
        f.write(json.dumps({"query": query, "answer": answer}) + "\n")

def ask_and_learn():
    while True:
        query = input("🧠 Your Question: ").strip()
        known = load_learned()
        for entry in known:
            if query.lower() in entry["query"].lower():
                print("💡 Using previous response:")
                print(entry["answer"])
                return

        ctx_ids = retrieve_context(query)
        ctx = "\n".join([f"Context entry {i}" for i in ctx_ids])  # Replace with actual text retrieval
        full_prompt = f"{ctx}\n\n{query}"
        answer = ask_llm(full_prompt)
        print(answer)

        if config.get("learning", True):
            fb = input("👍 Was this helpful? (Y/N): ").strip().lower()
            if fb == "y":
                save_learned(query, answer)
                print("✅ Learned.")
