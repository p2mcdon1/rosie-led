from abc import ABC, abstractmethod

class Animation(ABC):
    @abstractmethod
    def run(self, runFlag):
        pass