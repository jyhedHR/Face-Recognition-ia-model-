import cv2
import base64
import numpy as np
from deepface import DeepFace

def detect_emotion_from_image(image_data):
    # Decode base64 image data
    img_data = base64.b64decode(image_data.split(',')[1])  # Skip the base64 prefix 'data:image/jpeg;base64,'
    np_array = np.frombuffer(img_data, np.uint8)
    frame = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    if frame is None:
        return {"error": "Failed to decode image"}

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        dominant_emotion = result[0]['dominant_emotion']
        return {"emotion": dominant_emotion}
    except Exception as e:
        return {"error": str(e)}
