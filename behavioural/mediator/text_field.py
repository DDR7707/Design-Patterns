from ui_component import UIComponent
from ui_mediator import UIMediator

class TextField(UIComponent):
    def __init__(self, mediator: UIMediator):
        super().__init__(mediator)
        self._text = ""
        self._enabled = True

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        print('Setting value: {}'.format(value))
        self.notify_mediator()

    @property
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value
