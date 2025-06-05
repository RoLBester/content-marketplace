import pytest
from app import app

def test_homepage():
    with app.test_client() as client:
        response = client.get('/')
        assert response.get_data(as_text=True) == "Welcome to the Decentralized Content Marketplace!"
