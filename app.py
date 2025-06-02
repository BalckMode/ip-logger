from flask import Flask, request, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - IP: {ip}\n"

    # Ensure logs.txt exists before writing
    if not os.path.exists("logs.txt"):
        open("logs.txt", "w").close()

    with open("logs.txt", "a") as f:
        f.write(log_entry)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
