"""
OpenAPI configuration for FastAPI documentation.
"""

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from typing import Dict, Any


def custom_openapi(app: FastAPI) -> Dict[str, Any]:
    """
    Custom OpenAPI schema configuration.
    
    Args:
        app: FastAPI application instance
        
    Returns:
        Custom OpenAPI schema dictionary
    """
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Multifamily Underwriting API",
        version="1.0.0",
        description="""
        Comprehensive API for multifamily real estate underwriting and analysis.
        
        ## Features
        
        * **Pro-forma Analysis** - Load and analyze property financial data
        * **Scenario Modeling** - Create and compare different investment scenarios
        * **Assumption Management** - Manage underwriting assumptions and parameters
        * **Reporting** - Generate reports in multiple formats (XLSX, PDF, PPTX)
        * **Collaboration** - Comment and collaborate on models
        * **Data Integration** - Connect with external data sources (CoStar, Yardi, etc.)
        
        ## Authentication
        
        This API supports OAuth2 and SAML authentication methods.
        
        ## Rate Limiting
        
        API requests are rate limited to ensure fair usage.
        """,
        routes=app.routes,
        tags=[
            {
                "name": "underwriting",
                "description": "Underwriting analysis and modeling operations"
            },
            {
                "name": "scenarios",
                "description": "Scenario creation and comparison"
            },
            {
                "name": "reports",
                "description": "Report generation and export"
            },
            {
                "name": "collaboration",
                "description": "Comments and collaboration features"
            },
            {
                "name": "integrations",
                "description": "External data source integrations"
            },
            {
                "name": "monitoring",
                "description": "System monitoring and metrics"
            }
        ]
    )
    
    # Add custom info
    openapi_schema["info"]["x-logo"] = {
        "url": "https://example.com/logo.png"
    }
    
    # Ensure components section exists
    if "components" not in openapi_schema:
        openapi_schema["components"] = {}
    
    # Add security schemes
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2": {
            "type": "oauth2",
            "flows": {
                "authorizationCode": {
                    "authorizationUrl": "https://example.com/oauth/authorize",
                    "tokenUrl": "https://example.com/oauth/token",
                    "scopes": {
                        "read": "Read access",
                        "write": "Write access"
                    }
                }
            }
        },
        "SAML": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "SAML"
        }
    }
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def setup_documentation(app: FastAPI) -> None:
    """
    Setup documentation endpoints for the FastAPI app.
    
    Args:
        app: FastAPI application instance
    """
    # Set custom OpenAPI schema
    app.openapi = lambda: custom_openapi(app)
    
    # Documentation endpoints are automatically available:
    # - GET /docs (Swagger UI)
    # - GET /redoc (ReDoc)
    # - GET /openapi.json (OpenAPI schema) 