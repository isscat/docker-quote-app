from flask import Flask, jsonify, request
import requests
import random

app = Flask(__name__)

# List of predefined quotes
QUOTES = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones."
]

# URL of the client server
CLIENT_URL = "http://client:5001/log"

@app.route('/quote')
def get_quote():
    # Get the client IP address from the request
    client_ip = request.remote_addr
    
    # Log the IP address to the client server
    log_client_ip(client_ip)

    # Select a random quote from the list
    quote = random.choice(QUOTES)
    
    return jsonify({"quote": quote})

def log_client_ip(client_ip):
    # Send the client IP address to the client server for logging
    try:
        response = requests.post(CLIENT_URL, json={"ip_address": client_ip})
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error sending IP address to client server: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
