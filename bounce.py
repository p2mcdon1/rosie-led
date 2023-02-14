from animation import Animation
from stripFactory import StripFactory
import time


class Bounce(Animation):

    def __init__(self):
        Animation.__init__(self)

        numpix = self.parms.count

        stripFactory = StripFactory()
        self.strip = stripFactory.build()

        self.logSize = 10
        self.step = 2
        self.logLeft = 0
        self.leftToRight = True

        self.strip.set_pixel_line_gradient(
            self.logLeft, self.logSize, self.parms.ultraPink, self.parms.electricPurple)

    # override
    def onRun(self, runFlag):
        print('starting to run Bounce...')

        while runFlag():
            if (self.leftToRight):
                self.logLeft = self.logLeft + 2
                if (self.logLeft + self.logSize >= self.parms.count):
                    self.leftToRight = False
                    self.logLeft = self.logLeft - 2
                    self.strip.rotate_left(self.step)
                else:
                    self.strip.rotate_right(self.step)
            else:
                self.logLeft = self.logLeft - 2
                if (self.logLeft < 0):
                    self.leftToRight = True
                    self.logLeft = self.logLeft + 2
                    self.strip.rotate_right(self.step)
                else:
                    self.strip.rotate_left(self.step)

            time.sleep(self.refresh)
            self.strip.show()

        print('done running Bounce')
