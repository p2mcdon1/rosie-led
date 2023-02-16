from animation import Animation
import random
from stripFactory import StripFactory


class Twinkle(Animation):

    def __init__(self):
        Animation.__init__(self)

        stripFactory = StripFactory()
        self.strip = stripFactory.build()

        self.colors = self.parms.getColors(True)
        self.pixelRgbs = []

        for x in range(self.parms.count):
            self.pixelRgbs.append(self.parms.black)

        self.twinklers = []

    # override
    def onRun(self, runFlag):
        print('starting to run Twinkle...')

        while runFlag():
            self.updateTwinklers()

            for _ in range(random.randrange(0, 6)):
                color = random.choice(self.colors)
                pixel = random.randrange(0, self.parms.count)
                self.strip.set_pixel(pixel, color)
                self.pixelRgbs[pixel] = color

                if (color != self.parms.black and self.twinklers.count(pixel) < 1):
                    self.twinklers.append(pixel)

            self.rest()
            self.strip.show()

        print('done running Twinkle')

    def updateTwinklers(self):

        index = 0
        toRemove = []
        for t in self.twinklers:
            pixelRgb = self.pixelRgbs[t]
            if (pixelRgb == self.parms.black):
                toRemove.append(index)

            reducedRgb = self.reduce(pixelRgb)
            if (self.isEffectivelyOff(reducedRgb)):
                reducedRgb = self.parms.black

            self.pixelRgbs[t] = reducedRgb
            self.strip.set_pixel(t, reducedRgb)

            index = index + 1

        for i in toRemove:
            try:
                self.twinklers.pop(i)
            except:
                print(f"{i} does not exist")
                print('Twinklers:')
                print(*self.twinklers)
                print('ToRemove:')
                print(*toRemove)

    def reducePart(self, val):
        return round(val / 2)

    def reduce(self, rgb):
        return (self.reducePart(rgb[0]), self.reducePart(rgb[1]), self.reducePart(rgb[2]))

    def isEffectivelyOff(self, rgb):
        return rgb[0] + rgb[1] + rgb[2] < 50
