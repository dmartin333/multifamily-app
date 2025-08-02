"""
Tests for monitoring metrics.
"""

import pytest
from backend.monitoring.metrics import (
    inc_request, 
    observe_latency, 
    inc_underwriting_model,
    inc_scenario,
    inc_report_export,
    get_metrics
)


class TestMetrics:
    """Test cases for metrics functions."""
    
    def test_inc_request(self):
        """Test that inc_request can be called without errors."""
        # This should not raise any exceptions
        inc_request("/test", "GET", 200)
        inc_request("/api/scenarios", "POST", 201)
        inc_request("/api/reports", "GET", 404)
    
    def test_observe_latency(self):
        """Test that observe_latency can be called without errors."""
        # This should not raise any exceptions
        observe_latency("/test", "GET", 0.1)
        observe_latency("/api/scenarios", "POST", 1.5)
        observe_latency("/api/reports", "GET", 0.05)
    
    def test_inc_underwriting_model(self):
        """Test that inc_underwriting_model can be called without errors."""
        inc_underwriting_model()
        inc_underwriting_model()
    
    def test_inc_scenario(self):
        """Test that inc_scenario can be called without errors."""
        inc_scenario()
        inc_scenario()
    
    def test_inc_report_export(self):
        """Test that inc_report_export can be called without errors."""
        inc_report_export("xlsx")
        inc_report_export("pdf")
        inc_report_export("pptx")
    
    def test_get_metrics_returns_string(self):
        """Test that get_metrics returns a string."""
        metrics = get_metrics()
        assert isinstance(metrics, str)
        assert len(metrics) > 0
    
    def test_get_metrics_contains_prometheus_format(self):
        """Test that get_metrics returns Prometheus-formatted metrics."""
        metrics = get_metrics()
        # Should contain some Prometheus metric lines
        assert "# HELP" in metrics or "# TYPE" in metrics 