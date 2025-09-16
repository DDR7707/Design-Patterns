from abc import ABC, abstractmethod

class FitnessDataSubject(ABC):
    def __init__(self):
        self.observers = {}

    @abstractmethod
    def add_observer(name, location):
        pass

    def remove_observer(name):
        pass
