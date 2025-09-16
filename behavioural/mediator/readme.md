# Mediator Design Pattern

The **Mediator** design pattern defines an object that encapsulates how a set of objects interact. It promotes loose coupling by preventing objects from referring to each other explicitly, allowing their interaction to be varied independently.

## Intent

- Centralize complex communications and control between related objects.
- Reduce dependencies between communicating objects.

## Structure

```
+-------------------+
|    Mediator       |
+-------------------+
         ^
         |
+-------------------+      +-------------------+
| ConcreteMediator  |<---->|   Colleague       |
+-------------------+      +-------------------+
```

- **Mediator**: Declares the interface for communication.
- **ConcreteMediator**: Implements cooperative behavior by coordinating Colleague objects.
- **Colleague**: Communicates with other Colleagues through the Mediator.

## Example

A chat room where users (Colleagues) send messages to each other via a central ChatRoom (Mediator).

```python
class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self):
        self.colleague1 = Colleague1(self)
        self.colleague2 = Colleague2(self)

    def notify(self, sender, event):
        if event == "A":
            self.colleague2.do_c()
        elif event == "B":
            self.colleague1.do_d()

class Colleague1:
    def __init__(self, mediator):
        self.mediator = mediator

    def do_a(self):
        self.mediator.notify(self, "A")

    def do_d(self):
        print("Colleague1 handles D")

class Colleague2:
    def __init__(self, mediator):
        self.mediator = mediator

    def do_b(self):
        self.mediator.notify(self, "B")

    def do_c(self):
        print("Colleague2 handles C")
```

## When to Use

- When a set of objects communicate in complex ways.
- When you want to avoid tight coupling between objects.

## Benefits

- Decouples colleagues.
- Centralizes control logic.

## Drawbacks

- Mediator can become complex if it handles too many interactions.

## References

- [Refactoring Guru: Mediator](https://refactoring.guru/design-patterns/mediator)
- [Gang of Four: Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns)


## My Notes
- Main idea is no 2 classes should initialize each other.
- In such cases, have a mediator which will handle transactions between those classes.
