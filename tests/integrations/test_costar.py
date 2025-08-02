"""
Tests for CoStar integration.
"""

import pytest
from src.backend.integrations.costar import fetch_costar


def test_costar_import():
    """Test that CoStar module can be imported."""
    assert fetch_costar is not None 