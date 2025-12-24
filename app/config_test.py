def load_test_config(tmp_path):
    return {
        "TESTING": True,
        "DEBUG": False,
        "PORT": 8000,
        "STORAGE_BACKEND": "sqlite",
        "SQLITE_PATH": str(tmp_path / "test_chat.db"),
        "MAX_TURNS": 30,
        "MAX_INPUT_CHARS": 8000,
        "OPENAI_API_KEY": "test-key",
        "OPENAI_MODEL": "mock",
    }
