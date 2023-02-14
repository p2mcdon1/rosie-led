from neopixel import Neopixel
from parms import Parms


class StripFactory:
    def __init__(self):
        self.parms = Parms()

    def build(self):
        strip = Neopixel(self.parms.count, 0, self.parms.ledDataPin, "GRB")
        strip.brightness(self.parms.brightness)

        return strip
