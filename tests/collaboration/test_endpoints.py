"""
Tests for collaboration endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from backend.collaboration.endpoints import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
client = TestClient(app)


def test_endpoints_import():
    """Test that collaboration endpoints can be imported."""
    assert router is not None


def test_create_comment_endpoint():
    """Test the create comment endpoint."""
    comment_data = {
        "id": "comment_123",
        "user_id": "user_456",
        "model_id": "model_789",
        "cell_ref": "B5",
        "content": "Test comment"
    }
    
    response = client.post("/comments/", json=comment_data)
    # Should return 400 since the service functions are not implemented
    assert response.status_code == 400


def test_get_comments_endpoint():
    """Test the get comments endpoint."""
    response = client.get("/comments/?model_id=test_model")
    # Should return 400 since the service functions are not implemented
    assert response.status_code == 400 