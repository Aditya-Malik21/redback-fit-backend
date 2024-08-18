import os
import io
from google.cloud import vision
import pandas as pd

# Set the environment variable for the Google Application Credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

# Initialize the Vision API client
client = vision.ImageAnnotatorClient()

# def detectText(content):
#     # Create an Image object using the content
#     image = vision.Image(content=content)

#     # Perform text detection on the image
#     response = client.text_detection(image=image)
    
#     # Extract text annotations
#     texts = response.text_annotations

#     # Print the full response (optional)
#     # print(response)

#     # Create a DataFrame from the text annotations
#     df = pd.DataFrame([{
#         'locale': text.locale if hasattr(text, 'locale') else '',
#         'description': text.description
#     } for text in texts])

#     # Display the first detected description (assumed to be the most relevant text)
#     if not df.empty:
#         print(df['description'][0])
#     else:
#         print("No text detected.")

# # File and folder paths
# FILE_NAME = 'road-sign.png'
# FOLDER_PATH = r'C:\Users\chees\OCR\VisionAPIDemo\Images'

# # Load the image from file
# with io.open(os.path.join(FOLDER_PATH, FILE_NAME), 'rb') as image_file:
#     content = image_file.read()

# # Call the function to detect text
# detectText(content)

img_url = 'https://live.staticflickr.com/58/161344773_aa70ab71fa_z_d.jpg'
# Create an Image object using the image URI
image = vision.Image()
image.source.image_uri = img_url

# Perform text detection on the image
response = client.text_detection(image=image)

# Extract text annotations
texts = response.text_annotations

# Print the full response (optional)
# print(response)

# Create a DataFrame from the text annotations
df = pd.DataFrame([{
'locale': text.locale if hasattr(text, 'locale') else '',
'description': text.description
} for text in texts])

print(df['description'][0])