from colorwave import ColorWave
from key import KeyReader
from mouse import Mouse
import queue
import threading
import time

class Runner:
    def __init__(self):
        self.runAnimation = True
        self.checkRun = lambda : self.runAnimation
        self.t1 = None

        self.colorWave = ColorWave()
        self.mouse = Mouse()
        self.keyReader = KeyReader()

        self.selector = True

    def __runColorWave(self):
        self.colorWave.run(self.checkRun)

    def __runMouse(self):
        self.mouse.run(self.checkRun)


    def __switch(self):
        print('switching...')

        self.runAnimation = False
        if self.t1 != None:
            self.t1.join()

        self.selector = not self.selector
        if self.selector:
            self.t1 = threading.Thread(target=self.__runColorWave, args=())
        else:
            self.t1 = threading.Thread(target=self.__runMouse, args=())

        self.runAnimation = True
        self.t1.start()

    def run(self):
        while True:
            input = ''
            try:
                input = self.keyReader.keyQueue.get_nowait()
            except queue.Empty:
                input = 'empty'

            if input == 'c':
                self.__switch()
            elif input == self.keyReader.stop():
                print('main is stopping...')

                self.runAnimation = False
                if self.t1 != None:
                    self.t1.join()

                print('child thread has joined')
                break

            time.sleep(0.10)
        
        print('end main loop')
    