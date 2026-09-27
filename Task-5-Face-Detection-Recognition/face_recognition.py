import cv2
import os
import numpy as np

# ==============================
# CONFIGURATION
# ==============================

DATASET_PATH = "dataset/att_faces"
MODEL_PATH = "face_model.yml"

# ==============================
# CREATE LBPH RECOGNIZER
# ==============================

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []

print("========================================")
print("   FACE RECOGNITION MODEL TRAINING")
print("========================================")
print()

# ==============================
# LOAD DATASET
# ==============================

if not os.path.exists(DATASET_PATH):
    print(f"Error: Dataset not found at {DATASET_PATH}")
    exit()

print("Loading dataset...")

for subject_folder in sorted(os.listdir(DATASET_PATH)):

    subject_path = os.path.join(DATASET_PATH, subject_folder)

    # Skip files
    if not os.path.isdir(subject_path):
        continue

    # Convert s1 -> 1, s2 -> 2, etc.
    try:
        label = int(subject_folder.replace("s", ""))
    except ValueError:
        continue

    print(f"Loading {subject_folder}...")

    for image_name in sorted(os.listdir(subject_path)):

        image_path = os.path.join(subject_path, image_name)

        # Read image directly as grayscale
        image = cv2.imread(
            image_path,
            cv2.IMREAD_GRAYSCALE
        )

        if image is None:
            print(f"  Could not read: {image_name}")
            continue

        # Add image directly to training data
        faces.append(image)
        labels.append(label)

# ==============================
# CHECK TRAINING DATA
# ==============================

print()
print(f"Total training images: {len(faces)}")

if len(faces) == 0:
    print("Error: No training images were loaded.")
    exit()

# Convert labels to NumPy array
labels = np.array(labels)

# ==============================
# TRAIN MODEL
# ==============================

print()
print("Training LBPH face recognition model...")

recognizer.train(faces, labels)

# ==============================
# SAVE MODEL
# ==============================

recognizer.write(MODEL_PATH)

print()
print("========================================")
print("       TRAINING COMPLETED")
print("========================================")
print(f"Training images: {len(faces)}")
print(f"Number of people: {len(set(labels))}")
print(f"Model saved as: {MODEL_PATH}")
print()