import pyrealsense2 as rs
from find_rectangles import FindRectangles
from os import path
from image_fetcher import ImageFetcher
from image_cropper import ImageCropper
from HSV_filter import HSVFilter
from cv2 import line,imshow,waitKey,destroyAllWindows
class HeightEvaluator:

    def __init__(self, petri_distance):
        self.fx = 1365.8494873046875
        self.fy = 1363.700439453125
        self.cx = 959.4417724609375
        self.cy = 532.7769775390625
        self.petri_distance = petri_distance
        self.bottom_offset = 11

    def get_intrinsics(self, pipeline):
        rgb_intrinsics = pipeline.get_active_profile().get_stream(
            rs.stream.color).as_video_stream_profile().get_intrinsics()
        self.fx, self.fy = rgb_intrinsics.fx, rgb_intrinsics.fy
        self.cx, self.cy = rgb_intrinsics.ppx, rgb_intrinsics.ppy

    def get_agar_height(self,rectangle_coord,image):
        agar_height_pixel = rectangle_coord[1] + rectangle_coord[3]
        bottom_petri = self.cy+self.bottom_offset
        height = (agar_height_pixel - (bottom_petri)) * self.petri_distance / self.fy
        return height
    def show_result(self,height):
        print(height)
    def show_image(self,image,height):
        agar_height_pixel= height*self.fy/self.petri_distance+(self.cy+11)
        line(image, (750, int(agar_height_pixel)), (1160, int(agar_height_pixel)), (0, 255, 0), 1)
        line(image, (750, int(self.cy + 11)), (1160, int(self.cy + 11)), (0, 255, 0), 1)
        imshow('image', image)
        waitKey(0)
        destroyAllWindows()

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
    height_evaluator = HeightEvaluator(petri_distance=0.118614)
    for image in images:
        cropped_image = cropper.crop(image)
        filtered_image = hsv_filter.filter(cropped_image)
        rectangle_coord = rectangle_finder.find(image, filtered_image)
        height = height_evaluator.get_agar_height(rectangle_coord, image)
        height_evaluator.show_result(height)
        # height_evaluator.show_image(image,height)