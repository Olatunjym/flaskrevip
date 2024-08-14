from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def reverse_ip():
    # Get the original client IP address from X-Forwarded-For header if present
    origin_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Log the fetched IP address for debugging
    print(f"Fetched IP: {origin_ip}")
    
    # Reverse the IP address
    reversed_ip = '.'.join(origin_ip.split('.')[::-1])
    
    # Return both the original and reversed IP address
    return f"Fetched IP: {origin_ip}<br>Reversed IP: {reversed_ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
