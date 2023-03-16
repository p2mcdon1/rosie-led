from utility.palette import Palette
from parms import Parms
from strips.stripfactorybase import StripFactoryBase
import time


class AnimationBase:
    stripFactory = StripFactoryBase()  # must be overridden at runtime

    def __init__(self):
        self.parms = Parms()
        self.refresh = self.parms.refresh
        self.palette = Palette(self.parms.getColors(), self.parms.black)
        self.strip = AnimationBase.stripFactory.build(self.parms.count)

    def run(self, runFlag):
        pass

    def rest(self):
        time.sleep(self.refresh)

    def getCurrentColor(self):
        return self.palette.currentColor

    def getNextRandomColor(self):
        return self.palette.getNextRandomColor()
