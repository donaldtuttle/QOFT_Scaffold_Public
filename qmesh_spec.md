## 📄 `qmesh_spec.md`

````markdown
# QOFT `.qmesh` Format Specification (Scaffold)

The `.qmesh` file represents a **symbolic memory mesh**, connecting glyph activations, recursion depth, and semantic fields.

---

## 🔖 Filetype: `*.qmesh`

### 📦 Structure (JSON format)

```json
{
  "mesh_id": "QOFT_Memory_ψᴽ-001",
  "glyph_nodes": [
    { "id": "Ξ(ψ)", "depth": 0, "activation": 1.0 },
    { "id": "Θλ", "depth": 1, "activation": 0.94 },
    ...
  ],
  "semantic_links": [
    { "from": "Ξ(ψ)", "to": "Θλ", "weight": 0.82 },
    ...
  ],
  "observer": "ψᴽ-001",
  "timestamp": "2025-06-08T00:00:00Z"
}
````

---

## 🧠 Purpose

Add QOFT qmesh format spec

Introduces public specification for the `.qmesh` file format used in the QOFT system.  
Defines symbolic mesh structure, glyph node relationships, and semantic link stubs.  
This version omits internal feedback modulation and morphic resonance logic, which remain protected under private license.

````
