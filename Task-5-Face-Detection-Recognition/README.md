# Face Detection and Recognition

## 📌 Project Overview

This project implements a face detection and face recognition system using Python and OpenCV.

The system can:
- Detect faces using the Haar Cascade classifier.
- Recognize faces using the LBPH (Local Binary Patterns Histograms) face recognition algorithm.
- Recognize faces from individual images.
- Recognize faces from a prepared test dataset.
- Perform real-time face detection and recognition using a webcam.

This project was developed as part of the **CodSoft Artificial Intelligence Internship – Task 5**.

---

## 🎯 Objectives

- Implement face detection using OpenCV.
- Implement face recognition using LBPH.
- Train a face recognition model using a facial image dataset.
- Test recognition on unseen images.
- Implement real-time face recognition using a webcam.
- Understand the practical workflow of a computer vision recognition system.

---

## 🛠️ Technologies Used

- Python 3.10
- OpenCV
- OpenCV-Contrib
- NumPy
- Scikit-learn
- Haar Cascade Classifier
- LBPH Face Recognizer

---

## 📂 Dataset

The project uses the **Olivetti Faces dataset**, containing:

- 400 facial images
- 40 different individuals
- 10 images per individual
- Image size: 64 × 64 pixels
- Grayscale facial images

The dataset is downloaded automatically using Scikit-learn.

The dataset itself is excluded from the GitHub repository using `.gitignore`.

---

## 📁 Project Structure

```text
Task-5-Face-Detection-Recognition/
│
├── haarcascade/
│   └── haarcascade_frontalface_default.xml
│
├── test_images/
│   ├── 191.jpg
│   ├── 293.jpg
│   ├── 392.jpg
│   └── 94.jpg
│
├── dataset_recognition.py
├── demo.py
├── download_dataset.py
├── face_recognition.py
├── recognize_faces.py
├── recognize_image.py
├── test_recognition.py
├── train_model.py
├── requirements.txt
├── .gitignore
└── README.md