import os
import requests

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://host.docker.internal:11434/api/chat"
)

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are a concise assistant. "
        "Answer ONLY what the user asks. "
        "Be brief, clear, and avoid unnecessary explanations. "
        "Do not add examples unless asked."
    )
}

# -----------------------------
# Ollama (Local only)
# -----------------------------
def ollama_chat(model: str, messages: list) -> str:
    payload = {
        "model": model,
        "messages": [SYSTEM_PROMPT] + messages,
        "stream": False
    }

    res = requests.post(OLLAMA_URL, json=payload, timeout=120)
    res.raise_for_status()
    data = res.json()
    return data["message"]["content"]

# -----------------------------
# Mock (Cloud-safe demo)
# -----------------------------
def mock_chat(messages: list) -> str:
    last_user = next(
        (m["content"] for m in reversed(messages) if m["role"] == "user"),
        ""
    )
    return f"(Demo response) You asked: {last_user}"

# -----------------------------
# OpenAI (Future)
# -----------------------------
# from openai import OpenAI
# def openai_chat(model: str, messages: list) -> str:
#     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#     response = client.chat.completions.create(
#         model=model,
#         messages=[SYSTEM_PROMPT] + messages
#     )
#     return response.choices[0].message.content


def chat_completion(client, model, messages):
    if LLM_PROVIDER == "ollama":
        return ollama_chat("llama3", messages)

    if LLM_PROVIDER == "mock":
        return mock_chat(messages)

    if LLM_PROVIDER == "openai":
        return "⚠️ OpenAI disabled for now."

    return "⚠️ Invalid LLM_PROVIDER"
