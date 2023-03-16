import random


class Palette:
    def __init__(self, colors: list, initialColor):
        self.colors = colors.copy()
        self.count = len(self.colors)
        self.currentColor = initialColor if initialColor != None else random.choice(
            self.colors)
        self.previousColor = self.currentColor

    def getNextRandomColor(self):
        if (len(self.colors) < 2):
            return self.currentColor

        lastColor = self.currentColor

        while lastColor == self.currentColor:
            self.currentColor = random.choice(self.colors)

        self.previousColor = lastColor
        return self.currentColor

    def getColors(self):
        return self.colors.copy()
