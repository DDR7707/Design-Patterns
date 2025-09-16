# Command Design Pattern

The **Command** design pattern is a behavioral pattern that turns a request into a stand-alone object containing all information about the request. This allows you to parameterize methods with different requests, queue or log requests, and support undoable operations.

## Structure

- **Command**: Declares an interface for executing an operation.
- **ConcreteCommand**: Implements the Command interface and defines a binding between a Receiver and an action.
- **Client**: Creates a ConcreteCommand object and sets its receiver.
- **Invoker**: Asks the command to carry out the request.
- **Receiver**: Knows how to perform the operations associated with carrying out a request.

## UML Diagram

```
Client --> Invoker --> Command --> ConcreteCommand --> Receiver
```

## Example

```python
# Command interface
class Command:
    def execute(self):
        pass

# Receiver
class Light:
    def turn_on(self):
        print("Light is ON")

# ConcreteCommand
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.turn_on()

# Invoker
class RemoteControl:
    def __init__(self, command):
        self.command = command
    def press_button(self):
        self.command.execute()

# Usage
light = Light()
command = LightOnCommand(light)
remote = RemoteControl(command)
remote.press_button()
```

## When to Use

- To parameterize objects with operations.
- To queue, log, or support undoable operations.
- To decouple the object that invokes the operation from the one that knows how to perform it.

## Benefits

- Decouples sender and receiver.
- Supports undo/redo.
- Supports logging and transaction systems.

## Related Patterns

- **Chain of Responsibility**
- **Mediator**
- **Observer**
