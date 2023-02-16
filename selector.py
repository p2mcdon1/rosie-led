from bounce import Bounce
from colorwave import ColorWave
from twinkle import Twinkle


class Selector:
    def __init__(self):
        self.bounce = Bounce()
        self.colorWave = ColorWave()
        self.twinkle = Twinkle()
        self.selector = -1

    def switch(self):
        self.selector = self.selector + 1

        if (self.selector > 2):
            self.selector = 0

        if self.selector == 0:
            return self.bounce.run
        elif self.selector == 1:
            return self.colorWave.run
        elif self.selector == 2:
            return self.twinkle.run
