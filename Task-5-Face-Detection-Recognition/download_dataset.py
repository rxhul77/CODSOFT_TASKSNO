from sklearn.datasets import fetch_olivetti_faces
import cv2
import os

print("Downloading Olivetti Faces dataset...")

faces = fetch_olivetti_faces(
    data_home="./dataset",
    download_if_missing=True
)

output_dir = "./dataset/olivetti_faces"
os.makedirs(output_dir, exist_ok=True)

for i, (image, label) in enumerate(zip(faces.images, faces.target)):
    person_dir = os.path.join(output_dir, f"s{label + 1}")
    os.makedirs(person_dir, exist_ok=True)

    image_uint8 = (image * 255).astype("uint8")

    filename = os.path.join(
        person_dir,
        f"{i + 1}.jpg"
    )

    cv2.imwrite(filename, image_uint8)

print("\nDataset downloaded successfully!")
print(f"Total images: {len(faces.images)}")
print(f"Total people: {len(set(faces.target))}")
print(f"Saved to: {output_dir}")