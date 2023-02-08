from abc import ABC, abstractmethod
import _thread

class Animation(ABC):

    def __init__(self):
        self.refresh = 0.1

    def run(self, runFlag: bool, baton: _thread.LockType):
        baton.acquire()
        self.onRun(runFlag)
        baton.release()

    @abstractmethod
    def onRun(self, runFlag):
        pass