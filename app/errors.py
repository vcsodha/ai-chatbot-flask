from flask import jsonify, request
import uuid

class APIError(Exception):
    def __init__(self, code, message, status=400, details=None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.status = status
        self.details = details

def register_error_handlers(app):
    @app.before_request
    def attach_request_id():
        request.request_id = request.headers.get("X-Request-Id") or str(uuid.uuid4())

    @app.errorhandler(APIError)
    def handle_api_error(err):
        return jsonify({
            "error": {
                "code": err.code,
                "message": err.message,
                "details": err.details,
                "request_id": request.request_id,
            }
        }), err.status

    # 🔴 TEMPORARILY DISABLED FOR DEBUGGING
    # @app.errorhandler(Exception)
    # def handle_exception(err):
    #     return jsonify({
    #         "error": {
    #             "code": "internal_error",
    #             "message": "Unexpected server error",
    #             "request_id": getattr(request, "request_id", None)
    #         }
    #     }), 500
