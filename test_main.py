from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Devies"}


def test_create_and_get_user():
    # Create two users
    response1 = client.put("/user", json={"username": "user1", "email":"user1@example.com"})
    response2 = client.put("/user", json={"username": "user2", "email":"user2@example.com"})
    assert response1.status_code == response2.status_code == 200

    # Try to get one of the users
    response3 = client.get("/user", params={"username": "user1"})
    assert response3.status_code == 200
    assert response3.json() ==  {'email': 'user1@example.com', 'username': 'user1'}


def test_delete():
    assert True

