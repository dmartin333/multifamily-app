"""
Assumption service for managing underwriting assumptions.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any


def load_assumptions(name: str) -> Dict[str, Any]:
    """
    Load assumption set by name.
    
    Args:
        name: Name of the assumption set to load
        
    Returns:
        Dictionary containing assumption data
        
    Raises:
        ValueError: If assumption set not found
    """
    # Get the path to the assumptions directory
    assumptions_dir = Path(__file__).parent.parent.parent.parent.parent / "data" / "assumptions"
    file_path = assumptions_dir / f"{name}.json"
    
    if not file_path.exists():
        raise ValueError(f"Assumption set '{name}' not found")
    
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in assumption set '{name}': {e}")
    except Exception as e:
        raise ValueError(f"Error loading assumption set '{name}': {e}")


def list_assumption_sets() -> List[str]:
    """
    List all available assumption sets.
    
    Returns:
        List of assumption set names
    """
    # Get the path to the assumptions directory
    assumptions_dir = Path(__file__).parent.parent.parent.parent.parent / "data" / "assumptions"
    
    if not assumptions_dir.exists():
        return []
    
    assumption_sets = []
    for file_path in assumptions_dir.glob("*.json"):
        # Return filename without .json extension
        assumption_sets.append(file_path.stem)
    
    return sorted(assumption_sets) 