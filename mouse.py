from animation import Animation
import time

class Mouse(Animation):
    # override
    def onRun(self, runFlag):
        print('starting to run Mouse...')
        while runFlag():
            print('Mouse is running...')
            time.sleep(self.refresh)
        
        print('done running Mouse')