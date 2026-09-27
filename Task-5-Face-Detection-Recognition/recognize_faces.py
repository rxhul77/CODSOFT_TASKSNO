import cv2
import os

# Load trained LBPH model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")

# Load Haar Cascade face detector
cascade_path = "haarcascade/haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(cascade_path)

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Face recognition started.")
print("Press Q to quit.")

while True:

    ret, frame = camera.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    detected_faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(60, 60)
    )

    for (x, y, w, h) in detected_faces:

        # Extract face
        face = gray[y:y+h, x:x+w]

        # Recognize face
        label, confidence = recognizer.predict(face)

        # LBPH confidence: lower = better match
        if confidence < 70:
            name = f"Person {label}"
        else:
            name = "Unknown"

        # Draw rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Display name
        cv2.putText(
            frame,
            name,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    # Display camera
    cv2.imshow("Face Detection and Recognition", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()