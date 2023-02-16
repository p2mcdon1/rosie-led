class Parms:
    def __init__(self):
        self.count = 300
        self.refresh = 0.01
        self.brightness = 50
        self.ledDataPin = 5
        self.electricPurple = (196, 0, 255)
        self.steelPink = (200, 39, 178)
        self.ultraPink = (251, 98, 246)
        self.fuschia = (255, 0, 255)
        self.hollywoodCerise = (251, 0, 162)
        self.indigo = (100, 0, 90)
        self.violet = (200, 0, 100)
        self.black = (0, 0, 0)

    def getColors(self, withBlack: bool = False):
        colorList = [self.electricPurple, self.steelPink, self.ultraPink,
                     self.fuschia, self.hollywoodCerise, self.indigo, self.violet]

        if (withBlack):
            colorList.append(self.black)

        return colorList
