
from app import hello
import pytest

def test_hello():
    assert hello() == 'Hello, World!'
