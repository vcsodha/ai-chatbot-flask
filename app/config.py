import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    return {
        "LLM_PROVIDER": os.getenv("LLM_PROVIDER", "mock"),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "OPENAI_MODEL": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        "PORT": int(os.getenv("PORT", "8000")),
        "DEBUG": os.getenv("FLASK_ENV", "development") == "development",
        "STORAGE_BACKEND": os.getenv("STORAGE_BACKEND", "memory"),
        "SQLITE_PATH": os.getenv("SQLITE_PATH", "./data/chat.db"),
        "MAX_TURNS": int(os.getenv("MAX_TURNS", "30")),
        "MAX_INPUT_CHARS": int(os.getenv("MAX_INPUT_CHARS", "8000")),
    }
