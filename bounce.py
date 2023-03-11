from animation import Animation
import random


class Bounce(Animation):

    def __init__(self):
        Animation.__init__(self)

        self.strip = Animation.stripFactory.build()

        self.logSize = max(1, round(self.parms.count / 30))
        self.step = 2
        self.logLeft = 0
        self.leftToRight = True

        self.colors = self.parms.getColors()
        self.currentColor = self.parms.black
        self.previousColor = self.parms.black

    # override
    def run(self, checkRun):
        print(f'starting to run {self.__class__.__name__}...')

        self.setCurrentColor()

        while checkRun():

            if (self.checkReverse()):
                self.setCurrentColor()

            if (self.leftToRight):
                self.logLeft = self.logLeft + self.step
                self.strip.rotate_right(self.step)
            else:
                self.logLeft = self.logLeft - self.step
                self.strip.rotate_left(self.step)

            self.rest()
            self.strip.show()

        print(f'done running {self.__class__.__name__}')

    def shouldReverse(self):
        if (self.leftToRight):
            return (self.logLeft + self.logSize + self.step >= self.parms.count)
        else:
            return (self.logLeft - self.step < 0)

    def checkReverse(self):
        if (self.shouldReverse()):
            self.leftToRight = not self.leftToRight
            return True
        else:
            return False

    def setCurrentColor(self):
        self.previousColor = self.currentColor
        self.currentColor = random.choice(self.colors)

        logRange = range(self.logLeft, self.logLeft + self.logSize + 1, 1) if self.leftToRight else range(
            self.logLeft + self.logSize, self.logLeft - 1, -1)

        for pixel in logRange:
            self.setPixelToCurrentColor(pixel)

        if self.leftToRight:
            self.setLogGradient(self.parms.black, self.currentColor)
        else:
            self.setLogGradient(self.currentColor, self.parms.black)

    def setLogGradient(self, color1, color2):
        self.strip.set_pixel_line_gradient(
            self.logLeft, self.logLeft + self.logSize, color1, color2)

    def setPixelToCurrentColor(self, pixel):
        self.strip.set_pixel(pixel, self.currentColor)
        self.rest()
        self.strip.show()
