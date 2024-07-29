import cv2
import numpy as np
import pyrealsense2 as rs
import time
import os

def main():
    image_ammount = 3
    images = []
    # Configure depth and color streams
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)
    # Start streaming
    pipeline.start(config)
    time.sleep(2)
    input("Press Enter to capture an image...")
    for index in range(image_ammount):
        start_time = time.time()
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        # Convert images to numpy arrays
        color_image = np.asanyarray(color_frame.get_data())

        images.append(color_image)
    # frames = pipeline.wait_for_frames()
    # color_frame = frames.get_color_frame()
    # color_image = np.asanyarray(color_frame.get_data())
    stop_time = time.time()
    print(f"time : {stop_time - start_time}")
    pipeline.stop()
    #
    for image in images:
        cv2.imshow('image', image)
        cv2.waitKey(0)
    image_name = 0
    for image in images:
        img_path = os.path.join(r"C:\Users\15142\OneDrive - USherbrooke\S7\STAGE-T5\UR5_BIO_VISION\keyboard_images\spot\multiple_pics\trigger_test",f"{image_name}.jpg")
        cv2.imwrite(img_path, image)
        image_name += 1





if __name__ == "__main__":
    main()




    # def save_images(self, folder):
    #     for image_index in range(len(self.median_images)):
    #         self.save_image(self.median_images[image_index], image_index, folder)
    #
    # def save_image(self, image, image_name, folder):
    #     HSV_folder = path.join(folder, 'HSV_filtered')
    #     # Create the 'HSV' folder if it doesn't exist
    #     if not path.exists(HSV_folder):
    #         makedirs(HSV_folder)
    #     img_path = path.join(HSV_folder, f"{image_name}.png")
    #     cv2.imwrite(img_path, image)