"""
Tests for monitoring server.
"""

import pytest
from fastapi.testclient import TestClient
from src.backend.monitoring.server import monitoring_app

client = TestClient(monitoring_app)


class TestMonitoringServer:
    """Test cases for monitoring server."""
    
    def test_metrics_endpoint_returns_200(self):
        """Test that /metrics endpoint returns HTTP 200."""
        response = client.get("/metrics")
        assert response.status_code == 200
    
    def test_metrics_endpoint_content_type(self):
        """Test that /metrics endpoint returns text/plain content type."""
        response = client.get("/metrics")
        assert response.headers["content-type"] == "text/plain"
    
    def test_metrics_endpoint_content(self):
        """Test that /metrics endpoint returns Prometheus-formatted content."""
        response = client.get("/metrics")
        content = response.text
        
        # Should contain Prometheus metric definitions
        assert "# HELP" in content or "# TYPE" in content
        assert len(content) > 0
    
    def test_health_endpoint(self):
        """Test that /health endpoint returns healthy status."""
        response = client.get("/health")
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data
    
    def test_metrics_middleware_records_requests(self):
        """Test that metrics middleware records request metrics."""
        # Make a few requests to generate metrics
        client.get("/health")
        client.get("/metrics")
        
        # Get metrics and verify they contain our requests
        response = client.get("/metrics")
        content = response.text
        
        # Should contain metrics for our requests
        assert "http_requests_total" in content
        assert "http_request_duration_seconds" in content 