from os import path, listdir, makedirs
import cv2
from numpy import sqrt
from find_rectangles import FindRectangles
from HSV_filter import HSVFilter
from crop_auto import CropAuto



class HeightEvaluator:
    def __init__(self,images,rectangles_size,petri_position):
        self.images = images
        self.rectangles_size = rectangles_size
        self.petri_position = petri_position
        self.focal_length = 0.00188 #m
        self.pixel_size = 0.000003 #m
        self.rectangle_centered_size = []
        self.get_rect_coord_from_center()
        self.petri_distance = self.compute_petri_distance()
        self.sensor_distance = []
        self.compute_sensor_distance()
        self.metric_thickness = []



    def get_rect_coord_from_center(self):
        for image_index in range(len(self.images)):
            center_x = round(self.images[image_index].shape[1]/2)
            center_y = round(self.images[image_index].shape[0]/2)
            x_centered = center_x - self.rectangles_size[image_index][0]
            y_centered = center_y - self.rectangles_size[image_index][1]
            self.rectangle_centered_size.append([x_centered,y_centered,self.rectangles_size[image_index][2],self.rectangles_size[image_index][3]])
    def compute_petri_distance(self):
        x = self.petri_position[1]
        y = self.petri_position[2]
        return sqrt(x**2 + y**2)

    def get_metric_thickness(self):
        for image_index in range(len(self.images)):
            h = self.rectangles_size[image_index][3] * self.pixel_size
            thickness = h*self.petri_distance/self.sensor_distance[image_index]
            self.metric_thickness.append(thickness)
        return self.metric_thickness
    def compute_sensor_distance(self):
        for image_index in range(len(self.rectangle_centered_size)):
            y = self.rectangle_centered_size[image_index][1] * self.pixel_size
            h = self.rectangles_size[image_index][3] * self.pixel_size
            if y <= 0:
                distance = sqrt(y**2 + self.focal_length**2)
            else:
                distance = sqrt((y-h)**2 + self.focal_length**2)
            self.sensor_distance.append(distance)

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
    rectangle_finder = FindRectangles(images, filtered_images)
    rectangles_size = rectangle_finder.find()
    petri_position = [0, 0.0004, 0.0807071]
    app = HeightEvaluator(rectangle_finder.good_images,rectangles_size,petri_position)
    agar_thickness = app.get_metric_thickness()
    print(agar_thickness)
