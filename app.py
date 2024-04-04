from flask import Flask, request, jsonify
import subprocess
import requests
import os

app = Flask(__name__)

slack_webhook_url = os.environ.get('SLACK_WEBHOOK_URL')

@app.route('/runcmd', methods=['POST'])
def run_command():
    data = request.form
    command = data.get('text')

    # Sanitize and validate the command (optional)
    if not command or not isinstance(command, str):
        return jsonify({'error': 'Invalid command format'}), 400

    # Execute the bash command
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
        error = result.stderr

        # Send the output to Slack via webhook
        slack_payload = {'text': f"Command output:\n{output}"}
        response = requests.post(slack_webhook_url, json=slack_payload)

        if response.status_code != 200:
            return jsonify({'error': 'Failed to send message to Slack'}), 500
        
        return jsonify({'output': output, 'error': error}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
