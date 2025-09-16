# Strategy Design Pattern

The **Strategy Pattern** is a behavioral design pattern that enables selecting an algorithm's behavior at runtime. It defines a family of algorithms, encapsulates each one, and makes them interchangeable. This pattern lets the algorithm vary independently from clients that use it.

## Structure

- **Context**: Maintains a reference to a Strategy object.
- **Strategy**: Common interface for all supported algorithms.
- **ConcreteStrategy**: Implements the Strategy interface.


## The Problem: Shipping Cost Calculation
Imagine you're building a shipping cost calculator for an e-commerce platform.

As with most real-world applications, shipping charges can vary based on different business rules or external providers.

Here are some common strategies you may need to support:

Flat Rate: A fixed fee (e.g., $10 per shipment), regardless of weight or destination.

Weight-Based: Cost is calculated as a fixed amount per kilogram.

Distance-Based: Different rates depending on destination zones (e.g., Zone A = $5, Zone B = $12).

Third-Party API: Fetch dynamic rates from providers like FedEx or UPS.

A quick and naive solution might be to implement all of this logic inside a single class, using a long chain of conditionals:
- Violates the Open/Closed Principle
- Bloated Conditional Logic
- Difficult to Test in Isolation
- Risk of Code Duplication


## Example (Python)

```python
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return list(reversed(data))

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.execute(data)

# Usage
data = [3, 1, 2]
context = Context(ConcreteStrategyA())
print(context.execute_strategy(data))  # [1, 2, 3]
context.set_strategy(ConcreteStrategyB())
print(context.execute_strategy(data))  # [2, 1, 3]
```

## When to Use

- When you have multiple related algorithms for a specific task.
- When you want to avoid using conditional statements for selecting behaviors.
- When you want to make algorithms interchangeable and easily extendable.

## Benefits

- Promotes open/closed principle.
- Eliminates conditional statements.
- Allows dynamic switching of algorithms.

## Drawbacks

- Increases the number of classes.
- Client must be aware of different strategies.

## Related Patterns

- **State Pattern**: Similar structure, but strategies represent states.
- **Decorator Pattern**: Can be used to add responsibilities to strategies.
