import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_heartbeat(client):
    response = client.get("/heartbeat")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
