from palette import Palette
from parms import Parms
from stripfactorybase import StripFactoryBase
import time


class Animation:
    stripFactory = StripFactoryBase()

    def __init__(self):
        self.parms = Parms()
        self.refresh = self.parms.refresh
        self.palette = Palette(self.parms.getColors(), self.parms.black)

    def run(self, runFlag):
        pass

    def rest(self):
        time.sleep(self.refresh)

    def getCurrentColor(self):
        return self.palette.currentColor

    def getNextRandomColor(self):
        return self.palette.getNextRandomColor()
