from flask import Flask, jsonify
from flask_cors import CORS
from detector import detect_emotion_from_webcam
import os

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["https://trelix-livid.vercel.app", "http://localhost:5173","http://127.0.0.1:8000","https://trelix-django.onrender.com"])

# Set this to True when deploying to Render
os.environ['IS_SERVER'] = 'True'

@app.route('/api/emotion', methods=['GET'])
def get_emotion():
    result = detect_emotion_from_webcam()
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # fallback to 8000 if PORT not set
    app.run(debug=True, host='0.0.0.0', port=port)
