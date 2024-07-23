from os import path, listdir
from cv2 import imread, imencode, IMREAD_GRAYSCALE, warpAffine, getRotationMatrix2D
from robot_position import RobotPosition
from numpy import zeros, uint8

class ImageFetcherCombiner:
    def __init__(self,images_folder):
        self.images_folder = images_folder

    def fetch(self,robot_position_name):
        images_content = []
        cropped_images= []
        images_name = [f for f in listdir(self.images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        for image_name in images_name:
            cv2_img = self.get_image(image_name)
            cropped_img = self.crop_rotate(cv2_img,robot_position_name)
            cropped_images.append(cropped_img)
        combined_image = self.combine_images(cropped_images)
        self.encode_image(combined_image,images_content)
        return images_content


    def get_image(self, image_name):
        img_path = path.join(self.images_folder, image_name)
        cv2_img = imread(img_path, IMREAD_GRAYSCALE)
        return cv2_img
    def crop_rotate(self,image,robot_position_name):
        robot_position = RobotPosition(robot_position_name)

        top= robot_position.top_crop
        bottom = robot_position.bottom_crop
        left = robot_position.left_crop
        right = robot_position.right_crop

        cropped_image = image[top:image.shape[0] - bottom, left:image.shape[1] - right]
        angle = 180
        height, width = cropped_image.shape[:2]
        rotation_matrix = getRotationMatrix2D((width / 2, height / 2), angle, 1)
        rotated_image = warpAffine(cropped_image, rotation_matrix, (width, height))
        return rotated_image

    def combine_images(self,cropped_images):
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

    def encode_image(self,image,images_content):
        success, encoded_image = imencode('.jpg', image)
        if success:
            images_content.append(encoded_image.tobytes())

if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir,r"..\keyboard_images\spot\custom_light")
    image_fetcher = ImageFetcherCombiner(images_folder)
    image_content = image_fetcher.fetch('spot')
