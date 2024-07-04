from flask import Flask, request, jsonify
import logging
from model import run, get_input_token_length

app = Flask(__name__)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("flask_app")


@app.route('/')
def home():
    return "Welcome to the text generation API. Use /chat/generate to generate text."


@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({'error': 'Prompt is missing.'}), 400

    prompt = data.get('prompt', '')
    system_prompt = data.get('system_prompt', '')
    max_new_tokens = data.get('max_new_tokens', 1024)
    temperature = data.get('temperature', 0.8)
    top_p = data.get('top_p', 0.95)
    top_k = data.get('top_k', 50)
    chat_history = data.get('chat_history', [])

    try:
        generator = run(prompt, chat_history, system_prompt, max_new_tokens, temperature, top_p, top_k)
        response = ""
        for text in generator:
            pass
        response = text
    except Exception as e:
        logger.error(f"Error during text generation: {e}")
        return jsonify({'error': str(e)}), 500

    return jsonify({'text': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
