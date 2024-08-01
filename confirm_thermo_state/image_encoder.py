from cv2 import imencode

class ImageEncoder:
    def __init__(self):
        pass

    def encode(self, images):
        images_content = []
        for image in images:
            cropped_image = self.crop(image)
            success, encoded_image = imencode('.jpg', cropped_image)
            if success:
                images_content.append(encoded_image.tobytes())
        return images_content

    def crop(self,image):
        top_bottom = 200
        left_right = 600
        cropped_image = image[top_bottom:image.shape[0] - top_bottom, left_right:image.shape[1] - left_right]
        return cropped_image
