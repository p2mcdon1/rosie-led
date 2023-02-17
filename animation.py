from parms import Parms
from stripfactorybase import StripFactoryBase
import time


class Animation:
    stripFactory = StripFactoryBase()

    def __init__(self):
        self.parms = Parms()
        self.refresh = self.parms.refresh

    def run(self, runFlag):
        pass

    def rest(self):
        time.sleep(self.refresh)
