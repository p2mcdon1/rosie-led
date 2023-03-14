from animation import Animation
import random


class Drip(Animation):

    def __init__(self):
        Animation.__init__(self)

        self.strip = Animation.stripFactory.build()
        self.growing = True
        self.maxPixel = self.parms.count - 1

    # override
    def run(self, checkRun):
        print(f'starting to run {self.__class__.__name__}...')

        self.initialize()
        self.setCurrentColor()

        while checkRun():
            self.step()

            self.rest()
            self.strip.show()

            self.checkReverse()

        print(f'done running {self.__class__.__name__}')

    def checkReverse(self):
        if (not self.shouldReverse()):
            return

        self.growing = not self.growing
        self.setCurrentColor()

    def shouldReverse(self):
        if self.growing:
            return self.left == 0
        else:
            return self.left == self.getStartingLeft()

    def initialize(self):
        self.hasCenter = self.parms.count % 2 == 1

        if self.hasCenter:
            self.middle = max(0, round(self.parms.count / 2) - 1)
        else:
            self.middle = round(self.parms.count / 2)

        self.left = self.getStartingLeft()
        self.right = self.getStartingRight()

    def setCurrentColor(self):
        color = self.getNextRandomColor()

        if not self.growing:
            color = self.parms.black

        if self.hasCenter:
            self.strip.set_pixel(self.middle, color)

        self.strip.set_pixel(self.left, color)
        self.strip.set_pixel(self.right, color)

    def step(self):
        if self.growing:
            color = self.getCurrentColor()
            self.left = max(0, self.left - 1)
            self.right = min(self.right + 1, self.maxPixel)
            self.strip.set_pixel(self.left, color)
            self.strip.set_pixel(self.right, color)
        else:
            self.left = min(self.getStartingLeft(), self.left + 1)
            self.right = max(self.right - 1, self.getStartingRight())
            self.strip.set_pixel(self.left, self.parms.black)
            self.strip.set_pixel(self.right, self.parms.black)

    def getStartingRight(self):
        return min(self.maxPixel, self.middle + 1 if self.hasCenter else self.middle)

    def getStartingLeft(self):
        return max(0, self.middle - 1)
