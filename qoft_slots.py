# qoft_slots.py
"""
Public Slot Interface – replaces qoft_slots_demo.py
Compatible with slot_adapter.py and slot_server.py
"""

from slot_adapter import get_slot, SAFE_SLOTS
import json
import sys


def cli():
    """
    Basic CLI usage:
        python qoft_slots.py All
        python qoft_slots.py Ψmeta
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <slot_name|All>")
        print(f"Available slots: {', '.join(sorted(SAFE_SLOTS))} or 'All'")
        sys.exit(1)

    slot_name = sys.argv[1]
    result = get_slot(slot_name)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    cli()
# qoft_slots.py
"""
Public Slot Interface – replaces qoft_slots_demo.py
Compatible with slot_adapter.py and slot_server.py
"""

from slot_adapter import get_slot, SAFE_SLOTS
import json
import sys


def cli():
    """
    Basic CLI usage:
        python qoft_slots.py All
        python qoft_slots.py Ψmeta
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <slot_name|All>")
        print(f"Available slots: {', '.join(sorted(SAFE_SLOTS))} or 'All'")
        sys.exit(1)

    slot_name = sys.argv[1]
    result = get_slot(slot_name)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    cli()
