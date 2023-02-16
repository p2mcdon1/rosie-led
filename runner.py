from key import KeyReader
from selector import Selector
import _thread
import time


class Runner:
    def __init__(self):
        self.runAnimation = True
        self.checkRun = lambda: self.runAnimation
        self.baton = _thread.allocate_lock()
        self.keyReader = KeyReader()
        self.selector = Selector()

    def __runBounce(self):
        self.bounce.run(self.checkRun, self.baton)

    def __runColorWave(self):
        self.colorWave.run(self.checkRun, self.baton)

    def __runMouse(self):
        self.twinkle.run(self.checkRun, self.baton)

    def __switch(self):
        print('switching...')

        if self.runAnimation:
            self.runAnimation = False
            self.baton.acquire()
            self.runAnimation = True
            self.baton.release()

        animation = self.selector.switch()

        _thread.start_new_thread(animation, (self.checkRun, self.baton))

    def run(self):
        while True:
            pushed = self.keyReader.wasPushed()

            if pushed:
                self.__switch()

            time.sleep(0.2)

        print('end main loop')
