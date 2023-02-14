from colorwave import ColorWave
from key import KeyReader
from mouse import Mouse
import _thread
import time

class Runner:
    def __init__(self):
        self.runAnimation = True
        self.checkRun = lambda : self.runAnimation
        self.baton = _thread.allocate_lock()
        self.colorWave = ColorWave()
        self.mouse = Mouse()
        self.keyReader = KeyReader()
        self.selector = True

    def __runColorWave(self):
        self.colorWave.run(self.checkRun, self.baton)

    def __runMouse(self):
        self.mouse.run(self.checkRun, self.baton)

    def __switch(self):
        print('switching...')

        if self.runAnimation:
            self.runAnimation = False
            self.baton.acquire()
            self.runAnimation = True
            self.baton.release()

        self.selector = not self.selector
        self.runAnimation = True
        if self.selector:
            _thread.start_new_thread(self.__runColorWave, ())
        else:
            _thread.start_new_thread(self.__runMouse, ())

    def run(self):
        while True:
            pushed = self.keyReader.wasPushed()
            
            if pushed:
                self.__switch()
            
            time.sleep(0.2)
        
        print('end main loop')
    