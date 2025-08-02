"""
Tests for assumption engine.
"""

import pytest
from src.backend.underwriting.assumptions.service import load_assumptions, list_assumption_sets
from src.backend.underwriting.assumptions.models import Assumption


class TestAssumptionService:
    """Test cases for assumption service functions."""
    
    def test_load_assumptions_stub(self):
        """Test that load_assumptions returns None (stub implementation)."""
        result = load_assumptions("test_assumption_set")
        assert result is None
    
    def test_list_assumption_sets_stub(self):
        """Test that list_assumption_sets returns None (stub implementation)."""
        result = list_assumption_sets()
        assert result is None


class TestAssumptionModel:
    """Test cases for Assumption Pydantic model."""
    
    def test_assumption_creation(self):
        """Test creating a valid Assumption instance."""
        assumption_data = {
            "name": "Test Assumption",
            "value": 0.05,
            "category": "expense",
            "description": "Test assumption for unit testing"
        }
        
        assumption = Assumption(**assumption_data)
        assert assumption.name == "Test Assumption"
        assert assumption.value == 0.05
        assert assumption.category == "expense"
        assert assumption.description == "Test assumption for unit testing"
    
    def test_assumption_validation(self):
        """Test that invalid assumption data raises validation error."""
        invalid_data = {
            "name": "Test Assumption",
            # Missing required 'value' field
            "category": "expense"
        }
        
        with pytest.raises(ValueError):
            Assumption(**invalid_data) 