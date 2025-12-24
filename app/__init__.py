from flask import Flask
from .config import load_config
from .errors import register_error_handlers
from .logging_config import configure_logging
from .storage import get_store
from flask import render_template

def create_app(test_config=None):
    app = Flask(__name__, static_folder='static', template_folder='templates')
    if test_config:
        app.config.update(test_config)
    else:
        cfg = load_config()
        app.config.update(cfg)

    configure_logging(app)
    register_error_handlers(app)

    app.store = get_store(app.config)

    from .routes.health import bp as health_bp
    from .routes.sessions import bp as sessions_bp
    from .routes.chat import bp as chat_bp

    app.register_blueprint(health_bp, url_prefix="/v1")
    app.register_blueprint(sessions_bp, url_prefix="/v1")
    app.register_blueprint(chat_bp, url_prefix="/v1")

    @app.get("/")
    def index():
        return {
            "status": "ok",
            "service": "AI Chatbot API",
            "endpoints": {
                "chat": "POST /v1/chat",
                "health": "GET /v1/health",
                "sessions": "GET /v1/sessions"
            }
        }
    @app.get("/ui")
    def ui():
        return render_template("index.html")

    return app
