from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


MODEL_NAME = "Salesforce/blip-image-captioning-base"
IMAGE_PATH = "images/test.jpg"


def generate_caption(image_path):
    print("Loading image captioning model...")

    processor = BlipProcessor.from_pretrained(MODEL_NAME)
    model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME)

    image = Image.open(image_path).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")

    output = model.generate(
        **inputs,
        max_new_tokens=30
    )

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption


def main():
    print("=" * 55)
    print("             AI IMAGE CAPTIONING")
    print("=" * 55)

    try:
        caption = generate_caption(IMAGE_PATH)

        print("\nGenerated Caption:")
        print(caption)

    except FileNotFoundError:
        print(f"\nImage not found: {IMAGE_PATH}")
        print("Please place your image inside the images folder.")

    except Exception as error:
        print(f"\nAn error occurred: {error}")


if __name__ == "__main__":
    main()