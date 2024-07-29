from google.cloud import vision
from os import path, listdir, makedirs, environ
import cv2

script_dir = path.dirname(path.abspath(__file__))
environ['GOOGLE_APPLICATION_CREDENTIALS'] = path.join(script_dir,"../quixotic-tesla-429014-k0-b26b43f8ede2.json")
client = vision.ImageAnnotatorClient()
images_folder = path.join(script_dir,"../image_ecran_test_unitaire")

images_name = [f for f in listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
for image_name in images_name:
    img_path = path.join(images_folder, image_name)
    with open(img_path,"rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("===========================================\n")
    print("Text:\n")

    for text in texts:
        print(text)

    image_shown = cv2.imread(img_path)
    cv2.imshow('original', image_shown)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
