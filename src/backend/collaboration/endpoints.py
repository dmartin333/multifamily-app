"""
FastAPI endpoints for collaboration features.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import List, Dict, Any
from .models import Comment
from .service import add_comment, list_comments

router = APIRouter(prefix="/comments", tags=["collaboration"])


@router.post("/", response_model=Comment)
async def create_comment(comment_data: Dict[str, Any]) -> Comment:
    """
    Create a new comment.
    
    Args:
        comment_data: Comment data from request body
        
    Returns:
        Created comment object
        
    Raises:
        HTTPException: If comment creation fails
    """
    try:
        # TODO: Implement comment creation logic
        comment = Comment(**comment_data)
        return add_comment(comment)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[Comment])
async def get_comments(model_id: str = Query(..., description="Model ID to get comments for")) -> List[Comment]:
    """
    Get all comments for a specific model.
    
    Args:
        model_id: Model ID from query parameter
        
    Returns:
        List of comments for the specified model
        
    Raises:
        HTTPException: If comment retrieval fails
    """
    try:
        # TODO: Implement comment retrieval logic
        return list_comments(model_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 