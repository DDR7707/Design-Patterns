from ui_component import UIComponent
from ui_mediator import UIMediator

class Button(UIComponent):
    def __init__(self, mediator: 'UIMediator'):
        super().__init__(mediator)
        self._enabled = True

    @property
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        print("Button value: {}".format(value))
        self._enabled = value

    def click(self) -> None:
        if self._enabled:
            self.notify_mediator()
