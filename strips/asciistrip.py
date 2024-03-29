from parms import Parms
from strips.stripbase import StripBase


class AsciiStrip(StripBase):
    def __init__(self, count):
        self.count = count
        self.parms = Parms()

        self.pixels = []
        for x in range(self.count):
            self.pixels.append(' ')

    def set_pixel_line_gradient(self, pixel1, pixel2, left_rgb_w, right_rgb_w):
        self.set_pixel(pixel1, left_rgb_w)
        self.set_pixel(pixel2, right_rgb_w)
        for i in range(pixel1 + 1, pixel2):
            self.set_pixel(i, (122, 122, 122))

    def set_pixel(self, pixel_num, rgb_w):
        self.pixels[pixel_num] = self.__getChar(rgb_w)

    def rotate_left(self, num_of_pixels):
        if num_of_pixels == None:
            num_of_pixels = 1
        self.pixels = self.pixels[num_of_pixels:] + self.pixels[:num_of_pixels]

    def rotate_right(self, num_of_pixels):
        if num_of_pixels == None:
            num_of_pixels = 1
        num_of_pixels = -1 * num_of_pixels
        self.pixels = self.pixels[num_of_pixels:] + self.pixels[:num_of_pixels]

    def show(self):
        print(''.join(self.pixels), end="\r")

    def __getChar(self, rgb):
        if (rgb == self.parms.black):
            return '#'

        if (AsciiStrip.__isLight(rgb)):
            return '-'

        match rgb:
            case self.parms.red:
                return 'R'
            case self.parms.green:
                return 'G'
            case self.parms.blue:
                return 'B'
            case self.parms.orange:
                return 'O'
            case self.parms.purple:
                return 'P'
            case self.parms.yellow:
                return 'Y'

        return 'X'

    def __isLight(rgb):
        total = rgb[0] + rgb[1] + rgb[2]
        if (total < 50):
            return True

        return False
