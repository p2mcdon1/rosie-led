from animation import Animation
import sys
import time

class Bounce(Animation):

    def __init__(self):
        self.count = 160
        self.logSize = 10
        self.step = 2
        self.sleep = 0.01
        
    # override
    def run(self, runFlag):
        print('starting to run Bounce...')
        self.items = numpy.zeros(self.count, numpy.ubyte)

        logRight = -self.logSize
        logLeft = logRight - self.logSize

        rightToLeft = True

        while runFlag():

            if (rightToLeft):
                for x in range(0, self.step):
                    rightIndex = logRight - x
                    leftIndex = logLeft - x
                    if (rightIndex >= 0 and rightIndex < (self.count - 1)):
                        self.items[rightIndex] = 1
                    if (leftIndex >= 0 and leftIndex < (self.count - 1)):
                        self.items[leftIndex] = 0
                
                self.__printItems()
                logRight = logRight + self.step
                logLeft = logLeft + self.step

                if (logRight > (self.count + self.logSize)):
                    rightToLeft = False
            else:
                for x in range(0, self.step):
                    rightIndex = logRight + x
                    leftIndex = logLeft + x
                    if (rightIndex >= 0 and rightIndex < (self.count - 1)):
                        self.items[rightIndex] = 0
                    if (leftIndex >= 0 and leftIndex < (self.count - 1)):
                        self.items[leftIndex] = 1
                
                self.__printItems()
                logRight = logRight - self.step
                logLeft = logLeft - self.step

                if (logRight < 0):
                    rightToLeft = True

            time.sleep(self.sleep)
        
        print('done running Bounce')
