import cv2
from numpy import array
from os import path, listdir, makedirs
from crop_auto import CropAuto

class HSVFilter:
    def __init__(self,bgr_images,virtual_aperture):
        self.lower_red1 = array([0, 70, 185])
        self.upper_red1 = array([10, 255, 255])
        self.lower_red2 = array([170, 70, 185])
        self.upper_red2 = array([180, 255, 255])
        self.hsv_images = []
        self.bgr_images = bgr_images
        self.filtered_images = []
        self.median_images = []
        self.virtual_aperture = virtual_aperture


    def filter(self):
        for image in self.bgr_images:
            hsv_image = self.convert_bgr_to_HSV(image)
            self.hsv_images.append(hsv_image)
        for image_index in range(len(self.hsv_images)):
            filtered_image = self.get_agar_pixels(self.hsv_images[image_index],self.bgr_images[image_index])
            self.filtered_images.append(filtered_image)
        for image in self.filtered_images:
            median_blured = cv2.medianBlur(image, 5)
            self.median_images.append(median_blured)
        return self.median_images

    def show_images(self):
        for image_index in range(len(self.bgr_images)):
            self.compare_to_original(self.bgr_images[image_index],self.median_images[image_index])

    def compare_to_original(self,original_image,new_image):
        compare_figure = cv2.hconcat([original_image, new_image])
        cv2.imshow('original', compare_figure)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_images(self, folder):
        for image_index in range(len(self.median_images)):
            self.save_image(self.median_images[image_index], image_index, folder)

    def save_image(self, image, image_name, folder):
        HSV_folder = path.join(folder, 'HSV_filtered')
        # Create the 'HSV' folder if it doesn't exist
        if not path.exists(HSV_folder):
            makedirs(HSV_folder)
        img_path = path.join(HSV_folder, f"{image_name}.png")
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
    images_folder = path.join(script_dir, r"..\images_petri")
    images=[]
    images_name = [f for f in listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    for image_name in images_name:
        img_path = path.join(images_folder, image_name)
        image = cv2.imread(img_path)
        images.append(image)
    top_bottom = 250
    left_right = 350
    cropper = CropAuto(images, top_bottom, left_right)
    cropped_images = cropper.crop()
    hsv_filter = HSVFilter(cropped_images,250)
    filtered_images = hsv_filter.filter()
    hsv_filter.show_images()
    hsv_filter.save_images(images_folder)