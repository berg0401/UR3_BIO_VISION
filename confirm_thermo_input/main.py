from text_reader import TextReader
from realsense_camera import RealsenseCamera
from image_encoder import ImageEncoder


#INIT THE SERVER
text_reader = TextReader()
camera = RealsenseCamera()
while(True):
    input("Press Enter to capture an image...") # Replace this line with call from robot
    try:
        images = camera.trigger()
        image_encoder = ImageEncoder()
        images_content = image_encoder.encode(images)

        #GET THE IMAGE AFTER THE CAPTURE
        for content in images_content:
            texts = text_reader.read(content)
            text_reader.show_result(texts)
            # text_reader.show_image(content)
    except Exception as e:
        raise
