"""
Pydantic models for underwriting assumptions.
"""

from typing import Optional, Dict, Any
from pydantic import BaseModel, Field


class Assumption(BaseModel):
    """
    Pydantic model for underwriting assumptions.
    """
    
    name: str = Field(..., description="Name of the assumption")
    value: float = Field(..., description="Numeric value of the assumption")
    unit: Optional[str] = Field(None, description="Unit of measurement")
    category: str = Field(..., description="Category of the assumption (e.g., 'expense', 'revenue', 'financing')")
    description: Optional[str] = Field(None, description="Description of the assumption")
    source: Optional[str] = Field(None, description="Source of the assumption")
    confidence_level: Optional[float] = Field(None, ge=0.0, le=1.0, description="Confidence level (0-1)")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")
    
    class Config:
        """Pydantic configuration."""
        json_schema_extra = {
            "example": {
                "name": "Property Tax Rate",
                "value": 0.025,
                "unit": "percentage",
                "category": "expense",
                "description": "Annual property tax rate as percentage of assessed value",
                "source": "County Assessor",
                "confidence_level": 0.9,
                "metadata": {
                    "last_updated": "2024-01-15",
                    "data_source": "official_records"
                }
            }
        } 