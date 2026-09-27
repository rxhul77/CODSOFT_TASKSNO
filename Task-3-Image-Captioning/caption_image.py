import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import torch
import torchvision.models as models
from torchvision import transforms
from transformers import BlipProcessor, BlipForConditionalGeneration
# ============================================================
# CONFIGURATION
# ============================================================
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
BLIP_MODEL = "Salesforce/blip-image-captioning-base"
# ============================================================
# LOAD RESNET-50
# ============================================================
print("=" * 60)
print("             IMAGE CAPTIONING AI")
print("=" * 60)
print("\nArchitecture:")
print("Image")
print("  ↓")
print("Pre-trained ResNet-50")
print("  ↓")
print("Image Features")
print("  ↓")
print("Pre-trained BLIP Caption Generator")
print("  ↓")
print("Generated Caption")
print(f"\nUsing device: {DEVICE}")
print("\nLoading ResNet-50...")
resnet = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
# Remove classification layer
resnet = torch.nn.Sequential(*list(resnet.children())[:-1])

resnet = resnet.to(DEVICE)
resnet.eval()

print("ResNet-50 loaded successfully.")
# ============================================================
# RESNET PREPROCESSING
# ============================================================
resnet_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])
# ============================================================
# EXTRACT RESNET FEATURES
# ============================================================
def extract_resnet_features(image):

    image_tensor = resnet_transform(image)
    image_tensor = image_tensor.unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        features = resnet(image_tensor)

    features = features.view(features.size(0), -1)

    return features
# ============================================================
# LOAD BLIP
# ============================================================
print("\nLoading pretrained captioning model...")

processor = BlipProcessor.from_pretrained(BLIP_MODEL)
caption_model = BlipForConditionalGeneration.from_pretrained(
    BLIP_MODEL
)
caption_model = caption_model.to(DEVICE)
caption_model.eval()

print("Captioning model loaded successfully.")
# ============================================================
# GENERATE CAPTION
# ============================================================
def generate_caption(image):

    inputs = processor(
        images=image,
        return_tensors="pt"
    )

    inputs = {
        key: value.to(DEVICE)
        for key, value in inputs.items()
    }

    with torch.no_grad():

        output = caption_model.generate(
            **inputs,
            max_new_tokens=30
        )

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption
# ============================================================
# GUI
# ============================================================
root = tk.Tk()
root.title("AI Image Captioning")
root.geometry("850x700")
root.configure(bg="#f5f5f5")
# ============================================================
# TITLE
# ============================================================
title = tk.Label(
    root,
    text="AI IMAGE CAPTIONING",
    font=("Arial", 26, "bold"),
    bg="#f5f5f5"
)
title.pack(pady=(25, 5))
subtitle = tk.Label(
    root,
    text="Computer Vision + Natural Language Processing",
    font=("Arial", 13),
    bg="#f5f5f5"
)
subtitle.pack()
architecture = tk.Label(
    root,
    text="Image → ResNet-50 → Feature Extraction → BLIP → Caption",
    font=("Arial", 11),
    bg="#f5f5f5"
)
architecture.pack(pady=10)
# ============================================================
# IMAGE DISPLAY
# ============================================================
image_label = tk.Label(
    root,
    text="No image selected",
    width=60,
    height=18,
    bg="white",
    relief="solid",
    borderwidth=1
)
image_label.pack(pady=15)
# ============================================================
# CAPTION LABEL
# ============================================================
caption_title = tk.Label(
    root,
    text="Generated Caption:",
    font=("Arial", 15, "bold"),
    bg="#f5f5f5"
)
caption_title.pack(pady=(10, 5))
caption_label = tk.Label(
    root,
    text="Select an image to generate a caption",
    font=("Arial", 14),
    wraplength=700,
    bg="#f5f5f5"
)
caption_label.pack(pady=5)
# ============================================================
# STATUS
# ============================================================
status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 10),
    bg="#f5f5f5"
)
status_label.pack(pady=5)
# ============================================================
# SELECT IMAGE
# ============================================================
def select_image():

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png *.webp"),
            ("JPG Files", "*.jpg"),
            ("PNG Files", "*.png")
        ]
    )

    if not file_path:
        return

    try:

        status_label.config(
            text="Loading image..."
        )

        root.update()

        image = Image.open(file_path).convert("RGB")

        # Display image
        display_image = image.copy()
        display_image.thumbnail((600, 350))

        photo = ImageTk.PhotoImage(display_image)

        image_label.config(
            image=photo,
            text=""
        )

        image_label.image = photo

        # ----------------------------------------------------
        # ResNet feature extraction
        # ----------------------------------------------------

        status_label.config(
            text="Extracting ResNet-50 image features..."
        )

        root.update()

        features = extract_resnet_features(image)

        print("\nImage selected:")
        print(file_path)

        print("\nResNet feature vector:")
        print(features.shape)

        # ----------------------------------------------------
        # Caption generation
        # ----------------------------------------------------

        status_label.config(
            text="Generating caption..."
        )

        root.update()

        caption = generate_caption(image)

        caption_label.config(
            text=f'"{caption}"'
        )

        status_label.config(
            text="Caption generated successfully!"
        )
    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

        status_label.config(
            text="Error occurred"
        )
# ============================================================
# BUTTON
# ============================================================
select_button = tk.Button(
    root,
    text="SELECT IMAGE & GENERATE CAPTION",
    command=select_image,
    font=("Arial", 13, "bold"),
    padx=20,
    pady=10
)
select_button.pack(pady=20)
# ============================================================
# FOOTER
# ============================================================
footer = tk.Label(
    root,
    text="CodSoft AI Image Captioning Project",
    font=("Arial", 9),
    bg="#f5f5f5"
)
footer.pack(side="bottom", pady=10)
# ============================================================
# START GUI
# ============================================================
root.mainloop()