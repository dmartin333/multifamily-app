"""
Prometheus metrics for monitoring and performance tracking.
"""

from prometheus_client import Counter, Histogram, generate_latest
from typing import Optional

# Define Prometheus metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total number of HTTP requests',
    ['path', 'method', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency in seconds',
    ['path', 'method'],
    buckets=[0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0]
)

# Additional metrics for business logic
UNDERWRITING_MODELS_CREATED = Counter(
    'underwriting_models_created_total',
    'Total number of underwriting models created'
)

SCENARIOS_GENERATED = Counter(
    'scenarios_generated_total',
    'Total number of scenarios generated'
)

REPORTS_EXPORTED = Counter(
    'reports_exported_total',
    'Total number of reports exported',
    ['format']  # xlsx, pdf, pptx
)


def inc_request(path: str, method: str, status: int) -> None:
    """
    Increment request counter metric.
    
    Args:
        path: Request path
        method: HTTP method
        status: HTTP status code
    """
    REQUEST_COUNT.labels(path=path, method=method, status=status).inc()


def observe_latency(path: str, method: str, latency: float) -> None:
    """
    Observe request latency metric.
    
    Args:
        path: Request path
        method: HTTP method
        latency: Request latency in seconds
    """
    REQUEST_LATENCY.labels(path=path, method=method).observe(latency)


def inc_underwriting_model() -> None:
    """Increment underwriting model creation counter."""
    UNDERWRITING_MODELS_CREATED.inc()


def inc_scenario() -> None:
    """Increment scenario generation counter."""
    SCENARIOS_GENERATED.inc()


def inc_report_export(format_type: str) -> None:
    """
    Increment report export counter.
    
    Args:
        format_type: Export format (xlsx, pdf, pptx)
    """
    REPORTS_EXPORTED.labels(format=format_type).inc()


def get_metrics() -> str:
    """
    Generate Prometheus metrics output.
    
    Returns:
        String containing all metrics in Prometheus format
    """
    return generate_latest().decode('utf-8') 