from flask import Flask, jsonify
import requests

app = Flask(__name__)

# VULNERABLE: secrets hardcoded directly in source code (all values are FAKE)
API_KEY = "demo_api_key_FAKE_1234567890abcdef"
DB_PASSWORD = "SuperSecretP@ssw0rd123"
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@app.route("/")
def home():
    return "Demo app (vulnerable version)"

@app.route("/status")
def status():
    return jsonify({
        "service": "payments",
        "api_key_in_use": API_KEY[:8] + "****",
        "db": "connected"
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
