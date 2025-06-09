from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

LICENSE_KEYS = {
    "ccarre": True,
    "abc123": True,
    "expiredkey": False
}

@app.route("/", methods=["GET"])
def home():
    return "✅ Serveur LaVisu en ligne", 200

@app.route("/validate", methods=["GET", "POST"])
def validate_key():
    if request.method == "GET":
        return "✅ endpoint /validate opérationnel (GET d'essai)", 200
    data = request.get_json() or {}
    key = data.get("key", "")
    valid = LICENSE_KEYS.get(key, False)
    return jsonify({"valid": valid}), (200 if valid else 401)
