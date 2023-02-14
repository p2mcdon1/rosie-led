import _thread

class Animation:

    def __init__(self):
        self.refresh = 0.01

    def run(self, runFlag: bool, baton: _thread.LockType):
        baton.acquire()
        self.onRun(runFlag)
        baton.release()

    def onRun(self, runFlag):
        pass