from flask import Flask, jsonify
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

# File path for the log file
LOG_FILE = '/logs/quote_logs.txt'

@app.route('/quote')
def get_quote():
    # Select a random quote
    quote = random.choice(QUOTES)
    
    # Log the selected quote
    log_quote(quote)

    return jsonify({"quote": quote})

def log_quote(quote):
    # Log the selected quote to the log file
    with open(LOG_FILE, 'a') as f:
        f.write(f"Quote: {quote}\n")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
