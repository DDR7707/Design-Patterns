# State Design Pattern

The **State** design pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class. This pattern is useful for implementing state machines and managing state-dependent behavior.

## Intent

- Encapsulate varying behavior for the same object based on its internal state.
- Allow an object to change its behavior without changing its class.

## Structure

```
+----------------+        +----------------+
|    Context     |<>------|    State       |
+----------------+        +----------------+
| - state: State |        | + handle()     |
| + request()    |        +----------------+
+----------------+                ^
                                   |
                        +----------------------+
                        | ConcreteStateA       |
                        +----------------------+
                        | + handle()           |
                        +----------------------+
                        | ConcreteStateB       |
                        +----------------------+
                        | + handle()           |
                        +----------------------+
```

## Participants

- **Context**: Maintains an instance of a ConcreteState subclass.
- **State**: Defines an interface for encapsulating behavior associated with a particular state.
- **ConcreteState**: Implements behavior associated with a state of the Context.

## Example

```python
class State:
    def handle(self, context):
        pass

class ConcreteStateA(State):
    def handle(self, context):
        print("State A: Handling request.")
        context.state = ConcreteStateB()

class ConcreteStateB(State):
    def handle(self, context):
        print("State B: Handling request.")
        context.state = ConcreteStateA()

class Context:
    def __init__(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)

# Usage
context = Context(ConcreteStateA())
context.request()  # State A: Handling request.
context.request()  # State B: Handling request.
```

## When to Use

- When an object's behavior depends on its state and it must change its behavior at runtime.
- When operations have large, multipart conditional statements that depend on the object's state.
- When there are multiple stages for an object. Like vending machine which can be in Idle, SelecteItem, InsertCoin, DispenseItem, ReturnChange states.
- When we can't mix up states. You can't jump from Idel state to InsertCoin state.
- When not to use: When there are less states. Eg: on and off, parking lot where it can be either empty/occupied.
- Very intutive to get confused with strategy design pattern. There its algorithm or logic which is been changing, not behavior due to state/stage change.

## Related Patterns

- **Strategy**: Similar structure, but strategies are interchangeable algorithms, not states.
- **Flyweight**: Can be combined to share state objects.

## References

- [Gang of Four, *Design Patterns: Elements of Reusable Object-Oriented Software*]
- [Refactoring Guru - State Pattern](https://refactoring.guru/design-patterns/state)

## Important Notes
- All methods should be present in every class which is inheriting from base abstract state class.
- Errors/warnings should be raised for unindented functions in concrete classes.
- When initializing concreteState classes, we need to pass in context class as attributes so that we can trigger state changes from concreteClasses to context class.
