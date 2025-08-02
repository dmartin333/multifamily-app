"""
Tests for collaboration models.
"""

import pytest
from backend.collaboration.models import Comment


def test_comment_import():
    """Test that Comment class can be imported."""
    assert Comment is not None


def test_comment_creation():
    """Test creating a valid Comment instance."""
    comment_data = {
        "id": "comment_123",
        "user_id": "user_456",
        "model_id": "model_789",
        "cell_ref": "B5",
        "content": "Test comment content"
    }
    
    comment = Comment(**comment_data)
    assert comment.id == "comment_123"
    assert comment.user_id == "user_456"
    assert comment.model_id == "model_789"
    assert comment.cell_ref == "B5"
    assert comment.content == "Test comment content" 