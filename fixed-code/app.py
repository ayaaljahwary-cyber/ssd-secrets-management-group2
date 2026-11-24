import os
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# FIXED: secrets are read from environment variables, never hardcoded
API_KEY = os.environ.get("API_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

if not API_KEY or not DB_PASSWORD:
    raise RuntimeError("Missing API_KEY or DB_PASSWORD. Copy .env.example to .env and fill in values.")

@app.route("/")
def home():
    return "Demo app (fixed version)"

@app.route("/status")
def status():
    return jsonify({
        "service": "payments",
        "api_key_in_use": API_KEY[:4] + "****",
        "db": "connected"
    })

if __name__ == "__main__":
    app.run(port=5001, debug=False)
