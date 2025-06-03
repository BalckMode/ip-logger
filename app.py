from flask import Flask, request
from database import log_ip
import os

app = Flask(__name__)

@app.route('/')
def home():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    log_ip(ip)
    return f"Your IP {ip} has been logged."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
