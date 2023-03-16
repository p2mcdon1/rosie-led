from animations.bounce import Bounce
from animations.colorwave import ColorWave
from animations.drip import Drip
from animations.pulse import Pulse
from animations.twinkle import Twinkle


class Selector:
    def __init__(self):
        self.animations = [Bounce(), ColorWave(), Drip(), Pulse(), Twinkle()]
        self.selector = -1

    def switch(self):
        self.selector = self.selector + 1

        if self.selector >= len(self.animations):
            self.selector = 0

        return self.animations[self.selector].run
