from os import path
from cv2 import imencode, warpAffine, getRotationMatrix2D
from image_fetcher import ImageFetcher
from numpy import zeros, uint8
class ImageEncoder:
    def __init__(self):
        pass
    def encode(self,images):
        keyboard_images = []
        image_content = []
        for image in images:
            cropped_img = self.crop(image)
            rotated_img = self.rotate(cropped_img)
            keyboard_images.append(rotated_img)
        combined_image = self.combine_images(keyboard_images)
        success, encoded_image = imencode('.jpg', combined_image)
        if success:
            image_content.append(encoded_image.tobytes())
        return image_content

    def crop(self, image):
        top = 600
        bottom = 455
        left = 860
        right = 855

        cropped_image = image[top:image.shape[0] - bottom, left:image.shape[1] - right]
        return cropped_image

    def rotate(self,image):
        angle = 180
        height, width = image.shape[:2]
        rotation_matrix = getRotationMatrix2D((width / 2, height / 2), angle, 1)
        rotated_image = warpAffine(image, rotation_matrix, (width, height))
        return rotated_image

    def combine_images(self, cropped_images):
        final_image = zeros(cropped_images[0].shape, dtype=uint8)
        for x in range(cropped_images[0].shape[0]):
            for y in range(cropped_images[0].shape[1]):
                max_value = 0
                for cropped_image in cropped_images:
                    value = cropped_image[x][y]
                    if value > max_value:
                        max_value = value
                final_image[x][y] = max_value
        return final_image




# if __name__ == "__main__":
#     script_dir = path.dirname(path.abspath(__file__))
#     images_folder = path.join(script_dir,r"..\keyboard_images\spot\custom_light")
#     image_fetcher = ImageFetcher(images_folder)
#     images = image_fetcher.fetch()
#     image_encoder = ImageEncoder('default')