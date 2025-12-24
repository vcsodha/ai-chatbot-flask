import sqlite3
import os

class SQLiteStore:
    def __init__(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self._init_db()

    def _init_db(self):
        cur = self.conn.cursor()

        # Messages table
        cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            session_id TEXT,
            role TEXT,
            content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Sessions table (NEW)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            session_id TEXT PRIMARY KEY,
            title TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.conn.commit()

    # -------------------------
    # Session helpers
    # -------------------------
    def create_session_if_missing(self, session_id, title=None):
        cur = self.conn.cursor()
        cur.execute(
            "SELECT session_id FROM sessions WHERE session_id=?",
            (session_id,)
        )

        if not cur.fetchone():
            cur.execute(
                "INSERT INTO sessions (session_id, title) VALUES (?, ?)",
                (session_id, title)
            )
            self.conn.commit()

    def set_session_title(self, session_id, title):
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE sessions SET title=? WHERE session_id=?",
            (title, session_id)
        )
        self.conn.commit()

    def list_sessions(self):
        cur = self.conn.cursor()
        cur.execute("""
            SELECT session_id, title
            FROM sessions
            ORDER BY created_at DESC
        """)
        return [
            {"id": row[0], "title": row[1]}
            for row in cur.fetchall()
        ]

    # -------------------------
    # Messages
    # -------------------------
    def append_message(self, session_id, role, content):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)",
            (session_id, role, content)
        )
        self.conn.commit()

    def session_exists(self, session_id:str) -> bool:
        cur = self.conn.cursor()
        cur.execute(
            "SELECT 1 FROM sessions WHERE session_id=?",
            (session_id,)
        )
        return cur.fetchone() is not None

    def get_messages(self, session_id):
        cur = self.conn.cursor()
        cur.execute(
            """
            SELECT role, content
            FROM messages
            WHERE session_id=?
            ORDER BY created_at
            """,
            (session_id,)
        )
        return [{"role": r, "content": c} for r, c in cur.fetchall()]
    
    #delete session

    def delete_session(self, session_id):
        cur = self.conn.cursor()

        cur.execute("DELETE FROM messages WHERE session_id=?", (session_id,))
        cur.execute("DELETE FROM sessions WHERE session_id=?", (session_id,))

        self.conn.commit()

    def ensure_session(self, session_id):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT OR IGNORE INTO sessions (session_id, title) VALUES (?, ?)",
            (session_id, "New chat")
        )
        self.conn.commit()
