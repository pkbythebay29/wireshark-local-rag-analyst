# 🕵️ Wireshark Local RAG Analyst

A fully local, self-learning Retrieval-Augmented Generation (RAG) pipeline for analyzing Wireshark `.pcap` logs using local LLMs — with built-in support for Hugging Face models, learning feedback, and REST API access.

---

## 🚀 Features

- 📁 **Drop-in Folder Watcher**: Automatically processes `.pcap` logs when dropped into a folder.
- 🔍 **Protocol-Aware Preprocessing**: Extracts HTTP, DNS, TCP, and other traffic.
- 🧠 **Self-Learning Engine**: Remembers helpful answers and improves responses over time.
- 📚 **RAG Pipeline**: Uses local vector database (FAISS) with sentence-transformer embeddings.
- 🤖 **Local LLM Integration**: Supports both:
  - 🧱 Ollama-based LLMs (e.g., LLaMA, Mistral, GPT4All)
  - 🤗 Hugging Face models (e.g., Mistral-7B, Zephyr, Falcon)
- 🌐 **API Access (MCP-style)**: Query the system over HTTP from other clients.
- 💻 **Extensible CLI**: Flexible CLI and script interface for querying and development.
- 📦 **PyPI-Ready**: Fully packageable and publishable as a pip package.
- ✅ **CI/CD Support**: GitHub Actions pipelines for testing and PyPI publishing.

---

## 📂 Project Structure
 ```
. 
	├── app/                # Core logic
	├── scripts/            # CLI scripts
	├── config/             # Config files
	├── data/               # Vector DB & learned responses
	├── logs/               # Input PCAPs
	├── processed/          # Archived PCAPs
	├── .github/workflows/  # CI/CD workflows

 ```
## ⚙️ Installation

1. Clone the repo

 ```
git clone https://github.com/pkbythebay29/wireshark-local-rag-analyst.git
cd wireshark-local-rag-analyst
 ```

2. Install Dependencies
 ```
pip install -r requirements.txt
 ```
3. Configuration

Edit config/config.yaml:
 ```
protocol_filter: ["http", "dns"]
learning: true

llm_backend: "ollama"       # or "huggingface"
llm_model: "llama3"         # or "mistralai/Mistral-7B-Instruct-v0.1"

vector_db_path: "./data/faiss.index"
learned_store: "./data/learned_data.jsonl"
 ```

4. Usage
 ```
wireshark-watch
 ```
or
 ```
python scripts/run_pipeline.py
 ```

Drop .pcap files into the logs/ folder — they will be processed automatically.

#5.  Ask questions
 ```
wireshark-query
 ```
or
 ```
python scripts/query_logs.py
 ```
Example questions:
- What HTTP requests failed with 404?
- Show DNS queries to suspicious domains.
- Were there any TCP handshakes that failed?


6. Use as a REST API (MCP server)

 ```
python -m app.mcp_server
 ```
 ```
curl -X POST http://localhost:8080/query \
     -H "Content-Type: application/json" \
     -d '{"query": "Show me failed DNS requests"}'
 ```

7. 🤗 Hugging Face Model Support

You can fork, fine-tune, or use any Hugging Face model by editing config.yaml

8. Acknowledgements

🙏 Acknowledgements


This project stands on the shoulders of open-source giants:
 ```
    Wireshark/tshark – For deep packet inspection

    FAISS – Vector search from Meta

    Sentence Transformers – Fast embeddings from Hugging Face

    Ollama – Local model hosting made easy

    Transformers – Hugging Face's interface to modern LLMs

    Watchdog, FastAPI, Uvicorn, and many more

Thank you to all the contributors making open-source incredible.
 ```
9. 🗺️ Roadmap

See ROADMAP.md for planned features and timeline.

#8. License
📜 License
MIT 
