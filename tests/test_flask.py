# test_flask.py
from app import app
import pytest

@pytest.fixture
def client():
    """Test client for the Flask app."""
    return app.test_client()

def test_hello(client):
    """Test if the app responds with 'Hello, World!'."""
    response = client.get('/')
    assert response.data == b'Hello, World!'
