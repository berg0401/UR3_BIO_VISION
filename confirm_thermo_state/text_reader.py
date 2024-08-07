from google.cloud import vision
from os import environ,path
from image_fetcher import ImageFetcher
from thermo_state_initializer import ThermoStateInitializer
from cv2 import imdecode, IMREAD_COLOR, imshow, waitKey, destroyAllWindows
from numpy import frombuffer, uint8
from image_encoder import ImageEncoder

class TextReader:
    def __init__(self):
        #connect to API with json key
        script_dir = path.dirname(path.abspath(__file__))
        environ['GOOGLE_APPLICATION_CREDENTIALS'] = path.join(script_dir, r"../path_to_your_json_key")
        self.client = vision.ImageAnnotatorClient()
        thermo_state_initializer = ThermoStateInitializer()
        self.thermo_states = thermo_state_initializer.init_state_options()
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

    def guess_menu(self,texts):
        for thermo_state in self.thermo_states:
            for feature in thermo_state.features:
                for text in texts:
                    if feature.word == text.description:
                        correct_left_top_corner_x = feature.location.left_top_corner[0]
                        correct_left_top_corner_y = feature.location.left_top_corner[1]
                        guessed_left_top_corner_x = text.bounding_poly.vertices[2].x
                        guessed_left_top_corner_y = text.bounding_poly.vertices[2].y
                        correct_right_bottom_corner_x = feature.location.right_bottom_corner[0]
                        correct_right_bottom_corner_y = feature.location.right_bottom_corner[1]
                        guessed_right_bottom_corner_x = text.bounding_poly.vertices[0].x
                        guessed_right_bottom_corner_y = text.bounding_poly.vertices[0].y
                        if guessed_left_top_corner_x >= correct_left_top_corner_x and guessed_left_top_corner_y >= correct_left_top_corner_y and guessed_right_bottom_corner_x <= correct_right_bottom_corner_x and guessed_right_bottom_corner_y <= correct_right_bottom_corner_y:
                            return thermo_state.name
    def show_result(self,thermo_state):
        print(f"{thermo_state}\n")




if __name__ == '__main__':
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir, r"..\state_menu_demo_images")
    ImageFetcher = ImageFetcher(images_folder)
    images = ImageFetcher.fetch()
    image_encoder = ImageEncoder()
    images_content = image_encoder.encode(images)

    text_reader = TextReader()
    for content in images_content:
        texts = text_reader.read(content)
        state_menu = text_reader.guess_menu(texts)
        text_reader.show_result(state_menu)
        text_reader.show_image(content)





