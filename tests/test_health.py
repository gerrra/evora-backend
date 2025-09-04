from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

HTTP_OK = 200


def test_health_check():
    response = client.get("/health")
    assert response.status_code == HTTP_OK  # noqa: S101
    assert response.json() == {"status": "ok"}  # noqa: S101
