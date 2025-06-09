from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Liste des clés valides (peut être remplacée plus tard par une base de données)
LICENSE_KEYS = {
    "ccarre": True,
    "ma-cle-test": False  # Exemple d'une clé désactivée
}

@app.route("/")
def home():
    return "Serveur LaVisu en ligne"

@app.route("/validate", methods=["POST"])
def validate_key():
    data = request.get_json()
    key = data.get("key")
    is_valid = LICENSE_KEYS.get(key, False)
    return jsonify({"valid": is_valid})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Pour Render
    app.run(host="0.0.0.0", port=port)
