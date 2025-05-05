from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Success is not in what you have, but who you are.",
    "Hardships often prepare ordinary people for an extraordinary destiny.",
    "Dream big and dare to fail.",
    "Turn your wounds into wisdom."
]

@app.route('/quote')
def quote():
    return jsonify({'quote': random.choice(quotes)})

if __name__ == '__main__':
    app.run(debug=True)

