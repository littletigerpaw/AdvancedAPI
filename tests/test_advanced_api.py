from app import create_app
from app.extensions import db
from config import TestingConfig


def setup_app():
    app = create_app(TestingConfig)
    with app.app_context():
        db.drop_all()
        db.create_all()
    return app


def test_customer_login_and_my_tickets():
    app = setup_app()

    with app.test_client() as client:
        resp = client.post(
            "/customers/",
            json={
                "name": "Token User",
                "email": "token@example.com",
                "phone": "111-222-3333",
                "password": "secret123",
            },
        )
        assert resp.status_code == 201

        login_resp = client.post(
            "/customers/login",
            json={"email": "token@example.com", "password": "secret123"},
        )
        assert login_resp.status_code == 200
        token = login_resp.get_json()["token"]
        assert token

        ticket_resp = client.post(
            "/service-tickets/",
            json={
                "customer_id": 1,
                "vin": "VIN12345",
                "issue_description": "Brake and tire service",
            },
        )
        assert ticket_resp.status_code == 201

        my_tickets = client.get(
            "/customers/my-tickets",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert my_tickets.status_code == 200
        assert len(my_tickets.get_json()) >= 1


def test_inventory_crud_flow():
    app = setup_app()

    with app.test_client() as client:
        create_resp = client.post(
            "/inventory/",
            json={"name": "Oil Filter", "price": 18.5},
        )
        assert create_resp.status_code == 201
        inventory_id = create_resp.get_json()["id"]

        get_all = client.get("/inventory/")
        assert get_all.status_code == 200
        assert any(item["id"] == inventory_id for item in get_all.get_json())

        update_resp = client.put(
            f"/inventory/{inventory_id}",
            json={"price": 22.0},
        )
        assert update_resp.status_code == 200
        assert update_resp.get_json()["price"] == 22.0

        delete_resp = client.delete(f"/inventory/{inventory_id}")
        assert delete_resp.status_code == 200
