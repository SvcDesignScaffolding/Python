import pytest
from example_pkg.core import app

def test_index():
    response = app.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}

def test_create_user():
    user = {"name": "John Doe", "age": 30}
    response = app.post("/user", json=user)
    assert response.status_code == 200
    assert response.json() == user

def test_create_user_valid_data():
    user = {"name": "John Doe", "age": 30}
    response = app.post("/user", json=user)
    assert response.status_code == 200
    assert response.json() == user

def test_create_user_missing_name():
    user = {"age": 30}
    response = app.post("/user", json=user)
    assert response.status_code == 400
    assert response.json() == {"detail": "Missing name field in request body"}

def test_create_user_missing_age():
    user = {"name": "John Doe"}
    response = app.post("/user", json=user)
    assert response.status_code == 400
    assert response.json() == {"detail": "Missing age field in request body"}
