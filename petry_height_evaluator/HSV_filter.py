import cv2
from numpy import array
from os import path, makedirs
from image_cropper import ImageCropper
from image_fetcher import ImageFetcher
import random

class HSVFilter:
    def __init__(self, virtual_aperture):
        self.lower_red1 = array([0, 70, 190])
        self.upper_red1 = array([10, 255, 255])
        self.lower_red2 = array([170, 70, 190])
        self.upper_red2 = array([180, 255, 255])
        self.virtual_aperture = virtual_aperture


    def filter(self, bgr_image):
        hsv_image = self.convert_bgr_to_HSV(bgr_image)
        filtered_image = self.get_agar_pixels(hsv_image,bgr_image)
        median_blured = cv2.medianBlur(filtered_image, 5)
        return median_blured

    def show_compared_image(self, original_image, filtered_image):
        compare_figure = cv2.hconcat([original_image, filtered_image])
        cv2.imshow('original', compare_figure)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_image(self, image, folder):
        HSV_folder = path.join(folder, 'hsv_filtered')
        # Create the 'hsv' folder if it doesn't exist
        if not path.exists(HSV_folder):
            makedirs(HSV_folder)
        img_path = path.join(HSV_folder, f"{random.randint(0, 100)}.png")
        cv2.imwrite(img_path, image)

    def get_agar_pixels(self,hsv_image,bgr_image):
        mask1 = cv2.inRange(hsv_image, self.lower_red1, self.upper_red1)
        mask2 = cv2.inRange(hsv_image, self.lower_red2, self.upper_red2)
        # Combine the masks
        mask = cv2.bitwise_or(mask1, mask2)
        # Apply the mask to the original image
        red_areas = cv2.bitwise_and(hsv_image, hsv_image, mask=mask)
        for x in range(red_areas.shape[0]):
            for y in range(red_areas.shape[1]):
                if y <= self.virtual_aperture or y >= (hsv_image.shape[1]-self.virtual_aperture):
                    red_areas[x][y] = [0,0,0]
                    continue
                if red_areas[x][y][2] > 0:
                    red_areas[x][y] = [255, 255, 255]
                else:
                    red_areas[x][y] = [0,0,0]
        return red_areas

    def convert_bgr_to_HSV(self,image):
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        return hsv_image

if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir, r"..\agar_height_evaluator_demo_images")
    top_bottom = 380
    left_right = 600
    image_fetcher = ImageFetcher(images_folder)
    images = image_fetcher.fetch()
    cropper = ImageCropper(top_bottom, left_right)
    hsv_filter = HSVFilter(virtual_aperture=320)
    for image in images:
        cropped_image = cropper.crop(image)
        filtered_image = hsv_filter.filter(cropped_image)
        hsv_filter.show_compared_image(cropped_image, filtered_image)
        # hsv_filter.save_image(filtered_image,images_folder)