"""
Tests for assumption engine.
"""

import json
import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch
from backend.underwriting.assumptions.service import load_assumptions, list_assumption_sets
from backend.underwriting.assumptions.models import Assumption


class TestAssumptionService:
    """Test cases for assumption service functions."""
    
    @pytest.fixture
    def temp_assumptions_dir(self):
        """Create a temporary directory with test assumption files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            assumptions_dir = Path(temp_dir) / "assumptions"
            assumptions_dir.mkdir()
            
            # Create test assumption files
            test_conservative = {
                "name": "Test Conservative",
                "description": "Test conservative assumptions",
                "assumptions": {
                    "expense_ratio": 0.45,
                    "vacancy_rate": 0.05
                }
            }
            
            test_aggressive = {
                "name": "Test Aggressive", 
                "description": "Test aggressive assumptions",
                "assumptions": {
                    "expense_ratio": 0.35,
                    "vacancy_rate": 0.03
                }
            }
            
            with open(assumptions_dir / "conservative.json", 'w') as f:
                json.dump(test_conservative, f)
            
            with open(assumptions_dir / "aggressive.json", 'w') as f:
                json.dump(test_aggressive, f)
            
            yield assumptions_dir
    
    def test_load_assumptions_success(self, temp_assumptions_dir):
        """Test that load_assumptions successfully loads assumption data."""
        with patch('src.backend.underwriting.assumptions.service.Path') as mock_path:
            # Mock the path to point to our temp directory
            mock_path.return_value.parent.parent.parent.parent.parent = temp_assumptions_dir.parent
            
            result = load_assumptions("conservative")
            
            assert result["name"] == "Test Conservative"
            assert result["assumptions"]["expense_ratio"] == 0.45
            assert result["assumptions"]["vacancy_rate"] == 0.05
    
    def test_load_assumptions_not_found(self, temp_assumptions_dir):
        """Test that load_assumptions raises ValueError for non-existent assumption set."""
        with patch('src.backend.underwriting.assumptions.service.Path') as mock_path:
            mock_path.return_value.parent.parent.parent.parent.parent = temp_assumptions_dir.parent
            
            with pytest.raises(ValueError, match="Assumption set 'nonexistent' not found"):
                load_assumptions("nonexistent")
    
    def test_load_assumptions_invalid_json(self, temp_assumptions_dir):
        """Test that load_assumptions handles invalid JSON gracefully."""
        # Create a file with invalid JSON
        invalid_file = temp_assumptions_dir / "invalid.json"
        with open(invalid_file, 'w') as f:
            f.write("{ invalid json content")
        
        with patch('src.backend.underwriting.assumptions.service.Path') as mock_path:
            mock_path.return_value.parent.parent.parent.parent.parent = temp_assumptions_dir.parent
            
            with pytest.raises(ValueError, match="Invalid JSON in assumption set 'invalid'"):
                load_assumptions("invalid")
    
    def test_list_assumption_sets_success(self, temp_assumptions_dir):
        """Test that list_assumption_sets returns all available assumption sets."""
        with patch('src.backend.underwriting.assumptions.service.Path') as mock_path:
            mock_path.return_value.parent.parent.parent.parent.parent = temp_assumptions_dir.parent
            
            result = list_assumption_sets()
            
            # Should return sorted list of assumption set names without .json extension
            assert result == ["aggressive", "conservative"]
    
    def test_list_assumption_sets_empty_directory(self):
        """Test that list_assumption_sets returns empty list when directory doesn't exist."""
        with patch('src.backend.underwriting.assumptions.service.Path') as mock_path:
            # Mock path to non-existent directory
            mock_path.return_value.parent.parent.parent.parent.parent = Path("/nonexistent")
            
            result = list_assumption_sets()
            assert result == []
    
    def test_list_assumption_sets_no_json_files(self, temp_assumptions_dir):
        """Test that list_assumption_sets returns empty list when no JSON files exist."""
        # Remove all JSON files
        for json_file in temp_assumptions_dir.glob("*.json"):
            json_file.unlink()
        
        with patch('src.backend.underwriting.assumptions.service.Path') as mock_path:
            mock_path.return_value.parent.parent.parent.parent.parent = temp_assumptions_dir.parent
            
            result = list_assumption_sets()
            assert result == []


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