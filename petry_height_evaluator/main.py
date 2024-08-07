from image_cropper import ImageCropper
from realsense_camera import RealsenseCamera
from HSV_filter import HSVFilter
from find_rectangles import FindRectangles
from height_evaluator import HeightEvaluator

if __name__ == "__main__":
    camera = RealsenseCamera()
    top_bottom = 380
    left_right = 600
    cropper = ImageCropper(top_bottom, left_right)
    hsv_filter = HSVFilter(virtual_aperture=320)
    rectangle_finder = FindRectangles()
    height_evaluator = HeightEvaluator(petri_distance=0.118614)
    height_evaluator.get_intrinsics(camera.pipeline)

    while(True):
        keyboard = input("Press '0' to capture an image, and 'exit' to quit:\n")  # Replace this line with call from robot
        if keyboard == '0':
            image = camera.trigger()
            cropped_image = cropper.crop(image)
            filtered_image = hsv_filter.filter(cropped_image)
            rectangle_finder = FindRectangles()
            rectangle_coord = rectangle_finder.find(image, filtered_image)
            if rectangle_coord != None:
                height = height_evaluator.get_agar_height(rectangle_coord, image)
                height_evaluator.show_result(height)
                height_evaluator.show_image(image, height)
            else : print("\nCan't detect the agar\n")
        if keyboard == 'exit':
            break
        else:
            continue
    del camera







