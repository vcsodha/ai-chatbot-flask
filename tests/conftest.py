import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    # FORCE mock LLM during tests
    app.config["LLM_PROVIDER"] = "mock"

    return app.test_client()
