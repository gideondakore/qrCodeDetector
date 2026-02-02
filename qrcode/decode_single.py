from qreader import QReader
import cv2
import os


# Create a QReader instance
qreader = QReader()

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "assets", "card_national.jpg")

# Verify file exists
if not os.path.exists(image_path):
    print(f"File not found: {image_path}")
    exit(1)

image = cv2.imread(image_path)
if image is None:
    print("Failed to load image")
    exit(1)

# Get the image that contains the QR code
# image = cv2.cvtColor(cv2.imread("assets/qr.png"), cv2.COLOR_BGR2RGB)

# Use the detect_and_decode function to get the decoded QR data
decoded_text = qreader.detect_and_decode(image=image)
print("Decoded QR Data:", decoded_text)