from flask import Blueprint, jsonify, current_app
from ..errors import APIError

bp = Blueprint("sessions", __name__)

@bp.get("/sessions")
def list_sessions():
    return jsonify({
        "sessions": current_app.store.list_sessions()
    })

@bp.get("/sessions/<session_id>")
def get_session(session_id):
    messages = current_app.store.get_messages(session_id)

    if not messages:
        raise APIError(
            code="not_found",
            message=f"Session '{session_id}' not found",
            status=404
        )

    return jsonify({
        "session_id": session_id,
        "messages": messages
    })

@bp.delete("/sessions/<session_id>")
def delete_session(session_id):
    current_app.store.delete_session(session_id)
    return jsonify({"status": "deleted"})
