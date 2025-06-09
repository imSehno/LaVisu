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

