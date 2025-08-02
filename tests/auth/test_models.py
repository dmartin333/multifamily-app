"""
Tests for authentication models.
"""

import pytest
from backend.auth.models import User


def test_user_import():
    """Test that User class can be imported."""
    assert User is not None


def test_user_creation():
    """Test creating a valid User instance."""
    user_data = {
        "id": "user_123",
        "email": "test@example.com",
        "roles": ["analyst"]
    }
    
    user = User(**user_data)
    assert user.id == "user_123"
    assert user.email == "test@example.com"
    assert user.roles == ["analyst"]
    assert user.is_active is True


def test_user_with_optional_fields():
    """Test creating a User with optional fields."""
    user_data = {
        "id": "user_456",
        "email": "test2@example.com",
        "roles": ["admin", "viewer"],
        "created_at": "2024-01-15T10:30:00Z",
        "last_login": "2024-01-20T14:45:00Z"
    }
    
    user = User(**user_data)
    assert user.created_at == "2024-01-15T10:30:00Z"
    assert user.last_login == "2024-01-20T14:45:00Z" 