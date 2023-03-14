from bounce import Bounce
from colorwave import ColorWave
from drip import Drip
from pulse import Pulse
from twinkle import Twinkle


class Selector:
    def __init__(self):
        self.animations = [Bounce(), ColorWave(), Drip(), Pulse(), Twinkle()]
        self.selector = -1

    def switch(self):
        self.selector = self.selector + 1

        if (self.selector >= len(self.animations)):
            self.selector = 0

        return self.animations[self.selector].run
