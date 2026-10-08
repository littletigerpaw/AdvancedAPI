from uuid import uuid4

from app import create_app
from config import TestingConfig


def test_health_check():
    app = create_app(TestingConfig)

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Mechanic Shop API is running"


def test_create_customer():
    app = create_app(TestingConfig)

    with app.test_client() as client:
        response = client.post(
            "/customers/",
            json={
                "name": "Smoke Test User",
                "email": f"pytest-{uuid4().hex}@example.com",
                "phone": "555-555-5555",
            },
        )

    assert response.status_code == 201
    assert response.get_json()["email"].endswith("@example.com")
