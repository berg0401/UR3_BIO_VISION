from google.cloud import vision
from os import environ,path
from image_fetcher import ImageFetcher
from thermo_state_initializer import ThermoStateInitializer
from cv2 import imdecode, IMREAD_COLOR, imshow, waitKey, destroyAllWindows
from numpy import frombuffer, uint8

class AnswerCreater:
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
        print(texts)
        return texts
    def show_image(self,image_content):
        nparr = frombuffer(image_content, uint8)
        image = imdecode(nparr, IMREAD_COLOR)
        imshow('Image', image)
        waitKey(0)
        destroyAllWindows()
    def writeFile(self,texts):
        file_path = r"C:\Users\15142\OneDrive - USherbrooke\S7\STAGE-T5\UR5_BIO_VISION\images_ecran\Pen_position\answers.txt"
        with open(file_path, 'w', encoding='utf-8') as file:
            for text in texts:
                right_bottom_corner_x = text.bounding_poly.vertices[0].x
                right_bottom_corner_y = text.bounding_poly.vertices[0].y
                left_top_corner_x = text.bounding_poly.vertices[2].x
                left_top_corner_y = text.bounding_poly.vertices[2].y
                word = text.description
                code = f"warning_pop.add_feature(word='{word}', location=Location(left_top_corner=({left_top_corner_x-10},{left_top_corner_y-10}),right_bottom_corner=({right_bottom_corner_x+10},{right_bottom_corner_y+10})))\n"
                file.write(code)




if __name__ == '__main__':
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir, r"..\image_ecran_test_unitaire")
    ImageFetcher = ImageFetcher(images_folder)
    images_content = ImageFetcher.fetch()
    text_reader = AnswerCreater()
    for content in images_content:
        texts = text_reader.read(content)
        texts = text_reader.writeFile(texts)





