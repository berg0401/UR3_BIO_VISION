class RobotPosition:
    def __init__(self,position_name):
        self.position_name = position_name
        self.crop_measures = []
        self.init_crop_dictionary()
        self.left_crop = self.crop_measures[position_name][0]
        self.right_crop = self.crop_measures[position_name][1]
        self.top_crop = self.crop_measures[position_name][2]
        self.bottom_crop = self.crop_measures[position_name][3]

    def init_crop_dictionary(self):
        self.crop_measures = {
            'default': [820,851,710,345],
            'spot' : [740,935,540,515]
        }
