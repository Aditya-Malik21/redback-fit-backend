import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import argparse
import cv2

# Initialize argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the input image")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["image"])
if image is None:
    print("Could not open or find the image.")
    exit()

# Convert the image to RGB (pytesseract expects an RGB image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)