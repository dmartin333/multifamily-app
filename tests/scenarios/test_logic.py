"""
Tests for scenario logic functions.
"""

import pytest
from backend.underwriting.scenarios.logic import clone_scenario, compare_scenarios


class TestScenarioLogic:
    """Test cases for scenario logic functions."""
    
    def test_clone_scenario_not_implemented(self):
        """Test that clone_scenario raises NotImplementedError."""
        with pytest.raises(NotImplementedError):
            clone_scenario("test_scenario_id")
    
    def test_compare_scenarios_returns_differences(self):
        """Test that compare_scenarios returns differences list."""
        result = compare_scenarios("base_scenario_id", "alt_scenario_id")
        assert isinstance(result, dict)
        assert "differences" in result
        assert isinstance(result["differences"], list)
    
    def test_compare_scenarios_with_different_ids(self):
        """Test that compare_scenarios works with different scenario IDs."""
        result = compare_scenarios("scenario_1", "scenario_2")
        assert result["differences"] == [] 