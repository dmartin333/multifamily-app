"""
Tests for reporting exporter functions.
"""

import pytest
from src.backend.reporting.exporter import to_xlsx, to_pdf, to_pptx


class TestExporter:
    """Test cases for exporter functions."""
    
    def test_to_xlsx_returns_bytes(self):
        """Test that to_xlsx returns bytes."""
        test_data = {
            "summary": {
                "Property Name": "Test Property",
                "IRR": "12.5%",
                "NPV": "$1,000,000"
            },
            "financial_metrics": {
                "Cap Rate": "6.5%",
                "Cash on Cash": "8.2%"
            }
        }
        result = to_xlsx(test_data)
        assert isinstance(result, bytes)
        assert len(result) > 0
    
    def test_to_xlsx_with_list_data(self):
        """Test that to_xlsx handles list data correctly."""
        test_data = {
            "summary": [
                {"Year": 1, "Revenue": 1000000, "Expenses": 600000},
                {"Year": 2, "Revenue": 1050000, "Expenses": 620000}
            ]
        }
        result = to_xlsx(test_data)
        assert isinstance(result, bytes)
        assert len(result) > 0
    
    def test_to_xlsx_empty_data(self):
        """Test that to_xlsx handles empty data."""
        empty_data = {}
        result = to_xlsx(empty_data)
        assert isinstance(result, bytes)
        assert len(result) > 0
    
    def test_to_pdf_not_implemented(self):
        """Test that to_pdf raises NotImplementedError."""
        test_data = {
            "property_name": "Test Property",
            "irr": 0.12,
            "npv": 1000000
        }
        with pytest.raises(NotImplementedError):
            to_pdf(test_data)
    
    def test_to_pptx_not_implemented(self):
        """Test that to_pptx raises NotImplementedError."""
        test_data = {
            "property_name": "Test Property",
            "irr": 0.12,
            "npv": 1000000
        }
        with pytest.raises(NotImplementedError):
            to_pptx(test_data)
    
    def test_exporter_with_complex_data(self):
        """Test exporter functions with complex data structure."""
        complex_data = {
            "property_info": {
                "name": "Sunset Apartments",
                "address": "123 Main St",
                "units": 150
            },
            "summary": {
                "Purchase Price": "$15,000,000",
                "IRR": "14.5%",
                "NPV": "$2,500,000"
            },
            "financial_metrics": {
                "irr": 0.145,
                "npv": 2500000,
                "cap_rate": 0.065
            },
            "cash_flow": [
                {"year": 1, "revenue": 1800000, "expenses": 1200000, "noi": 600000},
                {"year": 2, "revenue": 1850000, "expenses": 1220000, "noi": 630000}
            ]
        }
        
        # Test XLSX export
        xlsx_result = to_xlsx(complex_data)
        assert isinstance(xlsx_result, bytes)
        assert len(xlsx_result) > 0
        
        # Test PDF export (should raise NotImplementedError)
        with pytest.raises(NotImplementedError):
            to_pdf(complex_data)
        
        # Test PPTX export (should raise NotImplementedError)
        with pytest.raises(NotImplementedError):
            to_pptx(complex_data) 