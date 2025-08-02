"""
Tests for authentication service.
"""

import pytest
from src.backend.auth.auth_service import login_oauth2, verify_saml_assertion


def test_login_oauth2_import():
    """Test that login_oauth2 function can be imported."""
    assert login_oauth2 is not None


def test_verify_saml_assertion_import():
    """Test that verify_saml_assertion function can be imported."""
    assert verify_saml_assertion is not None


def test_login_oauth2_not_implemented():
    """Test that login_oauth2 raises NotImplementedError."""
    with pytest.raises(NotImplementedError):
        login_oauth2("google", "test_code")


def test_verify_saml_assertion_not_implemented():
    """Test that verify_saml_assertion raises NotImplementedError."""
    with pytest.raises(NotImplementedError):
        verify_saml_assertion("test_assertion") 