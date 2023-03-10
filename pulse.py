from animation import Animation
from colorutility import ColorUtility


class Pulse(Animation):

    def __init__(self):
        Animation.__init__(self)

        self.strip = Animation.stripFactory.build()

        self.colors = self.parms.getColors()
        self.colorIndex = 0

        self.pulseLength = 5.0
        self.totalSteps = self.pulseLength / self.parms.refresh
        self.stepModulo = max(1, round(self.totalSteps / 255))
        self.currentStep = 0

    # override
    def run(self, checkRun):
        print(f'starting to run {self.__class__.__name__}...')

        while checkRun():
            if (self.currentStep >= self.totalSteps):
                self.currentStep = 0
                self.colorIndex = self.colorIndex + 1
                if (self.colorIndex >= len(self.colors)):
                    self.colorIndex = 0

            if (self.currentStep == 0):
                self.__startColor()
            else:
                if (self.currentStep % self.stepModulo == 0):
                    self.__stepColor()

            self.strip.set_pixel_line_gradient(
                0, self.parms.count - 1, self.currentColor, self.currentColor)
            self.strip.show()
            self.currentStep = self.currentStep + 1

        print(f'done running {self.__class__.__name__}')

    def __startColor(self):
        self.currentColor = self.colors[self.colorIndex]

    def __stepColor(self):
        self.currentColor = ColorUtility.reduce(
            self.currentColor, 1)
