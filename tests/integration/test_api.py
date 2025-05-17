"""
Integration tests for the FastAPI application.
"""

import pytest
from fastapi.testclient import TestClient
from src.api.app import app

# Create a test client
client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Welcome to the Python Project Template API" in data["message"]
    assert "version" in data


def test_greeting_endpoint():
    """Test the greeting endpoint."""
    # Test with default name
    response = client.post("/greeting", json={})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, World!"
    
    # Test with custom name
    response = client.post("/greeting", json={"name": "FastAPI"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, FastAPI!"


def test_config_endpoint():
    """Test the config endpoint."""
    response = client.get("/config")
    assert response.status_code == 200
    data = response.json()
    assert "config" in data
    assert "app" in data["config"]
    assert "name" in data["config"]["app"] 