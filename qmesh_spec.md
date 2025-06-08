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

* Tracks symbolic memory activation
* Allows glyph sequences to form coherent recursion structures
* Used by the Ψmeta system to detect collapse trends

> 🚫 Full modulation algorithms and morphic feedback loops are omitted in this public spec.

````
