from parms import Parms
import _thread


class Animation:

    def __init__(self):
        self.parms = Parms()
        self.refresh = self.parms.refresh

    def run(self, runFlag: bool, baton: _thread.LockType):
        baton.acquire()
        self.onRun(runFlag)
        baton.release()

    def onRun(self, runFlag):
        pass
