import cv2
import os

MODEL_PATH = "face_model.yml"
TEST_FOLDER = "test_images"
CASCADE_PATH = "haarcascade/haarcascade_frontalface_default.xml"

# Load model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(MODEL_PATH)

# Load Haar Cascade
face_detector = cv2.CascadeClassifier(CASCADE_PATH)

if face_detector.empty():
    print("Error: Haar Cascade could not be loaded.")
    exit()

# Get test images
images = [
    file for file in os.listdir(TEST_FOLDER)
    if file.lower().endswith((".jpg", ".jpeg", ".png"))
]

if not images:
    print("No test images found.")
    exit()

print(f"Found {len(images)} test images.")

for filename in images:

    image_path = os.path.join(TEST_FOLDER, filename)
    image = cv2.imread(image_path)

    if image is None:
        print(f"Could not load: {filename}")
        continue

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    print(f"\nImage: {filename}")
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

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            image,
            name,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("CodSoft Task 5 - Face Recognition", image)

    print("Press any key for the next image...")
    cv2.waitKey(0)

cv2.destroyAllWindows()

print("\nDemo completed successfully!")