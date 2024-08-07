from os import path, makedirs
import cv2
from copy import deepcopy
from image_cropper import ImageCropper
from image_fetcher import ImageFetcher
from HSV_filter import HSVFilter
import random


class FindRectangles:
    def __init__(self):
        pass


    def find(self,image,filtered_image):
        horiz_crop = round((image.shape[1] - filtered_image.shape[1])/2)
        vert_crop = round((image.shape[0] - filtered_image.shape[0])/2)
        gray = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        possible_rectangles = []
        self.find_possible_rectangles(contours, possible_rectangles)
        if len(possible_rectangles) >> 0:
            biggest_rectangle = self.get_biggest_rectangle(possible_rectangles)
            x, y, w, h = cv2.boundingRect(biggest_rectangle)
            x = x + horiz_crop
            y = y + vert_crop
            return [x,y,w,h]
        else :
            return None

    def show_image(self, image, rectangle_coord):
        image_copy = deepcopy(image)
        x, y, w, h = rectangle_coord
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('Rectangles Detected', image_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def find_possible_rectangles(self,contours,possible_rectangles):
        for contour in contours:
            epsilon = 0.04 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            # Check if polygon has 4 corners (assuming it's a rectangle)
            if len(approx) == 4:
                possible_rectangles.append(contour)

    def get_biggest_rectangle(self,possible_rectangles):
        max_area = 0
        biggest_rectangle = None
        for rectangle in possible_rectangles:
            area = cv2.contourArea(rectangle)
            if area >= max_area:
                max_area = area
                biggest_rectangle = rectangle
        return biggest_rectangle

    def save_image(self, image, rectangle_coord, folder):
        image_copy = deepcopy(image)
        x, y, w, h = rectangle_coord
        cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
        rectangle_folder = path.join(folder, 'rectangle')
        # Create the 'rectangle' folder if it doesn't exist
        if not path.exists(rectangle_folder):
            makedirs(rectangle_folder)
        img_path = path.join(rectangle_folder, f"{random.randint(0, 100)}.png")
        cv2.imwrite(img_path, image_copy)


if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir, r"..\agar_height_evaluator_demo_images")
    top_bottom = 380
    left_right = 600
    image_fetcher = ImageFetcher(images_folder)
    images = image_fetcher.fetch()
    cropper = ImageCropper(top_bottom, left_right)
    hsv_filter = HSVFilter(virtual_aperture=320)
    rectangle_finder = FindRectangles()
    for image in images:
        cropped_image = cropper.crop(image)
        filtered_image = hsv_filter.filter(cropped_image)
        rectangle_coord = rectangle_finder.find(image, filtered_image)
        if rectangle_coord != None:
            rectangle_finder.show_image(image, rectangle_coord)
            # rectangle_finder.save_image(image, rectangle_coord,images_folder)
        else:
            print("\nCan't detect the agar\n")



