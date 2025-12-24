def test_chat_endpoint(client):
    res = client.post(
        "/v1/chat",
        json={"session_id": "test-session", "message": "Hello"}
    )

    assert res.status_code == 200

    data = res.get_json()
    assert "assistant_message" in data
    assert data["session_id"] == "test-session"
