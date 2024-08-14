from os import path, listdir
from cv2 import imread, imshow,waitKey

class ImageFetcher:
    def __init__(self,images_folder):
        self.images_folder = images_folder

    def fetch(self):
        images = []
        images_name = [f for f in listdir(self.images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        for image_name in images_name:
            img = self.get_image(image_name)
            images.append(img)
        return images

    def get_image(self, image_name):
        img_path = path.join(self.images_folder, image_name)
        cv2_img = imread(img_path)
        return cv2_img

    def show_images(self,images):
        for image in images:
            imshow('image',image)
            waitKey(0)

if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir,r"..\agar_height_evaluator_demo_images")
    image_fetcher = ImageFetcher(images_folder)
    images = image_fetcher.fetch()
    image_fetcher.show_images(images)
