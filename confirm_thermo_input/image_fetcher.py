from os import path, listdir
from cv2 import imread, imencode
import cv2
from robot_position import RobotPosition

class ImageFetcher:
    def __init__(self,images_folder):
        self.images_folder = images_folder

    def fetch(self,robot_position_name):
        images_content = []
        images_name = [f for f in listdir(self.images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        for image_name in images_name:
            img_path = path.join(self.images_folder, image_name)
            cv2_img = imread(img_path)
            cropped_img = self.crop(cv2_img,robot_position_name)
            success, encoded_image = imencode('.jpg', cropped_img)
            if success:
                images_content.append(encoded_image.tobytes())
        return images_content

    def crop(self,image,robot_position_name):
        robot_position = RobotPosition(robot_position_name)
        top= robot_position.top_crop
        bottom = robot_position.bottom_crop
        left = robot_position.left_crop
        right = robot_position.right_crop
        cropped_image = image[top:image.shape[0] - bottom, left:image.shape[1] - right]
        angle = 180

        # Get the dimensions of the image
        height, width = cropped_image.shape[:2]

        # Calculate the rotation matrix
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

        # Perform the rotation using cv2.warpAffine
        rotated_image = cv2.warpAffine(cropped_image, rotation_matrix, (width, height))

        return rotated_image

if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir,r"..\key_board_images")
    image_fetcher = ImageFetcher(images_folder)
    image_content = image_fetcher.fetch()
