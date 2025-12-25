import requests


OLLAMA_URL = "http://host.docker.internal:11434/api/chat"

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are a concise assistant. "
        "Answer ONLY what the user asks. "
        "Be brief, clear, and avoid unnecessary explanations. "
        "Do not add examples unless asked."
    )
}

def chat_completion(client, model, messages):
    payload = {
        "model": "llama3",
        "messages": [SYSTEM_PROMPT] + messages,
        "stream": False
    }

    try:
        res = requests.post(OLLAMA_URL, json=payload, timeout=120)
        res.raise_for_status()
        data = res.json()
        return data["message"]["content"]
    except Exception as e:
        return f"⚠️ Ollama error: {str(e)}"


# 🔮 Future OpenAI support
# from openai import OpenAI
# def openai_chat(...):
#     pass



