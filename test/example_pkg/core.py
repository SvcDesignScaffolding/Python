import pytest
from example_pkg import core

def test_index():
    response = core.app.get("/", params={"name": "John Doe"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John Doe!"}

def test_index_without_name():
    response = core.app.get("/")
    assert response.status_code == 400
    assert response.json()["detail"] == "name 参数不能为空"
