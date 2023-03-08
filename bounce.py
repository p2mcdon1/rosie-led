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

        colors = self.parms.getColors()

        self.strip.set_pixel_line_gradient(
            self.logLeft, self.logSize, random.choice(colors), random.choice(colors))

    # override
    def run(self, checkRun):
        print(f'starting to run {self.__class__.__name__}...')

        while checkRun():
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

            self.rest()
            self.strip.show()

        print(f'done running {self.__class__.__name__}')
