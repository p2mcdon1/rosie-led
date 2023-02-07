from animation import Animation
import time

class Mouse(Animation):
    # override
    def run(self, runFlag):
        print('starting to run Mouse...')
        while runFlag():
            print('Mouse is running...')
            time.sleep(2)
        
        print('done running Mouse')