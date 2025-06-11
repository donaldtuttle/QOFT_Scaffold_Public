# slot_server.py
# This script wraps qoft_slots.py in a Flask API, allowing you to query slots like this: GET http://localhost:3388/slot/Ψmeta
# Serves all SAFE_SLOTS via HTTP Fast local testing for symbolic interfaces Maintains Ξ-boundary enforcement Extendable to accept POST data for more complex observers

from flask import Flask, jsonify
from qoft_slots import get_slot

app = Flask(__name__)

@app.route("/slot/<slot_name>", methods=["GET"])
def slot_query(slot_name):
    return jsonify(get_slot(slot_name))

if __name__ == "__main__":
    app.run(port=3388, debug=True)
