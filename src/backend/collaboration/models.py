"""
Collaboration models for comments and annotations.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Comment(BaseModel):
    """
    Comment model for collaboration features.
    """
    
    id: str = Field(..., description="Unique comment identifier")
    user_id: str = Field(..., description="ID of the user who created the comment")
    model_id: str = Field(..., description="ID of the model/project this comment belongs to")
    cell_ref: str = Field(..., description="Cell reference (e.g., 'A1', 'B5') where comment is attached")
    content: str = Field(..., description="Comment content/text")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Comment creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Comment last update timestamp")
    parent_id: Optional[str] = Field(None, description="Parent comment ID for threaded comments")
    
    class Config:
        """Pydantic configuration."""
        json_schema_extra = {
            "example": {
                "id": "comment_123",
                "user_id": "user_456",
                "model_id": "model_789",
                "cell_ref": "B5",
                "content": "This assumption seems high for this market.",
                "created_at": "2024-01-15T10:30:00Z",
                "updated_at": "2024-01-15T14:45:00Z",
                "parent_id": None
            }
        } 