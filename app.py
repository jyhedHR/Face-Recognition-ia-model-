from flask import Flask, jsonify, request
from flask_cors import CORS
from detector import detect_emotion_from_image
import os

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["https://trelix-livid.vercel.app"])

@app.route('/api/emotion', methods=['POST'])
def get_emotion():
    data = request.json
    image_data = data.get('image')  # Get image data from request
    if not image_data:
        return jsonify({"error": "No image data received"})
    
    result = detect_emotion_from_image(image_data)  # Pass image data to emotion detector
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # fallback to 8000 if PORT not set
    app.run(debug=True, host='0.0.0.0', port=port)
