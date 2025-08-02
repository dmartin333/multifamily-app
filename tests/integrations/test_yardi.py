"""
Tests for Yardi integration.
"""

import pytest
from src.backend.integrations.yardi import fetch_yardi


def test_yardi_import():
    """Test that Yardi module can be imported."""
    assert fetch_yardi is not None 