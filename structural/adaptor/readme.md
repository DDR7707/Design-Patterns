# Adapter Design Pattern

The **Adapter** (or **Adaptor**) design pattern is a structural pattern that allows objects with incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces by wrapping an existing class with a new interface.

## Intent

- Convert the interface of a class into another interface clients expect.
- Let classes work together that couldn't otherwise because of incompatible interfaces.

## Real-World Analogy
Imagine you're traveling from the United States to Europe. Your laptop charger uses a Type A plug (used in the US), but European wall sockets expect a Type C plug.

You can’t plug your charger in directly—the interfaces don’t match.

Instead of buying a new charger, you use a travel plug adapter. This device accepts your Type A plug and converts it into a Type C shape that fits into the European socket.

You don’t modify the wall socket (it’s like the third-party API).

You don’t modify your charger (it’s like your existing business logic).

The adapter sits in between and translates the connection.

For our example:

Charger → your application (CheckoutService)

Wall socket → third-party system (LegacyGateway)

Travel plug adapter → Adapter class (LegacyGatewayAdapter)

Your application expects one interface (PaymentProcessor), but the legacy system provides another (LegacyGateway). The adapter allows the two to work together—without altering either side.

## Structure

```
Client --> Target (interface)
                ^
                |
           Adapter
                |
           Adaptee (existing class)
```

## Participants

- **Target**: Defines the domain-specific interface used by the client.
- **Adapter**: Implements the Target interface and adapts the Adaptee to the Target.
- **Adaptee**: The existing class with an incompatible interface.
- **Client**: Collaborates with objects conforming to the Target interface.

## Example

Suppose you have a legacy `OldPrinter` class, but your application expects a `Printer` interface:

```python
class OldPrinter:
    def print_legacy(self, text):
        print(f"Legacy: {text}")

class PrinterAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def print(self, text):
        self.adaptee.print_legacy(text)

# Usage
printer = PrinterAdapter(OldPrinter())
printer.print("Hello, Adapter!")
```

## When to Use

- When you want to use an existing class, but its interface does not match the one you need.
- When you want to create a reusable class that cooperates with unrelated or unforeseen classes.

## Related Patterns

- **Facade**: Provides a simplified interface to a subsystem.
- **Decorator**: Adds responsibilities to objects dynamically.

## Links
- https://blog.algomaster.io/p/ce091479-c602-4c07-b7ba-315c643b31d8
