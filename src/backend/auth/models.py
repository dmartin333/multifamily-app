"""
Authentication models.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    """
    User model for authentication and authorization.
    """
    
    id: str = Field(..., description="Unique user identifier")
    email: str = Field(..., description="User email address")
    roles: List[str] = Field(default_factory=list, description="User roles/permissions")
    is_active: bool = Field(default=True, description="Whether user account is active")
    created_at: Optional[str] = Field(None, description="Account creation timestamp")
    last_login: Optional[str] = Field(None, description="Last login timestamp")
    
    class Config:
        """Pydantic configuration."""
        json_schema_extra = {
            "example": {
                "id": "user_123",
                "email": "user@example.com",
                "roles": ["analyst", "viewer"],
                "is_active": True,
                "created_at": "2024-01-15T10:30:00Z",
                "last_login": "2024-01-20T14:45:00Z"
            }
        } 