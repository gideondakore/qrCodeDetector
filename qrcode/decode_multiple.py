from qreader import QReader
from cv2 import QRCodeDetector, imread
from pyzbar.pyzbar import decode
import os

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, "assets")

# Initialize readers
qreader_reader, cv2_reader, pyzbar_reader = QReader(), QRCodeDetector(), decode

image_files = (
    'card_national.jpg', 'card2.png', 'qr.png', 'qr2.png', 
    'qr3.png', 'qr4.png', 'voters_blur.png', 'voters1.jpeg', 
    'voters2.jpg', 'votters_id.jpg',
    'amalilaptop.jpg', 'basitv.jpg', 'basitv2.jpg',
    'bar.png', 'bar2.png'

)

for img_name in image_files:
    img_path = os.path.join(assets_dir, img_name)
    
    # Check if file exists
    if not os.path.exists(img_path):
        print(f"File not found: {img_path}")
        continue
    
    img = imread(img_path)
    if img is None:
        print(f"Failed to load: {img_path}")
        continue

    # Decode with all three readers
    qreader_out = qreader_reader.detect_and_decode(image=img)
    pyzbar_out = pyzbar_reader(image=img)
    cv2_out = cv2_reader.detectAndDecode(img=img)[0]

    print(f"Image: {img_name}")
    print(f"  QReader: {qreader_out}")
    print(f"  OpenCV:  {cv2_out}")
    print(f"  pyzbar:  {pyzbar_out}")
    print()
