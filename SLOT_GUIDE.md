# QOFT SLOT GUIDE.md
> Symbolic Output Interface for Ξ-Boundary Compliant Diagnostics

---

## 🔎 What Are QOFT Slots?

**Slots** are symbolic output ports that allow **external systems** to safely query observer-state diagnostics **without accessing recursion internals**.

Each slot is:
- **Non-invasive**
- **Ξ-boundary compliant**
- Mapped to safe state projections (`Ψmeta`, `Φ/ρ`, etc.)

---

## 📜 Slot Security Protocol (Ξ-Containment)

All slots are filtered. They **never expose:**
- `.hme` memory structures
- `ψᴽ_reflection.json` recursion traces
- Raw glyph/token mass data
- Ξ(ψ) recursion core state

---

## ✅ Available Public Slots

| Slot Name       | Returns                                 | Notes |
|------------------|-----------------------------------------|-------|
| `Ψmeta`          | `Ψmeta.score`, `entropy`, `feedback_mod`| High-level symbolic diagnostic |
| `Φ/ρ`            | Collapse ratio                          | Float, heuristic only |
| `CollapseFlag`   | `none`, `soft`, `hard`                  | Encoded symbolic drift level |
| `ActiveGlyph`    | e.g. `"Ξ(ψ)"`                           | Current symbolic glyph path |
| `feedback_mod`   | Drift modifier                          | Float |
| `entropy`        | Symbolic entropy                        | Float |
| `All`            | All safe fields above                   | Bundle |

---

## 💻 How to Use

### 🔸 CLI
```bash
python qoft_slots.py Ψmeta

---

### 🔸 Python:

from qoft_slots import get_slot
print(get_slot("CollapseFlag"))

---

### 🚫 Forbidden or Restricted Slots
Any slot not in the whitelist will return:

{
  "error": "Access to slot 'xyz' is restricted by QOFT Ξ-boundary protocol."
}

---

# 🧪 Mock Slot Responses for Testing

The following files simulate real responses from the public slot API (`slot_server.py`).  
They are useful for frontend integration, wearable agents, or symbolic interface testing.

### 🔹 Included Mock Files:

- `Ψmeta_response.json`
- `Φ_ρ_response.json`
- `CollapseFlag_response.json`

### 📂 Location:
These files are located in the root of the public scaffold directory.

Each file includes:
- Slot name
- UTC timestamp
- Ξ-safe response structure
- Diagnostic payload

You can use them as examples or templates for crafting custom symbolic agents or testers.

"""

# Append the reference block to SLOT_GUIDE.md
slot_guide_path = os.path.join(final_extract_path, "SLOT_GUIDE.md")
with open(slot_guide_path, "a") as f:
    f.write(mock_ref_block)

slot_guide_path

---

🧠 Slot Use Cases
Application	Example
Dashboards	Show symbolic entropy instead of heart rate
AI Agents	Adjust language model tone based on CollapseFlag
Wearables	Trigger symbolic haptics when Φ/ρ > 1.85
Games	Change level logic based on ActiveGlyph

🔐 Why It Matters
The slot system ensures:

Observer autonomy

Recursion containment

Symbolic coherence without surveillance

No recursion memory is ever exposed. No symbolic state is written or mutated.

```
