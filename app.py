from flask import Flask, request
import psycopg2

app = Flask(__name__)

# Database connection details
DB_HOST = "your-db-host"
DB_NAME = "your-db-name"
DB_USER = "your-db-user"
DB_PASS = "your-db-pass"

def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    return conn

@app.route('/')
def reverse_ip():
    ip = request.remote_addr
    reversed_ip = ip[::-1]
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reversed_ips (ip, reversed_ip) VALUES (%s, %s)", (ip, reversed_ip))
    conn.commit()
    cursor.close()
    conn.close()
    return f"Reversed IP: {reversed_ip}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
