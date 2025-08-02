"""
Tests for collaboration service.
"""

import pytest
from backend.collaboration.service import add_comment, list_comments


def test_add_comment_import():
    """Test that add_comment function can be imported."""
    assert add_comment is not None


def test_list_comments_import():
    """Test that list_comments function can be imported."""
    assert list_comments is not None


def test_add_comment_not_implemented():
    """Test that add_comment raises NotImplementedError."""
    from backend.collaboration.models import Comment
    
    comment = Comment(
        id="test_id",
        user_id="test_user",
        model_id="test_model",
        cell_ref="A1",
        content="Test content"
    )
    
    with pytest.raises(NotImplementedError):
        add_comment(comment)


def test_list_comments_not_implemented():
    """Test that list_comments raises NotImplementedError."""
    with pytest.raises(NotImplementedError):
        list_comments("test_model_id") 