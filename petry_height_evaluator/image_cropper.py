from cv2 import imshow, waitKey, destroyAllWindows, imwrite
from os import path, makedirs
from image_fetcher import ImageFetcher
import random

class ImageCropper:
    def __init__(self,top_bottom,left_right):
        self.top_bottom = top_bottom
        self.left_right = left_right
        self.cropped_image = None

    def crop(self,image):
        height, width = image.shape[:2]
        cropped_image = image[self.top_bottom:height - self.top_bottom, self.left_right:width - self.left_right]
        return cropped_image

    def show_image(self, image):
        imshow("Original Image", image)
        waitKey(0)
        destroyAllWindows()

    def save_image(self, image, folder):
        cropped_folder = path.join(folder, 'cropped')
        # Create the 'cropped' folder if it doesn't exist
        if not path.exists(cropped_folder):
            makedirs(cropped_folder)
        img_path = path.join(cropped_folder, f"{random.randint(0, 100)}.png")
        imwrite(img_path, image)


if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir, r"..\agar_height_evaluator_demo_images")
    image_fetcher = ImageFetcher(images_folder)
    images = image_fetcher.fetch()
    top_bottom = 380
    left_right = 600
    app = ImageCropper(top_bottom, left_right)
    for image in images:
        cropped_image = app.crop(image)
        app.show_image(cropped_image)
        # app.save_image(image,images_folder)
