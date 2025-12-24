from .memory import MemoryStore
from .sqlite import SQLiteStore

def get_store(config):
    backend = config.get("STORAGE_BACKEND", "memory")

    if backend == "sqlite":
        return SQLiteStore(config["SQLITE_PATH"])

    return MemoryStore()
