import cv2
from os import path, listdir, makedirs





class CropAuto:
    def __init__(self,images,top_bottom,left_right):
        self.height, self.width = images[0].shape[:2]
        self.images = images
        self.top_bottom = top_bottom
        self.left_right = left_right
        self.cropped_images = []

    def crop(self):
        for image in self.images:
            cropped_image = self.crop_image(image, self.top_bottom, self.top_bottom, self.left_right, self.left_right)
            self.cropped_images.append(cropped_image)
        return self.cropped_images

    def show_images(self):
        for image_index in range(len(self.images)):
            cv2.imshow("Original Image", self.images[image_index])
            cv2.imshow("Cropped Image", self.cropped_images[image_index])
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def save_images(self,folder):
        for image_index in range(len(self.cropped_images)):
            self.save_image(self.cropped_images[image_index],image_index,folder)

    def save_image(self,image,image_name,folder):
        cropped_folder = path.join(folder, 'cropped')
        # Create the 'cropped' folder if it doesn't exist
        if not path.exists(cropped_folder):
            makedirs(cropped_folder)
        img_path = path.join(cropped_folder, f"{image_name}.png")
        cv2.imwrite(img_path, image)
    def crop_image(self,image, top, bottom, left, right):
        cropped_image = image[top:self.height-bottom, left:self.width-right]
        return cropped_image


if __name__ == "__main__":
    script_dir = path.dirname(path.abspath(__file__))
    images_folder = path.join(script_dir, r"..\images_petri")
    images = []
    images_name = [f for f in listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    for image_name in images_name:
        img_path = path.join(images_folder, image_name)
        image =  cv2.imread(img_path)
        images.append(image)
    top_bottom = 250
    left_right = 350
    app = CropAuto(images,top_bottom,left_right)
    cropped_images = app.crop()
    app.show_images()
    app.save_images(images_folder)




