from os import path
from image_fetcher import ImageFetcher
from numpy import sqrt
from find_rectangles import FindRectangles
from HSV_filter import HSVFilter
from image_cropper import ImageCropper



class ManualHeightEvaluator:
    def __init__(self,images,rectangles_size,petri_position):
        self.images = images
        self.bottom_of_holder = 540
        self.rectangles_size = rectangles_size
        self.petri_position = petri_position
        self.focal_length = 0.00188 #m
        self.pixel_size = 0.00000207 #m
        self.top_rectangle_pixel_positions = []
        self.bottom_rectangle_pixel_positions = []
        self.height_in_pixel = []
        self.height_in_mm = []
        self.sensor_distance = []
        self.metric_thickness = []
        self.get_top_from_center()
        self.get_bottom_from_center()
        self.get_agar_height_in_pixel()
        self.petri_distance = self.compute_petri_distance()
        self.compute_sensor_distance()
        self.get_agar_height_in_mm()

    def get_top_from_center(self):
        for image_index in range(len(self.images)):
            center_y = round(self.images[image_index].shape[0]/2)
            rect_top = (self.rectangles_coord[image_index][1] + round(self.rectangles_coord[image_index][3]/2)) - center_y
            self.top_rectangle_pixel_positions.append(rect_top)
    def get_bottom_from_center(self):
        for image_index in range(len(self.images)):
            center_y = round(self.images[image_index].shape[0] / 2)
            rect_bottom = self.bottom_of_holder - center_y
            self.bottom_rectangle_pixel_positions.append(rect_bottom)
    def get_agar_height_in_pixel(self):
        for image_index in range(len(self.images)):
            self.height_in_pixel.append(self.top_rectangle_pixel_positions[image_index]- self.bottom_rectangle_pixel_positions[image_index])

    def get_agar_height_in_mm(self):
        for image_index in range(len(self.images)):
            height_metric = self.height_in_pixel[image_index]*self.pixel_size*self.petri_distance/self.sensor_distance[image_index]
            self.height_in_mm.append(height_metric)
            print(height_metric)

    def compute_petri_distance(self):
        x = self.petri_position[1]
        y = self.petri_position[2]
        return sqrt(x**2 + y**2)

    def compute_sensor_distance(self):
        for image_index in range(len(self.images)):
            distance = sqrt((self.bottom_rectangle_pixel_positions[image_index]**2)*self.pixel_size + self.focal_length**2)
            self.sensor_distance.append(distance)

if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir, r"..\agar_height_evaluator_demo_images")
    image_fetcher = ImageFetcher(images_folder)
    images = image_fetcher.fetch()
    top_bottom = 250
    left_right = 350
    cropper = ImageCropper(images, top_bottom, left_right)
    cropped_images = cropper.crop()
    hsv_filter = HSVFilter(cropped_images, 275)
    filtered_images = hsv_filter.filter()
    rectangle_finder = FindRectangles(images, filtered_images)
    rectangles_coord = rectangle_finder.find()
    rectangle_finder.show_images()
    petri_position = [0, 0.0004, 0.118614]
    app = ManualHeightEvaluator(rectangle_finder.good_images,rectangles_coord,petri_position)
    # agar_thickness = app.get_metric_thickness()
    # print(agar_thickness)
