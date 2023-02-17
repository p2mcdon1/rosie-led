from animation import Animation
import random


class Twinkler:
    def __init__(self):
        self.rgb = (0, 0, 0)
        self.velocity = 1


class Twinkle(Animation):

    def __init__(self):
        Animation.__init__(self)

        self.strip = Animation.stripFactory.build()

        self.numberOfTwinklers = max(1, round(self.parms.count / 10))

        self.fadeLength = 3
        self.fadeCycleCount = self.fadeLength / self.parms.refresh
        self.reduction = max(1, round(255 / self.fadeCycleCount))
        self.colors = self.parms.getColors()

        self.twinklers = []
        for x in range(self.parms.count):
            self.twinklers.append(Twinkler())

    # override
    def run(self, checkRun):
        print('starting to run Twinkle...')

        while checkRun():
            self.updateTwinklers()

            currentNumberOfTwinklers = sum(
                t.rgb != self.parms.black for t in self.twinklers)
            numberToAdd = self.numberOfTwinklers - currentNumberOfTwinklers
            for _ in range(numberToAdd):
                color = random.choice(self.colors)
                pixel = random.randrange(0, self.parms.count)

                self.strip.set_pixel(pixel, color)
                twinkler = self.twinklers[pixel]
                twinkler.rgb = color
                twinkler.velocity = random.randint(1, 10)

            self.rest()
            self.strip.show()

        print('done running Twinkle')

    def updateTwinklers(self):

        index = 0
        for t in self.twinklers:
            twinkler = self.twinklers[index]

            reducedRgb = self.reduce(twinkler)
            if (self.isEffectivelyOff(reducedRgb)):
                reducedRgb = self.parms.black

            twinkler.rgb = reducedRgb
            self.strip.set_pixel(index, reducedRgb)

            index = index + 1

    def reducePart(self, val, velocity):
        return max(0, round(val - (self.reduction * velocity)))

    def reduce(self, twinkler: Twinkler):
        return (tuple(map(lambda x: self.reducePart(x, twinkler.velocity), twinkler.rgb)))

    def isEffectivelyOff(self, rgb):
        return (rgb[0] + rgb[1] + rgb[2]) < 30
