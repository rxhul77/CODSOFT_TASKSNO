import cv2
import os
import numpy as np

# Dataset path
dataset_path = "dataset/olivetti_faces"

# Store training images and corresponding labels
faces = []
labels = []

print("Loading dataset...")

# 40 people: s1 to s40
for label in range(1, 41):

    person_folder = os.path.join(dataset_path, f"s{label}")

    if not os.path.exists(person_folder):
        print(f"Warning: {person_folder} not found")
        continue

    for filename in os.listdir(person_folder):

        image_path = os.path.join(person_folder, filename)

        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            continue

        faces.append(image)
        labels.append(label)

print(f"Total training images: {len(faces)}")
print(f"Total labels: {len(labels)}")

if len(faces) == 0:
    print("No images found. Check the dataset path.")
    exit()

# Convert labels to NumPy array
labels = np.array(labels)

# Create LBPH Face Recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

print("Training LBPH face recognition model...")

recognizer.train(faces, labels)

# Save trained model
model_path = "face_model.yml"
recognizer.write(model_path)

print("\nTraining completed successfully!")
print(f"Model saved as: {model_path}")