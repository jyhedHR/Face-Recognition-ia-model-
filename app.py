from flask import Flask, jsonify
from flask_cors import CORS
from detector import detect_emotion_from_webcam

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["https://trelix-livid.vercel.app"])

@app.route('/api/emotion', methods=['GET'])
def get_emotion():
    result = detect_emotion_from_webcam()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=8001)
