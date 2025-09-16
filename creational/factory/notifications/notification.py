from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        """Send a notification with the given message."""
        raise NotImplementedError("This method should be overridden by subclasses")
