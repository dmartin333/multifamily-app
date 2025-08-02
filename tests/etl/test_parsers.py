"""
Tests for ETL parsers module.
"""

import pytest
from src.backend.etl.parsers import parse_csv, parse_xlsx, parse_pdf


class TestParsers:
    """Test cases for ETL parser functions."""
    
    def test_parse_csv_not_implemented(self):
        """Test that parse_csv raises NotImplementedError."""
        with pytest.raises(NotImplementedError) as exc_info:
            parse_csv("test.csv")
        assert "CSV parsing not yet implemented" in str(exc_info.value)
    
    def test_parse_xlsx_not_implemented(self):
        """Test that parse_xlsx raises NotImplementedError."""
        with pytest.raises(NotImplementedError) as exc_info:
            parse_xlsx("test.xlsx")
        assert "XLSX parsing not yet implemented" in str(exc_info.value)
    
    def test_parse_pdf_not_implemented(self):
        """Test that parse_pdf raises NotImplementedError."""
        with pytest.raises(NotImplementedError) as exc_info:
            parse_pdf("test.pdf")
        assert "PDF parsing not yet implemented" in str(exc_info.value) 