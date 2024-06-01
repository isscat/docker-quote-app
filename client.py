from flask import Flask, request
import os

app = Flask(__name__)

# File path for the log file
LOG_FILE = '/logs/client_logs.txt'

@app.route('/log', methods=['POST'])
def log_ip_address():
    # Get the IP address from the request
    ip_address = request.json.get('ip_address')

    # Log the IP address
    log_to_file(ip_address)

    return "OK"

def log_to_file(ip_address):
    # Log the IP address to the log file
    with open(LOG_FILE, 'a') as f:
        f.write(f"Client IP: {ip_address}\n")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
