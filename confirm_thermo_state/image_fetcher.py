from os import path, listdir
from cv2 import imread, imencode

class ImageFetcher:
    def __init__(self,images_folder):
        self.images_folder = images_folder

    def fetch(self):
        images_content = []
        images_name = [f for f in listdir(self.images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        for image_name in images_name:
            cv2_img = self.get_image(image_name)
            cropped_img = self.crop(cv2_img)
            self.encode_image(cropped_img,images_content)
        return images_content

    def crop(self,image):
        top_bottom = 200
        left_right = 600
        cropped_image = image[top_bottom:image.shape[0] - top_bottom, left_right:image.shape[1] - left_right]
        return cropped_image
    def encode_image(self,img,images_content):
        success, encoded_image = imencode('.jpg', img)
        if success:
            images_content.append(encoded_image.tobytes())

    def get_image(self, image_name):
        img_path = path.join(self.images_folder, image_name)
        cv2_img = imread(img_path)
        return cv2_img

if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir,r"..\images_ecran")
    image_fetcher = ImageFetcher(images_folder)
    image_content = image_fetcher.fetch()
