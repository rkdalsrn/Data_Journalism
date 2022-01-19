class Article(object):

    GENERIC   = 1
    HIGH_TEMP = 2
    LOW_TEMP  = 3
    HIGH_DUST = 4
    LOW_DUST  = 5

    def __init__(self, template, address, w_events, f_fortune):
        self.template = template
        self.address = address
        self.weather = w_events
        self.fortune = f_fortune

    def generate(self):
        if self.template == self.HIGH_TEMP:
            article = "오늘은 날씨가 덥겠습니다. {}시 현재 {}의 온도는 섭씨 {}도, 습도는 {}% 입니다. 이렇게 더운 날씨 {}".format(self.weather.time_observation.hour,
                                    self.address,
                                    self.weather.temp,
                                    self.weather.humidity,
                                    self.fortune)
        elif self.template == self.LOW_TEMP:
            article = "{}월 {}일 {}시 현재, {}의 온도는 섭씨 {}도로 영하권의 추운 날씨가 계속되고 있습니다. 이렇게 추운 날씨 {}".format(self.weather.time_observation.month,
                                    self.weather.time_observation.day,
                                    self.weather.time_observation.hour,
                                    self.address,
                                    self.weather.temp,
                                    self.fortune)
        else: #GENERIC
            article = "{}월 {}일 {}시 현재, {}의 온도는 섭씨 {}도, 습도는 {}%입니다. {}".format(self.weather.time_observation.month,
                                    self.weather.time_observation.day,
                                    self.weather.time_observation.hour,
                                    self.address,
                                    self.weather.temp,
                                    self.weather.humidity,
                                    self.fortune)

        return article
