from animation import Animation
from stripFactory import StripFactory
import time


class ColorWave(Animation):

    def __init__(self):
        Animation.__init__(self)

        numpix = self.parms.count

        stripFactory = StripFactory()

        self.strip = stripFactory.build()

        colors_rgb = [self.parms.electricPurple, self.parms.steelPink, self.parms.ultraPink,
                      self.parms.fuschia, self.parms.hollywoodCerise, self.parms.indigo, self.parms.violet]

        # same colors as normaln rgb, just 0 added at the end
        # colors_rgbw = [color+tuple([0]) for color in colors_rgb]
        # colors_rgbw.append((0, 0, 0, 255))

        colors = colors_rgb
        # uncomment colors_rgbw if you have RGBW strip
        # colors = colors_rgbw

        step = round(numpix / len(colors))
        current_pixel = 0

        for color1, color2 in zip(colors, colors[1:]):
            self.strip.set_pixel_line_gradient(
                current_pixel, current_pixel + step, color1, color2)
            current_pixel += step

        self.strip.set_pixel_line_gradient(
            current_pixel, numpix - 1, self.parms.violet, self.parms.electricPurple)

    # override
    def onRun(self, runFlag):
        print('starting to run ColorWave...')

        while runFlag():
            self.strip.rotate_right(1)
            time.sleep(self.refresh)
            self.strip.show()

        print('done running ColorWave')
