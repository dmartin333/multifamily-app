"""
Tests for the pro-forma loader module.
"""

import pytest
import tempfile
import os
from unittest.mock import Mock, patch
from backend.underwriting.loader import parse_proforma


class TestParseProforma:
    """Test cases for parse_proforma function."""
    
    def test_parse_proforma_file_not_found(self):
        """Test that FileNotFoundError is raised for non-existent file."""
        with pytest.raises(FileNotFoundError):
            parse_proforma("nonexistent_file.xlsx")
    
    def test_parse_proforma_invalid_file(self):
        """Test that ValueError is raised for invalid Excel file."""
        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp_file:
            tmp_file.write(b"not an excel file")
            tmp_file_path = tmp_file.name
        
        try:
            with pytest.raises(ValueError):
                parse_proforma(tmp_file_path)
        finally:
            os.unlink(tmp_file_path)
    
    @patch('openpyxl.load_workbook')
    def test_parse_proforma_success(self, mock_load_workbook):
        """Test successful parsing of pro-forma file."""
        # Mock workbook and named ranges
        mock_workbook = Mock()
        mock_defined_names = Mock()
        mock_defined_names.definedName = [
            Mock(name="Revenue"),
            Mock(name="Expenses"),
            Mock(name="NOI")
        ]
        
        # Mock the range values
        mock_defined_names.__getitem__.side_effect = lambda x: f"value_{x}"
        mock_workbook.defined_names = mock_defined_names
        mock_load_workbook.return_value = mock_workbook
        
        # Test the function
        result = parse_proforma("test_file.xlsx")
        
        # Verify the result
        expected = {
            "Revenue": "value_Revenue",
            "Expenses": "value_Expenses", 
            "NOI": "value_NOI"
        }
        assert result == expected
        mock_load_workbook.assert_called_once_with("test_file.xlsx", data_only=True) 