from abc import ABC, abstractmethod

class RequestHandler(ABC):
    def __init__(self):
        self.successor = None

    def set_successor(self, successor):
        self.successor = successor

    def pass_next_handler(self, request):
        if not self.successor:
            return
        self.successor.handle(request)

    @abstractmethod
    def handle(self):
        pass
