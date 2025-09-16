from abc import ABC, abstractmethod

class FitnessDataObservers(ABC):
    @abstractmethod
    def data_action(data):
        pass
