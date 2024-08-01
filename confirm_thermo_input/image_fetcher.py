from os import path, listdir
from cv2 import imread, imshow, waitKey, IMREAD_GRAYSCALE

class ImageFetcher:
    def __init__(self,images_folder):
        self.images_folder = images_folder

    def fetch(self):
        images = []
        images_name = [f for f in listdir(self.images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        for image_name in images_name:
            img_path = path.join(self.images_folder, image_name)
            image = imread(img_path, IMREAD_GRAYSCALE)
            images.append(image)
        return images

    def show_images(self, images):
        for image in images:
            imshow('image', image)
            waitKey(0)

if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir,r"..\input_thermo_demo_images\spot\ex1")
    image_fetcher = ImageFetcher(images_folder)
    image_content = image_fetcher.fetch()
    image_fetcher.show_images(image_content)