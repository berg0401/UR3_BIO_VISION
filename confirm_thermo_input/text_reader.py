from google.cloud import vision
from os import environ,path
from image_fetcher import ImageFetcher
from image_fetcher_combiner import ImageFetcherCombiner
from cv2 import imdecode, IMREAD_COLOR, imshow, waitKey, destroyAllWindows
from numpy import frombuffer, uint8

class TextReader:
    def __init__(self):
        #connect to API with json key
        script_dir = path.dirname(path.abspath(__file__))
        environ['GOOGLE_APPLICATION_CREDENTIALS'] = path.join(script_dir, r"../quixotic-tesla-429014-k0-b26b43f8ede2.json")
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


if __name__ == '__main__':
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir,r"..\keyboard_images\spot\multiple_pics\1278")
    ImageFetcher = ImageFetcherCombiner(images_folder)
    images_content = ImageFetcher.fetch('spot')
    text_reader = TextReader()
    for content in images_content:
        texts = text_reader.read(content)
        print(texts[1].description)
        text_reader.show_image(content)