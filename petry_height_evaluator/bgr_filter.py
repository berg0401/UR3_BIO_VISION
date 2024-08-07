from os import path, makedirs
import cv2
import copy
from image_cropper import ImageCropper
from image_fetcher import ImageFetcher


class BGRFilter:
    def __init__(self,images,virtual_aperture):
        self.images = images
        self.virtual_aperture = virtual_aperture

    def filter(self):
        self.filtered_images=[]
        self.median_images=[]
        self.filtered_images = copy.deepcopy(self.images)
        for image in self.filtered_images:
            self.get_agar_pixels(image)
        for image in self.filtered_images:
            median_blured = cv2.medianBlur(image, 9)
            self.median_images.append(median_blured)
        return self.median_images

    def save_images(self,folder):
        for image_index in range(len(self.median_images)):
            self.save_image(self.median_images[image_index],image_index,folder)

    def save_image(self,image,image_name,folder):
        cropped_folder = path.join(folder, 'BGR_filtered')
        # Create the 'cropped' folder if it doesn't exist
        if not path.exists(cropped_folder):
            makedirs(cropped_folder)
        img_path = path.join(cropped_folder, f"{image_name}.png")
        cv2.imwrite(img_path, image)
    def get_agar_pixels(self,image):
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                if y <= self.virtual_aperture or y >= (image.shape[1]-self.virtual_aperture):
                    image[x][y] = [0,0,0]
                    continue
                if image[x][y][2] <= 180 or image[x][y][0] >= 100 or image[x][y][1] >= 100:
                    image[x][y] = [0,0,0]
                else:
                    image[x][y] = [255,255,255]
    def show_images(self):
        for image in self.median_images:
            cv2.imshow('original', image)
            cv2.waitKey(0)  # Wait for a key press to close the window
            cv2.destroyAllWindows()

if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir, r"..\agar_height_evaluator_demo_images")
    image_fetcher = ImageFetcher(images_folder)
    images = image_fetcher.fetch()
    top_bottom = 250
    left_right = 350
    app = ImageCropper(images, top_bottom, left_right)
    cropped_images = app.crop()
    app = BGRFilter(cropped_images,250)
    filtered_images = app.filter()
    app.show_images()
    #app.save_images(images_folder)