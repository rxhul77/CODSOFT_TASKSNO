import cv2

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")

# Load a known face from the dataset
image_path = "dataset/olivetti_faces/s1/1.jpg"

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Could not load image.")
    exit()

# Recognize the face
label, confidence = recognizer.predict(image)

print("Recognition Result")
print("------------------")
print(f"Predicted person: s{label}")
print(f"Confidence value: {confidence:.2f}")

if confidence < 70:
    print(f"Recognized as: Person {label}")
else:
    print("Unknown person")

# Display image
cv2.imshow("Recognition Test", image)
cv2.waitKey(0)
cv2.destroyAllWindows()