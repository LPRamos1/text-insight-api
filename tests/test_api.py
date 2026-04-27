from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_analysis():
    response = client.post(
        "/analysis/",
        json={"title": "Test", "content": "This is a test content for API testing"},
    )

    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["word_count"] > 0


def test_get_all():
    response = client.get("/analysis/")
    assert response.status_code == 200
