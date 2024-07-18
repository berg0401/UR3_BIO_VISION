from state_feature import StateFeature

class ThermoState:
    def __init__(self, name):
        self.name = name
        self.features = []
    def add_feature(self, word, location):
        feature = StateFeature(word,location)
        self.features.append(feature)