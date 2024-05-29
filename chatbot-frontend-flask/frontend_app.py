import os
import logging
from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
from flask_session import Session  # Import Flask-Session for server-side sessions
import requests

app = Flask(__name__)
CORS(app)

# Session configuration
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

backend_service = os.getenv('API_ENDPOINT', 'http://localhost:5000')

def send_to_backend(input_text):
    api_endpoint = f"{backend_service}/chat"
    data = {'dialog': [input_text]}
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(api_endpoint, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Failed to reach the backend: {str(e)}")
        return {'response': 'Error: Could not reach the backend.', 'podName': 'N/A', 'nodeName': 'N/A'}

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'messages' not in session:
        session['messages'] = []

    if request.method == 'POST':
        data = request.get_json()  # Get JSON data sent from the front-end
        user_input = data['message']
        if user_input:
            response_data = send_to_backend(user_input)
            session['messages'].append({'text': user_input, 'user': True})
            session['messages'].append({'text': response_data['response'], 'user': False})
            session.modified = True
            return jsonify({
                'response': response_data['response'],
                'podName': response_data['podName'],
                'nodeName': response_data['nodeName']
            })

    return render_template('chat.html', messages=session['messages'])

@app.route('/clear_session', methods=['POST'])
def clear_session():
    session.clear()
    return jsonify({'status': 'session cleared'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
