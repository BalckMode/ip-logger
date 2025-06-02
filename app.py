import os
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def log_ip():
    ip = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - IP: {ip}")

    # Optional: write to file (not persistent on Render)
    with open("logs.txt", "a") as f:
        f.write(f"{timestamp} - IP: {ip}\n")

    return "Your IP has been logged."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT from Render
    app.run(host="0.0.0.0", port=port)
