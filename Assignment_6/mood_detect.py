class Mood(object):

    GENERIC   = 1
    HIGH_TEMP = 2
    LOW_TEMP  = 3
    HIGH_DUST = 4
    LOW_DUST  = 5

    def decision(self, data):
        temp = float(data)

        if temp <= 10:
            return self.LOW_TEMP

        if temp > 30:
            return self.HIGH_TEMP

        if (10 < temp <=30):
            return self.GENERIC
