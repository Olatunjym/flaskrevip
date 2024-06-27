from flask import Flask, request
import os
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection setup
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(mongo_uri)
db = client['ipdb']
ip_collection = db['ips']

@app.route('/')
def home():
    # Log all headers for debugging
    headers = request.headers
    print(headers)

    # Obtain the original IP address from headers if behind a proxy
    if 'X-Forwarded-For' in request.headers:
        ip = request.headers['X-Forwarded-For'].split(',')[0]
    else:
        ip = request.remote_addr

    reversed_ip = '.'.join(ip.split('.')[::-1])

    # Store the reversed IP in the database
    ip_collection.insert_one({'reversed_ip': reversed_ip})

    return f"Your reversed IP is: {reversed_ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)