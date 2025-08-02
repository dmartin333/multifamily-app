"""
Tests for OpenAPI documentation endpoints.
"""

import pytest
import json
from fastapi.testclient import TestClient
from backend.docs.openapi import custom_openapi
from fastapi import FastAPI


class TestOpenAPI:
    """Test cases for OpenAPI documentation."""
    
    def test_openapi_schema_structure(self):
        """Test that OpenAPI schema has correct structure."""
        app = FastAPI()
        schema = custom_openapi(app)
        
        # Check required OpenAPI fields
        assert "openapi" in schema
        assert "info" in schema
        assert "paths" in schema
        
        # Check info structure
        info = schema["info"]
        assert "title" in info
        assert "version" in info
        assert "description" in info
        
        # Check title and version
        assert info["title"] == "Multifamily Underwriting API"
        assert info["version"] == "1.0.0"
    
    def test_openapi_security_schemes(self):
        """Test that OpenAPI schema includes security schemes."""
        app = FastAPI()
        schema = custom_openapi(app)
        
        # Check security schemes
        assert "components" in schema
        assert "securitySchemes" in schema["components"]
        
        security_schemes = schema["components"]["securitySchemes"]
        assert "OAuth2" in security_schemes
        assert "SAML" in security_schemes
    
    def test_openapi_tags(self):
        """Test that OpenAPI schema includes API tags."""
        app = FastAPI()
        schema = custom_openapi(app)
        
        # Check tags
        assert "tags" in schema
        tags = schema["tags"]
        
        # Verify expected tags are present
        tag_names = [tag["name"] for tag in tags]
        expected_tags = [
            "underwriting", "scenarios", "reports", 
            "collaboration", "integrations", "monitoring"
        ]
        
        for expected_tag in expected_tags:
            assert expected_tag in tag_names
    
    def test_openapi_endpoint_returns_valid_json(self):
        """Test that /openapi.json endpoint returns valid JSON."""
        app = FastAPI()
        custom_openapi(app)  # Setup custom schema
        
        client = TestClient(app)
        response = client.get("/openapi.json")
        
        # Check response
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/json"
        
        # Validate JSON
        try:
            schema = response.json()
            assert isinstance(schema, dict)
            assert "openapi" in schema
        except json.JSONDecodeError:
            pytest.fail("Response is not valid JSON")
    
    def test_swagger_ui_endpoint(self):
        """Test that /docs endpoint (Swagger UI) is accessible."""
        app = FastAPI()
        custom_openapi(app)  # Setup custom schema
        
        client = TestClient(app)
        response = client.get("/docs")
        
        # Check response
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        
        # Should contain Swagger UI content
        content = response.text
        assert "swagger" in content.lower() or "swagger-ui" in content.lower() 