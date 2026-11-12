from fastapi.testclient import TestClient
from langchain_core.messages import AIMessage

from backend.app.main import app


client = TestClient(app)


class FakeAgent:
    """A fake Agent that does not call Gemini."""

    def invoke(self, input_data, config=None):
        return {
            "messages": [
                AIMessage(
                    content="Mock Agent Response"
                )
            ]
        }


def test_chat_success(monkeypatch):
    monkeypatch.setattr(
        "backend.app.api.chat.create_research_agent",
        lambda: FakeAgent()
    )

    response = client.post(
        "/api/v1/chat",
        json={
            "message": "Hello VoyageAI!"
        }
    )

    assert response.status_code == 200

    assert response.json() == {
        "reply": "Mock Agent Response"
    }


def test_chat_empty_message():
    response = client.post(
        "/api/v1/chat",
        json={
            "message": ""
        }
    )

    assert response.status_code == 422


def test_chat_missing_message():
    response = client.post(
        "/api/v1/chat",
        json={}
    )

    assert response.status_code == 422
