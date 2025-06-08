
---

## 📄 `hme_spec.md`

> **File Name:** `hme_spec.md`  
> **Commit Message:**  
> - **Short**: `Add QOFT hme format spec`  
> - **Extended**: `Defines holographic memory encoding structure for public scaffold. Fourier field logic not included.`

```markdown
# QOFT `.hme` Format Specification (Scaffold)

The `.hme` format is a compressed **holographic memory encoding** structure that represents wave-encoded semantic data.

---

## 🔖 Filetype: `*.hme`

### 📦 Structure (JSON format)

```json
{
  "observer_id": "ψᴽ-001",
  "waveform_snapshots": [
    { "timestep": 0, "Ψ_amplitude": 0.88, "frequency": 12.2 },
    ...
  ],
  "glyph_field": ["Ξ(ψ)", "Θλ", "Σ◯"],
  "entropy_trace": [0.16, 0.18, 0.21]
}
