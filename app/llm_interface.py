from app.config import load_config

config = load_config()

# Dynamic backend switch
if config.get("llm_backend") == "huggingface":
    from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
    import torch

    tokenizer = AutoTokenizer.from_pretrained(config["llm_model"])
    model = AutoModelForCausalLM.from_pretrained(
        config["llm_model"],
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto"
    )
    llm = pipeline("text-generation", model=model, tokenizer=tokenizer)

    def ask_llm(prompt):
        response = llm(prompt, max_new_tokens=300, do_sample=True, temperature=0.7)
        return response[0]["generated_text"]

else:
    import ollama
    def ask_llm(prompt):
        response = ollama.chat(model=config["llm_model"], messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
