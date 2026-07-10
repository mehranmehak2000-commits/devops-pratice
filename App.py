from flask import Flask, jsonify
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from my DevOps CI/CD pipeline!",
        "hostname": socket.gethostname(),
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/version")
def version():
    return jsonify({"version": "1.0.0", "app": "devops-demo"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
