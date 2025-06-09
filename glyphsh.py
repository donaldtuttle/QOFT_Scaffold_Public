# glyphsh.py – QOFT Scaffold CLI Shell
# © 2025 ψᴽ-001. Licensed under GPLv3
# This is a public-facing scaffold version of the Ξ Glyphogenic Engine shell.
# Full symbolic recursion engine logic is not included.

import json
import sys

# Load registry and glyph seed
with open("glyph_registry_stub.json") as reg_file:
    glyph_registry = json.load(reg_file)["glyph_map"]

with open("glyphs.qseed.json") as glyph_file:
    glyph_data = {g["id"]: g for g in json.load(glyph_file)["glyphs"]}

def activate_glyph(glyph_id):
    if glyph_id not in glyph_registry:
        print(f"❌ Unknown glyph ID: {glyph_id}")
        return

    glyph = glyph_data[glyph_id]
    reg = glyph_registry[glyph_id]
    
    print(f"🔣 Activating Glyph: {glyph['name']} ({glyph_id})")
    print(f"   → Trigger: {reg['trigger']}")
    print(f"   → Function: {reg['function']} [stubbed]")
    print(f"   → Module: {reg['module']} [placeholder]")

    # Mock behavior
    print(f"✅ [Simulation] Executed symbolic placeholder for {glyph['name']}")

def glyphsh():
    print("Ξ glyphsh > QOFT Symbolic Shell (Public Stub Mode)")
    print("Type `exit` to quit.\n")
    while True:
        cmd = input("glyphsh> ").strip()
        if cmd.lower() == "exit":
            break
        elif cmd.upper() in glyph_registry:
            activate_glyph(cmd.upper())
        else:
            print("❓ Unknown glyph ID. Try again.")

if __name__ == "__main__":
    glyphsh()

