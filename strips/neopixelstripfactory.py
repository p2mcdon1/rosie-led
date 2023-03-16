from parms import Parms
from strips.neopixelstrip import NeopixelStrip
from strips.stripfactorybase import StripFactoryBase


class NeoPixelStripFactory(StripFactoryBase):
    def __init__(self):
        self.parms = Parms()

    def build(self, count):
        strip = NeopixelStrip(count, 0, self.parms.ledDataPin, "GRB")
        strip.brightness(self.parms.brightness)

        return strip
