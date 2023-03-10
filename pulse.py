from animation import Animation
from colorutility import ColorUtility


class Pulse(Animation):

    def __init__(self):
        Animation.__init__(self)

        self.strip = Animation.stripFactory.build()

        self.colors = self.parms.getColors()
        self.colorIndex = 0
        self.goalColor = self.parms.black
        self.currentColor = self.parms.black

        self.stepFactor = 21
        self.totalSteps = round(max(1, round(255 / self.stepFactor)) * 1.3)
        self.fading = False
        self.step = 0

    # override
    def run(self, checkRun):
        print(f'starting to run {self.__class__.__name__}...')

        while checkRun():
            if self.fading:
                if (self.step > self.totalSteps):
                    self.fading = False
                    self.step = 0
                    self.__nextColor()
            else:
                if (self.step > self.totalSteps):
                    self.fading = True
                    self.step = 0

            for pixel in range(self.parms.count):
                self.strip.set_pixel(pixel, self.currentColor)

            self.strip.show()
            self.rest()

            self.__adjustColor()
            self.step += 1

        print(f'done running {self.__class__.__name__}')

    def __adjustColor(self):
        stepFactor = -self.stepFactor if self.fading else self.stepFactor
        self.currentColor = ColorUtility.adjustWithLimit(
            self.currentColor, stepFactor, self.goalColor)

    def __nextColor(self):
        self.colorIndex += 1
        if (self.colorIndex >= len(self.colors)):
            self.colorIndex = 0
        self.currentColor = self.colors[self.colorIndex]
        self.goalColor = self.currentColor
