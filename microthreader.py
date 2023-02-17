import _thread
from threaderbase import ThreaderBase


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
    def __startAnimationThread(self, func):
        _thread.start_new_thread(func, ())
