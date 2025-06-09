from flask import Flask, request, jsonify

app = Flask(__name__)

# Clés valides en mémoire (à remplacer par une base de données si besoin)
valid_keys = {
    "ccarre": True,
    "test123": True,
    "demo": False  # désactivée
}

@app.route("/validate", methods=["POST"])
def validate_key():
    data = request.get_json()
    key = data.get("key", "")
    is_valid = valid_keys.get(key, False)
    return jsonify({"valid": is_valid})

@app.route("/")
def home():
    return "Serveur LaVisu en ligne", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
