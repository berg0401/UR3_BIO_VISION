from cv2 import imshow, waitKey, COLOR_BGR2GRAY, cvtColor
import numpy as np
import pyrealsense2 as rs


class RealsenseCamera():
    def __init__(self):
        self.num_pics = 3
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)
        self.pipeline.start(self.config)
        self.options_value = {'Exposure': 19.0,
                               'Gain': 78.0,
                               'Brightness': 0.0,
                               'Contrast': 50.0,
                               'Gamma': 300.0,
                               'Hue': 0.0,
                               'Saturation': 64.0,
                               'Sharpness': 100.0,
                               'Enable Auto White Balance': 1.0,
                               'Enable Auto Exposure': 0.0}
        self.realsense_options = {'Exposure': rs.option.exposure,
                                  'Gain': rs.option.gain,
                                  'Brightness': rs.option.brightness,
                                  'Contrast': rs.option.contrast,
                                  'Gamma': rs.option.gamma,
                                  'Saturation': rs.option.saturation,
                                  'Sharpness': rs.option.sharpness,
                                  'Hue': rs.option.hue,
                                  'Enable Auto Exposure': rs.option.enable_auto_exposure,
                                  'Enable Auto White Balance': rs.option.enable_auto_white_balance}
        device = self.pipeline.get_active_profile().get_device()
        # Query sensors (typically, color and depth sensors)
        sensors = device.query_sensors()
        self.color_sensor = sensors[1]
        self.set_options()

    def __del__(self):
        self.pipeline.stop()

    def set_option(self, option_name):
        # Get the option constant from the map
        value = self.options_value[option_name]
        realsense_option = self.realsense_options[option_name]
        # Set the option value
        self.color_sensor.set_option(realsense_option, value)
    def set_options(self):
        # Must initialize Enable Auto White Balance and Auto Exposure first
        self.set_option('Enable Auto White Balance')
        self.set_option('Enable Auto Exposure')
        self.set_option('Exposure')
        self.set_option('Gain')
        self.set_option('Brightness')
        self.set_option('Contrast')
        self.set_option('Gamma')
        self.set_option('Hue')
        self.set_option('Saturation')
        self.set_option('Sharpness')




    def trigger(self):
        images = []
        for index in range(self.num_pics):
            frames = self.pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            color_image = np.asanyarray(color_frame.get_data())
            gray_image = cvtColor(color_image, COLOR_BGR2GRAY)
            images.append(gray_image)
        return images

#convert color to gray
    def show_images(self, images):
        for image in images:
            imshow('captured image', image)
            waitKey(0)

if __name__ == "__main__":
    camera = RealsenseCamera()
    images = camera.trigger()
    camera.show_images(images)
