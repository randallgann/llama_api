from flask import Flask, request, jsonify
from .model import ModelManager
from .config import API_HOST, API_PORT

app = Flask(__name__)
model_manager = ModelManager.get_instance()

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        
        # Validate input
        if not data or 'messages' not in data:
            return jsonify({'error': 'Missing messages in request'}), 400
        
        # Generate response
        response = model_manager.generate(
            messages=data['messages'],
            temperature=data.get('temperature'),
            max_tokens=data.get('max_tokens')
        )
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def run_app():
    app.run(host=API_HOST, port=API_PORT)

if __name__ == '__main__':
    run_app()
