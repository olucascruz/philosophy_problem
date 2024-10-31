import pytest
from fastapi.testclient import TestClient
from philosophy_problem.api.main import app

client = TestClient(app)

def test_ping():
    response = client.get("/eat")
    print(response.content)
    assert response.status_code == 200
    # assert response.json() == {"message": "pong"}
