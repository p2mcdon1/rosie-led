class Colors:
    def adjustPart(colorPart, adjustment, velocity=1):
        return min(255, max(0, round(colorPart + (adjustment * velocity))))

    def adjust(rgb, adjustment, velocity=1):
        return (tuple(map(lambda x: Colors.adjustPart(x, adjustment, velocity), rgb)))

    def adjustPartWithMax(colorPart, adjustment, maximum):
        return min(maximum, max(0, round(colorPart + adjustment)))

    def adjustWithLimit(rgb, adjustment, limitRgb):
        r = Colors.adjustPartWithMax(
            rgb[0], adjustment, limitRgb[0])
        g = Colors.adjustPartWithMax(
            rgb[1], adjustment, limitRgb[1])
        b = Colors.adjustPartWithMax(
            rgb[2], adjustment, limitRgb[2])

        return (r, g, b)

    def isEffectivelyOff(rgb):
        return (rgb[0] + rgb[1] + rgb[2]) < 30
