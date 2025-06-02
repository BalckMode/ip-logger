from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get real IP address from X-Forwarded-For header (Render adds this)
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Log to terminal
    print(f"[{timestamp}] Visitor IP: {ip}")
    
    # Show a friendly message
    return f"Your IP address has been logged: {ip}"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
