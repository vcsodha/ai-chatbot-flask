from flask import Blueprint, jsonify, request, current_app
from ..errors import APIError
from ..openai_client import chat_completion
import uuid

bp = Blueprint("chat", __name__)

@bp.post("/chat")
def send_message():
    # 1️⃣ Validate request
    data = request.get_json(silent=True)
    if not data or "message" not in data:
        raise APIError(
            code="invalid_request",
            message="Request body must include 'message'.",
            status=400
        )

    # 2️⃣ Get or create session_id
    session_id = data.get("session_id") or str(uuid.uuid4())

    # 3️⃣ Ensure session exists in DB
    current_app.store.create_session_if_missing(session_id)

    # 4️⃣ Auto-title ONLY if first user message
    existing_messages = current_app.store.get_messages(session_id)
    if not existing_messages:
        title = data["message"][:40]
        current_app.store.set_session_title(session_id, title)

    # 5️⃣ Store user message
    current_app.store.append_message(
        session_id,
        "user",
        data["message"]
    )

    # 6️⃣ Fetch full conversation
    messages = current_app.store.get_messages(session_id)

    # 7️⃣ Call Ollama (OpenAI intentionally NOT used)
    assistant_text = chat_completion(
        client=None,          # 🔒 Ollama only
        model="llama3",
        messages=messages
    )

    # 8️⃣ Store assistant reply
    current_app.store.append_message(
        session_id,
        "assistant",
        assistant_text
    )

    # 9️⃣ Return response
    return jsonify({
        "session_id": session_id,
        "assistant_message": assistant_text
    })
