import time
from flask import Flask, request, jsonify
from flask_cors import CORS

from script_to_run import process_data

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/execute', methods=['POST'])
def execute_script():
    try:
        # Get the JSON payload from the request
        data = request.json

        # execute script to fill automated forms 
        process_data(data)

        # Return success response
        return jsonify({'message': 'success'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
