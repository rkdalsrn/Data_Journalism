import json
from datetime import datetime

class Events(object):

    WEATHER   = 1

    def __init__(self, data, event_type):
        self.data = data
        self.event_type = event_type

    def process_events(self):
        if self.event_type == self.WEATHER:
            self.time_observation = datetime.fromtimestamp(self.data["dt"])
            self.temp = self.data["main"]["temp"]
            self.temp_max = self.data["main"]["temp_max"]
            self.temp_min = self.data["main"]["temp_min"]
            self.humidity = self.data["main"]["humidity"]

