from animation import Animation
from neopixel import Neopixel
import time

class ColorWave(Animation):
    
    def __init__(self):
        Animation.__init__(self)
        
        numpix = 300
        self.strip = Neopixel(numpix, 0, 5, "GRB")
        # strip = Neopixel(numpsix, 0, 0, "GRBW")

        electricPurple = (196, 0, 255)
        steelPink = (200, 39, 178)
        ultraPink = (251, 98, 246)
        fuschia = (255, 0, 255)
        hollywoodCerise = (251, 0, 162)
        indigo = (100, 0, 90)
        violet = (200, 0, 100)
        colors_rgb = [electricPurple, steelPink, ultraPink, fuschia, hollywoodCerise, indigo, violet]

        # same colors as normaln rgb, just 0 added at the end
        colors_rgbw = [color+tuple([0]) for color in colors_rgb]
        colors_rgbw.append((0, 0, 0, 255))

        # uncomment colors_rgbw if you have RGBW strip
        colors = colors_rgb
        # colors = colors_rgbw


        step = round(numpix / len(colors))
        current_pixel = 0
        self.strip.brightness(50)

        for color1, color2 in zip(colors, colors[1:]):
            self.strip.set_pixel_line_gradient(current_pixel, current_pixel + step, color1, color2)
            current_pixel += step

        self.strip.set_pixel_line_gradient(current_pixel, numpix - 1, violet, electricPurple)
        
    # override
    def onRun(self, runFlag):
        print('starting to run ColorWave...')
        
        while runFlag():
            self.strip.rotate_right(1)
            time.sleep(self.refresh)
            self.strip.show()
            
        print('done running ColorWave')
        
