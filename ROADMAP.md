# 🗺️ Roadmap — Wireshark Local RAG Analyst

This file outlines planned features and improvements for the project. Contributions and suggestions are welcome!

---

## ✅ Current Features

- Watcher for `.pcap` drop folder
- Protocol-specific log extraction
- Vector DB (FAISS) + embeddings
- Self-learning from user feedback
- Local LLM querying (via Ollama or Hugging Face)

---

## 🚧 Planned Features

### 1. 🧠 Multi-Model Selection (CLI or Config)
- Allow user to choose from multiple LLMs at runtime
- Option to define different models for:
  - General questions
  - Threat analysis
  - Low-resource fallback

**Planned Implementation:**
- CLI flag: `--model mistral-custom`
- Automatic detection from `models/` or Hugging Face model list

---

### 2. 🌐 Web UI (Streamlit)
- Streamlit dashboard for:
  - Uploading `.pcap` files
  - Viewing parsed log summaries
  - Chat-based interface to ask questions
  - Annotating answers as helpful/unhelpful

**Planned Pages:**
- `Upload`
- `Live Traffic Monitor`
- `Ask Questions`
- `Learning History`

---

### 3. 🛡️ Suspicious Pattern Auto-Detection
- Built-in rule engine to flag:
  - Port scanning
  - DNS tunneling
  - MAC spoofing
  - Protocol misuse
- Use Suricata/YARA-style logic + NLP summaries

**Planned Approaches:**
- Pattern matching via custom rules
- Use a lightweight threat intelligence DB
- Anomaly score overlay on packet summaries


### 4. 🔌 MCP-Compatible API Server (DONE)
- FastAPI server to:
  - Accept JSON log queries from any client
  - Return structured answers (LLM or learned)
  - Enable client/server decoupling

✅ Released in `app/mcp_server.py`

---

### 5. 🤗 Hugging Face Fork & Direct Model Support
- Seamlessly use any model from Hugging Face (e.g. `mistralai/Mistral-7B-Instruct-v0.1`)
- Support for:
  - Forking models on Hugging Face
  - Using LoRA/adapters or quantized variants
  - Inference via `transformers` and `accelerate`
- Selectable backend: `huggingface` or `ollama` in `config.yaml`

🗓️ ETA: **2025-07-22**

---

### 6. 📉 GPU Memory Auto-Scaling (Future)
- Detect available VRAM
- Auto-select appropriate model precision (fp16, int8, etc.)
- Prevent memory crashes during Hugging Face model load

🗓️ ETA: **2025-08-01**

---
---

## 📅 Timeline (Updated for July 2025)

## 📅 Combined Timeline

| Milestone                    | Target Date   | Status |
|-----------------------------|---------------|--------|
| MVP (CLI + Learning)        | ✅ Done        | ✅     |
| MCP Server (FastAPI)        | ✅ Done        | ✅     |
| Multi-Model Support         | 2025-07-05     | ⏳     |
| Streamlit UI                | 2025-07-15     | ⏳     |
| Threat Detection Engine     | 2025-07-29     | ⏳     |
| Hugging Face Forking + API  | 2025-07-22     | ⏳     |
| GPU-aware Model Loader      | 2025-08-01     | ⏳     |
---

## 📬 Contributing

If you'd like to help with any roadmap item, open an issue or PR with `[ROADMAP]` in the title. Suggestions welcome!
