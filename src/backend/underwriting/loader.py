"""
Pro-forma loader for multifamily underwriting analysis.
"""

from typing import Dict, Any
import openpyxl


def parse_proforma(xlsx_path: str) -> Dict[str, Any]:
    """
    Parse a pro-forma Excel file and extract named ranges.
    
    Args:
        xlsx_path: Path to the Excel file containing pro-forma data
        
    Returns:
        Dictionary containing parsed pro-forma data from named ranges
        
    Raises:
        FileNotFoundError: If the Excel file doesn't exist
        ValueError: If the file is not a valid Excel file
    """
    try:
        # Load the workbook
        workbook = openpyxl.load_workbook(xlsx_path, data_only=True)
        
        # Extract named ranges
        named_ranges = {}
        for named_range in workbook.defined_names.definedName:
            try:
                # Get the range value
                range_value = workbook.defined_names[named_range.name]
                named_ranges[named_range.name] = range_value
            except Exception as e:
                # Skip ranges that can't be parsed
                continue
        
        return named_ranges
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Excel file not found: {xlsx_path}")
    except Exception as e:
        raise ValueError(f"Invalid Excel file: {e}") 