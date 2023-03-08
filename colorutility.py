class ColorUtility:
    def reducePart(colorPart, reduction, velocity=1):
        return max(0, round(colorPart - (reduction * velocity)))

    def reduce(rgb, reduction, velocity=1):
        return (tuple(map(lambda x: ColorUtility.reducePart(x, reduction, velocity), rgb)))

    def isEffectivelyOff(rgb):
        return (rgb[0] + rgb[1] + rgb[2]) < 30
