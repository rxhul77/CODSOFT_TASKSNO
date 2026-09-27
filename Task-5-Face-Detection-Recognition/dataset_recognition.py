import cv2
import os

MODEL_PATH = "face_model.yml"
TEST_FOLDER = "test_images"

# Load trained LBPH model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(MODEL_PATH)

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

    # Load image directly as grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print(f"Could not load: {filename}")
        continue

    # Recognize the already-cropped face
    label, confidence = recognizer.predict(image)

    if confidence < 70:
        name = f"Person {label}"
    else:
        name = "Unknown"

    print("\n----------------------------")
    print(f"Image: {filename}")
    print(f"Prediction: {name}")
    print(f"Confidence: {confidence:.2f}")

    # Convert grayscale to BGR for displaying text
    display_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    cv2.putText(
        display_image,
        name,
        (5, 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 255, 0),
        1
    )

    cv2.imshow("LBPH Face Recognition", display_image)

    print("Press any key for the next image...")
    cv2.waitKey(0)

cv2.destroyAllWindows()

print("\nRecognition demo completed!")