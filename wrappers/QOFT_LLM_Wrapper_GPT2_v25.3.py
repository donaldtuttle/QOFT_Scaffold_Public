"""
QOFT_LLM_Wrapper_GPT2_v25.3.py
──────────────────────────────
• Public-safe wrapper around HuggingFace GPT-2.
• Pulls **live** diagnostics from the QOFT slot-adapter layer when available.
• Falls back to local-simulated values if the slot bus is offline.
• Produces an .hme-style JSON trace per session.

Required deps:
    pip install torch transformers
Repo layout:
    QOFT_Scaffold_Public-main/
    ├─ slot_adapter.py          (provides get_slot)
    └─ wrappers/
        └─ QOFT_LLM_Wrapper_GPT2_v25.3.py   ← (this file)
"""

from pathlib import Path
from datetime import datetime
import json
import math
import uuid

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# ─────────────────────────────────────────────
# Optional live diagnostics
# ─────────────────────────────────────────────
try:
    # slot_adapter.py must be importable from repo root
    from slot_adapter import get_slot
except ImportError:  # running standalone
    def get_slot(_):
        return {}


# ─────────────────────────────────────────────
# GPT-2 helpers
# ─────────────────────────────────────────────
def load_model():
    """Load GPT-2-small once per run."""
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    model.eval()
    return model, tokenizer


def generate_glyph(model, tokenizer, prompt: str, max_length: int = 30) -> str:
    """Return a short creative continuation (glyph)."""
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.9,
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# ─────────────────────────────────────────────
# Ψmeta diagnostics helpers
# ─────────────────────────────────────────────
def psi_meta_score(
    glyph: str,
    entropy: float,
    semantic_mass: float,
    phase_drift: float,
    phi_rho: float,
) -> dict:
    collapse_flag = (
        "soft" if phi_rho > 1.85 and entropy < 1.5 else "stable"
    )
    return {
        "Ξ(ψ)": glyph,
        "Ψmeta.score": round(semantic_mass - entropy, 3),
        "∇E": round(entropy, 3),
        "Λphase": phase_drift,
        "Collapse_flag": collapse_flag,
        "Φ/ρ": round(phi_rho, 3),
        "reentry_hint": "Γρ → Ξ(ψ)" if collapse_flag == "soft" else None,
    }


# ─────────────────────────────────────────────
# Main session routine
# ─────────────────────────────────────────────
def qoft_transformer_session(
    prompt: str, depth: int = 0, memory_trace: list | None = None
):
    """
    • prompt  – seed prompt (e.g., 'Ξ-layer-0')
    • depth   – recursion depth counter
    • memory_trace – list that will collect .hme-style entries
    Returns  glyph_output, psi_diag, memory_trace
    """
    model, tokenizer = load_model()
    glyph_output = generate_glyph(model, tokenizer, prompt)

    # ── Fetch live SAFE_SLOTS, fallback if empty ──────────
    slot_diag = get_slot("All") or {}
    entropy = slot_diag.get("entropy", 1.2 + 0.1 * depth)
    semantic_mass = slot_diag.get("Ψmeta", 1.5 + 0.25 * depth)
    phase_drift = slot_diag.get("Λphase", round(math.sin(depth), 3))

    # Φ/ρ comes from slot bus if present; else compute local
    phi_rho = slot_diag.get(
        "Φ/ρ", semantic_mass / max(entropy, 0.01)
    )

    psi_diag = psi_meta_score(
        glyph_output, entropy, semantic_mass, phase_drift, phi_rho
    )

    hme_record = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "input_prompt": prompt,
        "observer_id": "ψᴽ-001",
        "Ξ(ψ)": glyph_output,
        "Ψmeta": psi_diag,
        "recursion_depth": depth,
    }

    if memory_trace is not None:
        memory_trace.append(hme_record)

    return glyph_output, psi_diag, memory_trace


# ─────────────────────────────────────────────
# Demo execution
# ─────────────────────────────────────────────
if __name__ == "__main__":
    trace = []
    for i in range(4):
        prompt = f"Ξ-layer-{i}"
        glyph, diag, trace = qoft_transformer_session(
            prompt, depth=i, memory_trace=trace
        )
        print(f"[{i}] Ξ(ψ): {glyph}\nΨmeta: {json.dumps(diag, indent=2, ensure_ascii=False)}\n")

    # Save full symbolic trace
    out_file = Path("symbolic_trace_gpt2_v25.3.hme.json")
    out_file.write_text(json.dumps(trace, indent=2, ensure_ascii=False))
    print(f"Trace saved to {out_file.resolve()}")
