import os
import requests

# -----------------------------
# Configuration
# -----------------------------
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
# Ollama (Local / Private LLM)
# -----------------------------
def ollama_chat(model: str, messages: list[str]) -> str:
    payload = {
        "model": model,
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


# -----------------------------
# OpenAI (Future / Optional)
# -----------------------------
# Uncomment ONLY when you want to enable OpenAI
#
# from openai import OpenAI
#
# def openai_chat(model: str, messages: list[str]) -> str:
#     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#     response = client.chat.completions.create(
#         model=model,
#         messages=[SYSTEM_PROMPT] + messages
#     )
#     return response.choices[0].message.content


# -----------------------------
# Unified entry point
# -----------------------------
def chat_completion(client, model, messages):
    """
    Single interface used by the app.
    Switches LLM backend via LLM_PROVIDER env variable.
    """

    if LLM_PROVIDER == "openai":
        # return openai_chat(model, messages)
        return "⚠️ OpenAI provider is disabled."

    # Default → Ollama
    return ollama_chat("llama3", messages)
