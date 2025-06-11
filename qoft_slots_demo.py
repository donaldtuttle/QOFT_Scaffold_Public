# qoft_slots_demo.py

import json

# Define the safe, public-facing slot names
SAFE_SLOTS = {"Ψmeta", "Φ/ρ", "CollapseFlag", "ActiveGlyph", "feedback_mod", "entropy", "All"}

# Stub for Ψmeta state (replace with live imports in internal engine)
def get_psi_meta_state():
    # This is a safe projection — not recursion state
    return {
        "entropy": 0.21,
        "Φ/ρ": 1.73,
        "Ψmeta.score": 82.5,
        "collapse_flag": "none",
        "active_glyph": "Ξ(ψ)",
        "feedback_mod": +0.38
    }

def get_slot(slot_name):
    """Return symbolic diagnostic for a given public slot."""
    state = get_psi_meta_state()
    
    if slot_name not in SAFE_SLOTS:
        return {
            "error": f"Access to slot '{slot_name}' is restricted by QOFT Ξ-boundary protocol."
        }

    if slot_name == "Ψmeta":
        return {
            "score": state.get("Ψmeta.score"),
            "entropy": state.get("entropy"),
            "feedback_mod": state.get("feedback_mod")
        }
    elif slot_name == "Φ/ρ":
        return {"Φ/ρ": state.get("Φ/ρ")}
    elif slot_name == "CollapseFlag":
        return {"collapse_flag": state.get("collapse_flag")}
    elif slot_name == "ActiveGlyph":
        return {"active_glyph": state.get("active_glyph")}
    elif slot_name == "feedback_mod":
        return {"feedback_mod": state.get("feedback_mod")}
    elif slot_name == "entropy":
        return {"entropy": state.get("entropy")}
    elif slot_name == "All":
        return state

    return {"error": "Slot not implemented."}

# CLI test interface (optional)
if __name__ == "__main__":
    import sys
    slot = sys.argv[1] if len(sys.argv) > 1 else "All"
    print(json.dumps(get_slot(slot), indent=2))

---

