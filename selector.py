from bounce import Bounce
from colorwave import ColorWave
from pulse import Pulse
from twinkle import Twinkle


class Selector:
    def __init__(self):
        self.animations = [Pulse(), Bounce(), ColorWave(), Twinkle()]
        self.selector = -1

    def switch(self):
        self.selector = self.selector + 1

        if (self.selector >= len(self.animations)):
            self.selector = 0

        return self.animations[self.selector].run
