from buttonbase import ButtonBase
from selector import Selector
import signal
from threaderbase import ThreaderBase
import time


class Runner:
    def __init__(self, button: ButtonBase, threader: ThreaderBase):
        self.runAnimation = True
        self.keepRunningAnimation = lambda: self.runAnimation
        self.threader = threader
        self.button = button
        self.selector = Selector()
        self.keepRunning = True

        def handler(signum, frame):
            self.runAnimation = False
            self.threader.acquireLock()
            self.button.stopListening()
            self.keepRunning = False

        signal.signal(signal.SIGINT, handler)

    def __switch(self):
        print()
        print('switching...')

        if self.runAnimation:
            self.runAnimation = False
            self.threader.acquireLock()
            self.runAnimation = True
            self.threader.releaseLock()

        animation = self.selector.switch()

        self.threader.startAnimation(animation, self.keepRunningAnimation)

    def run(self):
        while self.keepRunning:
            buttonPressed = self.button.wasPressed()

            if buttonPressed:
                self.__switch()

            time.sleep(0.2)
