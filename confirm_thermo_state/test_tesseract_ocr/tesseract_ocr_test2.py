import cv2
import pytesseract
from pytesseract import Output
from PIL import Image
# Configure pytesseract path if needed
# pytesseract.pytesseract.tesseract_cmd = r'path\to\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def process_image(image_path):
    # Load the image using OpenCV
    img = cv2.imread(image_path)
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY)
    cv2.imshow('thresh', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Perform OCR with pytesseract
    # Output the data in dict format
    d = pytesseract.image_to_data(thresh, output_type=Output.DICT)

    # Number of boxes
    n_boxes = len(d['text'])

    # Loop through each detected text component
    for i in range(n_boxes):
        text = d['text'][i]
        if text.strip() != "":
            # Get the bounding box coordinates
            x, y, w, h = d['left'][i], d['top'][i], d['width'][i], d['height'][i]
            # Draw a rectangle around detected text
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Print text information
            print(f"Box[{i}]: x={x}, y={y}, w={w}, h={h}, text: {text}")

    # Display the result
    cv2.imshow('Text Detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Path to your image file
image_path = r"C:\Users\15142\OneDrive - USherbrooke\S7\STAGE-T5\VISION\IMAGE_TEST\keyboard\big.png"
process_image(image_path)