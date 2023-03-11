from animation import Animation
import random


class Drip(Animation):

    def __init__(self):
        Animation.__init__(self)

        self.strip = Animation.stripFactory.build()
        
        self.growing = True

        self.colors = self.parms.getColors()

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
        self.currentColor = random.choice(self.colors)

        middle = self.parms.count / 2
        if (self.parms.count % 2 == 1):
            # we have to paint the middle pixel
            middle = round(self.parms.count / 2) - 1
            self.left = middle - 1
            self.right = middle + 1 
            self.strip.set_pixel(middle, self.currentColor)
        else:
            self.left = middle - 1
            self.right = middle

    def setLogGradient(self, color1, color2):
        self.strip.set_pixel_line_gradient(
            self.logLeft, self.logLeft + self.logSize, color1, color2)

    def setPixelToCurrentColor(self, pixel):
        self.strip.set_pixel(pixel, self.currentColor)
        self.rest()
        self.strip.show()
