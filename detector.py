import cv2
from deepface import DeepFace

def detect_emotion_from_webcam():
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
