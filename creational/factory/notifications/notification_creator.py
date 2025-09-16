from abc import ABC, abstractmethod

class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self):
        """Create a notification instance."""
        raise NotImplementedError("This method should be overridden by subclasses")
