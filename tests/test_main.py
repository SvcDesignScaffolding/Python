# tests/functional/test_main.py
import pytest

from example_pkg.core import app


def test_main():
    app.run(debug=True)
