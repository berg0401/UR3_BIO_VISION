from google.cloud import vision
from os import environ,path
from image_fetcher import ImageFetcher
from image_encoder import ImageEncoder
from cv2 import imdecode, IMREAD_COLOR, imshow, waitKey, destroyAllWindows
from numpy import frombuffer, uint8

class TextReader:
    def __init__(self):
        #connect to API with json key
        script_dir = path.dirname(path.abspath(__file__))
        environ['GOOGLE_APPLICATION_CREDENTIALS'] = path.join(script_dir, r"../path_to_json")
        self.client = vision.ImageAnnotatorClient()

    def read(self,image_content):
        image = vision.Image(content=image_content)
        response = self.client.text_detection(image=image)
        texts = response.text_annotations
        return texts
    def show_image(self,image_content):
        nparr = frombuffer(image_content, uint8)
        image = imdecode(nparr, IMREAD_COLOR)
        imshow('Image', image)
        waitKey(0)
        destroyAllWindows()
    def show_result(self,texts):
        if len(texts) != 0:
            print(texts[1].description)
        else:
            print("Can't detect any texts")


if __name__ == '__main__':
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir,r"..\input_thermo_demo_images\ex4")
    ImageFetcher = ImageFetcher(images_folder)
    images = ImageFetcher.fetch()
    image_encoder = ImageEncoder()
    images_content = image_encoder.encode(images)
    text_reader = TextReader()
    for content in images_content:
        texts = text_reader.read(content)
        text_reader.show_result(texts)
        text_reader.show_image(content)
