from ui_component import UIComponent
from ui_mediator import UIMediator

class Label(UIComponent):
    def __init__(self, mediator: 'UIMediator'):
        super().__init__(mediator)
        self._text = ""

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        print("Label value: {}".format(value))
        self._text = value
