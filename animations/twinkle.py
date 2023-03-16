from animations.animationbase import AnimationBase
from utility.colors import Colors
import random


class Twinkler:
    def __init__(self):
        self.rgb = (0, 0, 0)
        self.velocity = 1


class Twinkle(AnimationBase):
    def __init__(self):
        AnimationBase.__init__(self)

        self.numberOfTwinklers = max(1, round(self.parms.count / 10))
        self.fadeLength = 3
        self.fadeCycleCount = self.fadeLength / self.parms.refresh
        self.reduction = -max(1, round(255 / self.fadeCycleCount))

        self.twinklers = []
        for _ in range(self.parms.count):
            self.twinklers.append(Twinkler())

    # override
    def run(self, checkRun):
        print(f"starting to run {self.__class__.__name__}...")

        while checkRun():
            self.updateTwinklers()

            currentNumberOfTwinklers = sum(
                t.rgb != self.parms.black for t in self.twinklers
            )
            numberToAdd = self.numberOfTwinklers - currentNumberOfTwinklers
            for _ in range(numberToAdd):
                color = self.getNextRandomColor()
                pixel = random.randrange(0, self.parms.count)

                self.strip.set_pixel(pixel, color)
                twinkler = self.twinklers[pixel]
                twinkler.rgb = color
                twinkler.velocity = random.randint(1, 10)

            self.rest()
            self.strip.show()

        print(f"done running {self.__class__.__name__}")

    def updateTwinklers(self):
        index = 0
        for t in self.twinklers:
            twinkler = self.twinklers[index]

            reducedRgb = self.reduce(twinkler)
            if Colors.isEffectivelyOff(reducedRgb):
                reducedRgb = self.parms.black

            twinkler.rgb = reducedRgb
            self.strip.set_pixel(index, reducedRgb)

            index = index + 1

    def reduce(self, twinkler: Twinkler):
        return Colors.adjust(twinkler.rgb, self.reduction, twinkler.velocity)
