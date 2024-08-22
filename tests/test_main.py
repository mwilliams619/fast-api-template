from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_read_environment():
    response = client.get("/env")
    assert response.status_code == 200
    assert "Running in" in response.json()["message"]