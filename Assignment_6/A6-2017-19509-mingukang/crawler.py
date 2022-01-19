import urllib.request
from urllib import parse
import json

class Crawler(object):

    def __init__(self, city="Seoul", region=None):
        self.city = city      # e.g. 서울
        self.county = region    # e.g. 강남구

    def weather_fetch(self, city="Seoul"):
        self.city = city

        app_key = "7a8b1150587922f7e510d4deb4f96aef"
        loc = self.city
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(loc, app_key)

        with urllib.request.urlopen(url) as response:
            self.weather_data = json.loads(response.read().decode("utf-8"))

        return self.weather_data

