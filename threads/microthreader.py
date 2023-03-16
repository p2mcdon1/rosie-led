import _thread
from threads.threaderbase import ThreaderBase


class MicroThreader(ThreaderBase):
    def __init__(self):
        self.baton = _thread.allocate_lock()

    # override
    def acquireLock(self):
        self.baton.acquire()

    # override
    def releaseLock(self):
        self.baton.release()

    # override
    def startAnimationThread(self, func):
        _thread.start_new_thread(func, ())
