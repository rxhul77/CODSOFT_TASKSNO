import cv2
import os

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")

# Image to test
image_path = "dataset/olivetti_faces/s1/1.jpg"

# Load image
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load Haar Cascade
cascade_path = "haarcascade/haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(cascade_path)

# Detect faces
faces = face_detector.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

print(f"Faces detected: {len(faces)}")

for (x, y, w, h) in faces:

    face = gray[y:y+h, x:x+w]

    label, confidence = recognizer.predict(face)

    if confidence < 70:
        name = f"Person {label}"
    else:
        name = "Unknown"

    print(f"Prediction: {name}")
    print(f"Confidence: {confidence:.2f}")

    # Draw detection box
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    # Display name
    cv2.putText(
        image,
        name,
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

# Display result
cv2.imshow("Face Detection and Recognition", image)

print("Press any key to close.")

cv2.waitKey(0)
cv2.destroyAllWindows()