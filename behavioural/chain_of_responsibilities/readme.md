# Chain of Responsibility Design Pattern

The **Chain of Responsibility** pattern is a behavioral design pattern that allows an object to pass a request along a chain of handlers. Each handler can either process the request or pass it to the next handler in the chain.

## Intent

- Decouple sender and receiver of a request.
- Allow multiple objects to handle the request without specifying the handler explicitly.

## Structure

```
Client → Handler1 → Handler2 → Handler3 → ...
```

- **Handler**: Defines an interface for handling requests and optionally maintains a reference to the next handler.
- **ConcreteHandler**: Handles requests it is responsible for or forwards them to the next handler.

## Example

```python
class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if self.successor:
            self.successor.handle(request)

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            print("Handled by A")
        else:
            super().handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("Handled by B")
        else:
            super().handle(request)

# Usage
handler_chain = ConcreteHandlerA(ConcreteHandlerB())
handler_chain.handle("B")  # Output: Handled by B
```

## When to Use

- When multiple objects can handle a request and the handler is not known a priori.
- When you want to issue a request to a chain of objects.

## Advantages

- Reduces coupling between sender and receiver.
- Adds flexibility in assigning responsibilities.

## Drawbacks

- Request may go unhandled if no handler processes it.
- Can be hard to follow the flow of requests.

## Related Patterns

- **Decorator**
- **Command**
- **Observer**
- **Composite**

---

**References:**
- [Refactoring Guru: Chain of Responsibility](https://refactoring.guru/design-patterns/chain-of-responsibility)
- [Gang of Four: Design Patterns](https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern)
- [AlgoMaster](https://algomaster.io/learn/lld/chain-of-responsibility)


## My Notes
- When a request is supposed to flow through different handlers. Eg: API request through Authentication, Autherization, RateLimiting, Data Validation, BussinessLogic.

- You can write if-else logics but that will contradict below principles:
    - Open Closed principle.
        - When new handlers is introduced, you need to change your core code.
    - All handlers are tightly coupled into one single class which violates Single responsibility principle.
    - If we want to resue any handlers in other places, we can't.
    - If you want to skip authentication in dev environment, you need to write even more if-else.

- Apparently, any changes in adding or removing or changing the order of handlers should be handled through client code.
