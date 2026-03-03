from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

messages_file = "messages.txt"

def get_messages():
    if not os.path.exists(messages_file):
        return []
    with open(messages_file, "r") as f:
        return f.read().splitlines()

def save_message(msg):
    with open(messages_file, "a") as f:
        f.write(msg + "\n")

@app.route('/')
def messenger():
    return render_template('messenger.html')

@app.route('/get_messages')
def get_messages_route():
    return jsonify(get_messages())

@app.route('/add_message', methods=['POST'])
def add_message():
    data = request.json
    name = data.get("name", "Unknown")
    message = data.get("message", "")

    if message:
        save_message(f"{name}: {message}")

    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)