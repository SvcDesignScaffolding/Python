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
