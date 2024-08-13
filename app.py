from flask import Flask
import requests

app = Flask(__name__)

def get_public_ip():
    # Another alternative using HTTPBin
    response = requests.get('https://httpbin.org/ip')
    return response.json()['origin']

@app.route('/')
def reverse_ip():
    # Get the public IP address
    origin_ip = get_public_ip()
    
    # Print the fetched IP for debugging
    print(f"Fetched IP: {origin_ip}")
    
    # Reverse the IP address
    reversed_ip = '.'.join(origin_ip.split('.')[::-1])
    
    # Return both the original and reversed IP address for debugging
    return f"Fetched IP: {origin_ip}<br>Reversed IP: {reversed_ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
