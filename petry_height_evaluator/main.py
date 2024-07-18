import cv2
from os import path, listdir, makedirs
from crop_auto import CropAuto
from HSV_filter import HSVFilter
from find_rectangles import FindRectangles
from height_evaluator import HeightEvaluator

def get_images(images_folder):
    images_name = [f for f in listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    images = []
    for image_name in images_name:
        img_path = path.join(images_folder, image_name)
        image = cv2.imread(img_path)
        images.append(image)
    return images

if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir, r"..\images_petri")
    images = get_images(images_folder)

    #crop dimensions
    top_bottom = 250
    left_right = 350

    #petri pot's position
    petri_position = [0, 0.0004, 0.0807071]

    #pipeline
    cropper = CropAuto(images, top_bottom, left_right)
    cropped_images = cropper.crop()
    hsv_filter = HSVFilter(cropped_images,275)
    filtered_images = hsv_filter.filter()
    rectangle_finder = FindRectangles(images,filtered_images)
    rectangles_size = rectangle_finder.find()
    #rectangle_finder.show_images()
    height_evaluator = HeightEvaluator(rectangle_finder.good_images, rectangles_size, petri_position)
    height = height_evaluator.get_metric_thickness()
    print(height)



