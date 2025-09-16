from abc import ABC

class UIComponent(ABC):
    def __init__(self, mediator):
        self.mediator = mediator

    def notify_mediator(self) -> None:
        self.mediator.component_changed(self)
