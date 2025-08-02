"""
Collaboration service for managing comments and annotations.
"""

from typing import List
from .models import Comment


def add_comment(comment: Comment) -> Comment:
    """
    Add a new comment to the system.
    
    Args:
        comment: Comment object to add
        
    Returns:
        The created comment with generated ID and timestamps
        
    Raises:
        ValueError: If comment data is invalid
    """
    raise NotImplementedError


def list_comments(model_id: str) -> List[Comment]:
    """
    List all comments for a specific model.
    
    Args:
        model_id: ID of the model to get comments for
        
    Returns:
        List of comments for the specified model
        
    Raises:
        ValueError: If model_id is invalid
    """
    raise NotImplementedError 