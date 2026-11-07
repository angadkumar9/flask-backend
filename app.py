import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("APP_API_KEY", "not-set")  # sensitive data via env variable


@app.route("/")
def home():
    return jsonify(service="Flask Backend", status="running")


@app.route("/api/health")
def health():
    return jsonify(status="ok")


@app.route("/api/message")
def message():
    return jsonify(message="Hello from Flask backend v2 (auto-deployed)!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)