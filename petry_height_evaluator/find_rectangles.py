from os import path, listdir, makedirs
import cv2
from copy import deepcopy
from crop_auto import CropAuto
from HSV_filter import HSVFilter



class FindRectangles:
    def __init__(self,images,filtered_images):
        self.filtered_images = filtered_images
        self.images = images
        self.good_images = []
        self.rectangles_size = []
        self.rectangles_size_show = []


    def find(self):
        for image_index in range(len(self.filtered_images)):
            horiz_crop = round((self.images[image_index].shape[1] - self.filtered_images[image_index].shape[1])/2)
            vert_crop = round((self.images[image_index].shape[0] - self.filtered_images[image_index].shape[0])/2)
            gray = cv2.cvtColor(self.filtered_images[image_index], cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 50, 150)
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            possible_rectangles = []
            self.find_possible_rectangles(contours, possible_rectangles)
            if len(possible_rectangles) >> 0:
                self.good_images.append(self.images[image_index])
                biggest_rectangle = self.get_biggest_rectangle(possible_rectangles)
                x, y, w, h = cv2.boundingRect(biggest_rectangle) #top left corner
                x = x + horiz_crop
                y = y + vert_crop
                self.rectangles_size.append([x,y,w,h])
            else:
                print("No rectangles found")
        return self.rectangles_size

    def show_images(self):
        images_copy = deepcopy(self.good_images)
        for image_index in range(len(self.good_images)):
            x = self.rectangles_size[image_index][0]
            y = self.rectangles_size[image_index][1]
            w = self.rectangles_size[image_index][2]
            h = self.rectangles_size[image_index][3]
            cv2.rectangle(images_copy[image_index], (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow('Rectangles Detected', images_copy[image_index])
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

    def save_images(self,folder):
        images_copy = deepcopy(self.good_images)
        for image_index in range(len(self.good_images)):
            x = self.rectangles_size[image_index][0]
            y = self.rectangles_size[image_index][1]
            w = self.rectangles_size[image_index][2]
            h = self.rectangles_size[image_index][3]
            cv2.rectangle(images_copy[image_index], (x, y), (x + w, y + h), (0, 255, 0), 2)
            self.save_image(images_copy[image_index],image_index,folder)

    def save_image(self,image,image_name,folder):
        rectangle_folder = path.join(folder, 'rectangle')
        # Create the 'rectangle' folder if it doesn't exist
        if not path.exists(rectangle_folder):
            makedirs(rectangle_folder)
        img_path = path.join(rectangle_folder, f"{image_name}.png")
        cv2.imwrite(img_path, image)

if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir, r"..\images_petri")
    images = []
    images_name = [f for f in listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    for image_name in images_name:
        img_path = path.join(images_folder, image_name)
        image = cv2.imread(img_path)
        images.append(image)
    top_bottom = 250
    left_right = 350
    cropper = CropAuto(images, top_bottom, left_right)
    cropped_images = cropper.crop()
    hsv_filter = HSVFilter(cropped_images, 250)
    filtered_images = hsv_filter.filter()
    app = FindRectangles(images,filtered_images)
    rectangles_size = app.find()
    app.show_images()
    app.save_images(images_folder)
