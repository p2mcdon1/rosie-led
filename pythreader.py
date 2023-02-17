from threaderbase import ThreaderBase
import threading


class PyThreader(ThreaderBase):
    def __init__(self):
        self.baton = threading.Lock()
        self.thread = None

    # override
    def acquireLock(self):
        self.baton.acquire()

    # override
    def releaseLock(self):
        self.baton.release()

    # override
    def startAnimationThread(self, func):
        if (self.thread is not None):
            self.thread.join()

        self.thread = threading.Thread(target=func, args=())
        self.thread.start()
