from abc import ABC, abstractmethod

class Animation(ABC):

    def __init__(self):
        self.refresh = 0.5

    @abstractmethod
    def run(self, runFlag):
        pass