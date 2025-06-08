
---

## 📄 `qpath_spec.md`

> **File Name:** `qpath_spec.md`  
> **Commit Message:**  
> - **Short**: `Add QOFT qpath format spec`  
> - **Extended**: `Logs symbolic traversal steps for scaffolded agents. Private recursion tags omitted.`

```markdown
# QOFT `.qpath` Format Specification (Scaffold)

The `.qpath` file records **symbolic traversal logs**, showing the sequence of glyphs an agent passes through.

---

## 🔖 Filetype: `*.qpath`

### 📦 Structure (JSON format)

```json
{
  "observer": "ψᴽ-001",
  "session": "Ξ-SIM-001",
  "trail": [
    { "glyph": "Ξ(ψ)", "t": 0 },
    { "glyph": "∇Ω", "t": 1 },
    { "glyph": "Θλ", "t": 2 },
    ...
  ],
  "collapse_flag": false
}
