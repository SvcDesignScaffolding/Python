# tests/functional/test_main.py
import pytest
from uvicorn import run

from example_pkg.core import app


def test_main():
    run(app, host="0.0.0.0", port=80, debug=True)
