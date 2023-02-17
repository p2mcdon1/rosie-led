from asciistrip import AsciiStrip
from parms import Parms
from stripfactorybase import StripFactoryBase


class AsciiStripFactory(StripFactoryBase):
    def __init__(self):
        self.parms = Parms()

    def build(self):
        strip = AsciiStrip(self.parms.count)

        return strip
