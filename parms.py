class Parms:
    count = 300
    pink = False

    def __init__(self):
        self.count = Parms.count
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
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)
        self.orange = (255, 165, 0)
        self.purple = (255, 0, 255)
        self.yellow = (255, 255, 0)

    def getColors(self, withBlack: bool = False):

        if (Parms.pink):
            colorList = [self.electricPurple, self.steelPink, self.ultraPink,
                         self.fuschia, self.hollywoodCerise, self.indigo, self.violet]
        else:
            colorList = [self.red, self.green, self.blue,
                         self.orange, self.purple, self.yellow]

        if (withBlack):
            colorList.append(self.black)

        return colorList
