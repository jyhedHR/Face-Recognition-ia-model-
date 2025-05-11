import cv2
from deepface import DeepFace
import os
import random

def detect_emotion_from_webcam():
    # Check if we're in a server environment (like Render)
    is_server = os.environ.get('IS_SERVER', 'False').lower() == 'true'
    
    # If we're in a server environment, use mock mode
    if is_server:
        return mock_emotion_detection()
    
    # Otherwise try to use the webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return {"error": "Failed to access webcam"}

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        dominant_emotion = result[0]['dominant_emotion']
        return {"emotion": dominant_emotion}
    except Exception as e:
        return {"error": str(e)}

def mock_emotion_detection():
    # Return a random emotion for testing
    emotions = ["happy", "sad", "angry", "surprised", "neutral", "fearful", "disgusted"]
    random_emotion = random.choice(emotions)
    return {"emotion": random_emotion}