# Task 3 - Image Captioning

## Overview

This project implements an AI-based image captioning system that automatically generates a natural-language description for an input image.

The project combines **Computer Vision** and **Natural Language Processing (NLP)** using a pretrained **BLIP (Bootstrapped Language-Image Pretraining)** vision-language transformer model.

The model analyzes the visual content of an image and generates a meaningful text caption describing the image.

## Objectives

- Generate captions automatically from images.
- Combine computer vision and natural language processing.
- Use a pretrained transformer-based image captioning model.
- Process an input image and generate a natural-language description.
- Demonstrate an end-to-end AI image captioning pipeline.

## Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- BLIP Image Captioning Model
- Pillow (PIL)

## Project Structure

```text
Task-3-Image-Captioning/
│
├── images/
│   └── test.jpg
│
├── caption_image.py
├── requirements.txt
├── .gitignore
└── README.md