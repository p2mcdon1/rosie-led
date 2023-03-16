from strips.asciistrip import AsciiStrip
from strips.stripfactorybase import StripFactoryBase


class AsciiStripFactory(StripFactoryBase):
    def build(self, count):
        return AsciiStrip(count)
