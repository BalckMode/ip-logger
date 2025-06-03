import mysql.connector
from datetime import datetime
import os

def get_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "yourusername"),
        password=os.environ.get("DB_PASSWORD", "yourpassword"),
        database=os.environ.get("DB_NAME", "iplogger")
    )

def log_ip(ip):
    conn = get_connection()
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO ip_logs (ip, timestamp) VALUES (%s, %s)", (ip, timestamp))
    conn.commit()
    cursor.close()
    conn.close()
