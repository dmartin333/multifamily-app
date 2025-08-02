"""
Tests for BLS integration.
"""

import pytest
from src.backend.integrations.bls import fetch_bls


def test_bls_import():
    """Test that BLS module can be imported."""
    assert fetch_bls is not None 