"""
Tests for scenario endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from backend.underwriting.scenarios.endpoints import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
client = TestClient(app)


class TestScenarioEndpoints:
    """Test cases for scenario endpoints."""
    
    def test_create_scenario(self):
        """Test scenario creation endpoint."""
        scenario_data = {
            "name": "Test Scenario",
            "assumptions": {"property_tax_rate": 0.025}
        }
        
        response = client.post("/scenarios/", json=scenario_data)
        assert response.status_code == 200
        
        data = response.json()
        assert data["name"] == "Test Scenario"
        assert data["status"] == "created"
        assert "scenario_123" in data["id"]
    
    def test_clone_scenario_endpoint(self):
        """Test scenario cloning endpoint."""
        base_id = "test_base_scenario"
        
        response = client.post(f"/scenarios/clone/?base_id={base_id}")
        assert response.status_code == 501  # Not implemented yet
        
        data = response.json()
        assert "detail" in data
        assert "not yet implemented" in data["detail"]
    
    def test_compare_scenarios_endpoint(self):
        """Test scenario comparison endpoint."""
        base_id = "test_base_scenario"
        alt_id = "test_alt_scenario"
        
        response = client.get(f"/scenarios/{base_id}/compare/{alt_id}/")
        assert response.status_code == 200
        
        data = response.json()
        assert "differences" in data
        assert isinstance(data["differences"], list)
    
    def test_compare_scenarios_with_different_ids(self):
        """Test scenario comparison with different scenario IDs."""
        base_id = "scenario_1"
        alt_id = "scenario_2"
        
        response = client.get(f"/scenarios/{base_id}/compare/{alt_id}/")
        assert response.status_code == 200
        
        data = response.json()
        assert data["differences"] == []
    
    def test_compare_scenario(self):
        """Test scenario comparison endpoint."""
        scenario_id = "test_scenario_123"
        
        response = client.get(f"/scenarios/{scenario_id}/compare/")
        assert response.status_code == 200
        
        data = response.json()
        assert data["base_scenario"] == scenario_id
        assert "comparison_data" in data
        assert "irr_difference" in data["comparison_data"]
        assert "npv_difference" in data["comparison_data"]
        assert "cash_flow_impact" in data["comparison_data"] 