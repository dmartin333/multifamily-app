"""
Monitoring server with Prometheus metrics endpoint and middleware.
"""

import time
from fastapi import FastAPI, Request, Response
from fastapi.middleware.base import BaseHTTPMiddleware
from .metrics import inc_request, observe_latency, get_metrics


class MetricsMiddleware(BaseHTTPMiddleware):
    """
    Middleware to collect HTTP request metrics.
    """
    
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # Process the request
        response = await call_next(request)
        
        # Calculate latency
        latency = time.time() - start_time
        
        # Extract path and method
        path = request.url.path
        method = request.method
        status = response.status_code
        
        # Record metrics
        inc_request(path=path, method=method, status=status)
        observe_latency(path=path, method=method, latency=latency)
        
        return response


def create_monitoring_app() -> FastAPI:
    """
    Create FastAPI app with monitoring middleware and metrics endpoint.
    
    Returns:
        FastAPI application with monitoring capabilities
    """
    app = FastAPI(title="Multifamily Underwriting API", version="1.0.0")
    
    # Add metrics middleware
    app.add_middleware(MetricsMiddleware)
    
    @app.get("/metrics")
    async def metrics_endpoint():
        """
        Prometheus metrics endpoint.
        
        Returns:
            Prometheus-formatted metrics
        """
        return Response(
            content=get_metrics(),
            media_type="text/plain"
        )
    
    @app.get("/health")
    async def health_check():
        """
        Health check endpoint.
        
        Returns:
            Health status
        """
        return {"status": "healthy", "timestamp": time.time()}
    
    return app


# Create the monitoring app instance
monitoring_app = create_monitoring_app() 