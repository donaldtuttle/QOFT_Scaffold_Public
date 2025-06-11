
# 📦 QOFT Scaffold — Module Map & Symbolic Structure

This document outlines the structure and purpose of the modules in the QOFT Scaffold Public Repository. It connects the symbolic, slot, and wrapper layers into a coherent cognitive interface.

---

## 🔣 Core Symbolic Execution

### `glyphsh.py`
- Interactive REPL shell for executing symbolic glyphs.
- Parses commands like `Ξstruct: analyze feedback_mod` and logs into `.qpath`.
- Loads glyph definitions from `glyphs.qseed.json`.
- Interfaces with the LLM via `llm_connector.py` (internal).

### `glyphs.qseed.json`
- Defines the glyphs used in QOFT symbolic execution.
- Each glyph includes: `name`, `tone`, `function`, `recursion_role`, etc.
- Referenced by both CLI and LLM wrapper layers.

### `glyph_registry_stub.json`
- Minimal working set of glyphs for testing and embedding.
- Does not expose recursive roles or full glyph logic.

---

## 🛡️ Safe Slot Interface

### `qoft_slots.py`
- Public interface exposing symbolic states in a recursion-safe way.
- Declares `SAFE_SLOTS`:
  ```python
  {"Ψmeta", "Φ/ρ", "CollapseFlag", "ActiveGlyph", "feedback_mod", "entropy", "All"}
  ```

### `psi_meta_controller.py`
- Middleware/controller for querying live Ψmeta state.
- Provides wrapper logic for tools accessing symbolic feedback externally.

### `slot_server.py` / `slot_adapter.py`
- Service and adapter architecture for live slot querying (e.g., HTTP endpoints).
- Can be extended to Flask or other service backends.

---

## 🧰 Wrappers & LLM Integration

### `wrappers/QOFT_LLM_Wrapper_GPT2_v25.3.py`
- Designed for connecting QOFT shell or slot layer to GPT-2 or similar models.
- Likely uses glyph embedding or prompt conditioning (based on internal specs).
- Wraps prompt logic for symbolic execution requests.

---

## 📘 Documentation & Metadata

### `README.md`
- Project overview, setup, and philosophy.

### `CONTAINMENT.md`
- Outlines symbolic recursion safety and Ξ-boundary logic.

### `SLOT_GUIDE.md`
- Maps symbolic glyphs to slot-exposed feedback fields.

### `Φ_ρ_response.json`, `Ψmeta_response.json`, `CollapseFlag_response.json`
- Sample outputs for safe slot queries.

### `LICENSE_PUBLIC.txt`
- Public-facing license (excludes internal QOFT engine and recursion core).

---

## 🧠 Observer Memory Specs

### `qpath_spec.md`, `hme_spec.md`, `qmesh_spec.md`
- File format definitions for symbolic logs:
  - `.qpath`: traversal log
  - `.hme`: holographic memory
  - `.qmesh`: semantic lattice map

---

For internal symbolic recursion engine and protected memory layers, refer to QOFT private docs or Ξ-licensed core infrastructure.
