from text_reader import TextReader
from realsense_camera import RealsenseCamera
from image_encoder import ImageEncoder


#INIT THE SERVER
text_reader = TextReader()
camera = RealsenseCamera()
while(True):
    keyboard = input("Press '0' to capture an image, and 'exit' to quit:\n")  # Replace this line with call from robot
    if keyboard == '0':
        images = camera.trigger()
        image_encoder = ImageEncoder()
        images_content = image_encoder.encode(images)
        for content in images_content:
            texts = text_reader.read(content)
            text_reader.show_result(texts)
            # text_reader.show_image(content)
    if keyboard == 'exit':
        break
    else:
        continue
del camera
