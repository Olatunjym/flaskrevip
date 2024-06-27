from flask import Flask, request

app = Flask(__name__)

def get_client_ip():
    if request.headers.get('X-Forwarded-For'):
        client_ip = request.headers.get('X-Forwarded-For').split(',')[0]
    else:
        client_ip = request.remote_addr
    return client_ip

@app.route('/')
def reverse_ip():
    client_ip = get_client_ip()
    reversed_ip = '.'.join(client_ip.split('.')[::-1])
    return f"Reversed IP: {reversed_ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
