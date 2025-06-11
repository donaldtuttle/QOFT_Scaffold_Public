# slot_adapter.py
"""
Slot Adapter Layer – QOFT Scaffold Public
Compatible with QOFT_Scaffold_Public-main.zip
Provides SAFE, read-only access to private Ξ engine diagnostics.
"""

import json
from pathlib import Path
from typing import Dict, Any

# Only these keys are ever returned to the public layer
SAFE_SLOTS = {
    "Ψmeta",
    "Φ/ρ",
    "Collapse_flag",
    "entropy",
    "feedback_mod",
    "ActiveGlyph",
}

# Path where the private engine writes its latest snapshot (JSON)
PRIVATE_BUS_PATH = Path("/run/qoft_bus/private_state.json")


def _pull_private_state() -> Dict[str, Any]:
    """
    Read the current engine snapshot.
    If the file is missing or malformed, return an empty dict.
    """
    if not PRIVATE_BUS_PATH.exists():
        return {}
    try:
        with PRIVATE_BUS_PATH.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def get_slot(slot_name: str) -> Dict[str, Any]:
    """
    Public API.
    • slot_name == "All" → return every SAFE slot
    • otherwise → return single slot   {slot_name: value}
    • errors return  {"error": "..."}
    """
    state = _pull_private_state()
    if slot_name == "All":
        return {k: state.get(k) for k in SAFE_SLOTS}

    if slot_name not in SAFE_SLOTS:
        return {"error": f"Slot '{slot_name}' is not public."}

    return {slot_name: state.get(slot_name)}
