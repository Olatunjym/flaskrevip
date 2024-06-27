from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def reverse_ip():
    # Get the client's IP address
    client_ip = request.remote_addr
    # Reverse the IP address
    reversed_ip = client_ip[::-1]
    # Return the reversed IP address
    return f'Reversed IP: {reversed_ip}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
