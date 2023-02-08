from animation import Animation
import time

class ColorWave(Animation):
    # override
    def onRun(self, runFlag):
        print('starting to run ColorWave...')
        while runFlag():
            print('ColorWave is running...')
            time.sleep(self.refresh)
        
        print('done running ColorWave')