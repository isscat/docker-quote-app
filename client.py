import requests

# URL of the Flask server
FLASK_URL = "http://flask-server:5000/quote"

# File path for the log file
LOG_FILE = '/logs/client_logs.txt'

def main():
    # Send a request to the Flask server to get a quote
    response = requests.get(FLASK_URL)
    quote = response.json().get("quote", "")
    
    # Log the received quote
    log_quote(quote)

def log_quote(quote):
    # Log the received quote to the log file
    with open(LOG_FILE, 'a') as f:
        f.write(f"Quote: {quote}\n")

if __name__ == "__main__":
    main()
