# Decorator Design Pattern

The **Decorator** pattern is a structural design pattern that allows behavior to be added to individual objects, dynamically, without affecting the behavior of other objects from the same class.

## Intent

- Attach additional responsibilities to an object dynamically.
- Provide a flexible alternative to subclassing for extending functionality.

## Structure

```
Component
    ↑
ConcreteComponent
    ↑
Decorator
    ↑
ConcreteDecorator
```

- **Component**: Interface for objects that can have responsibilities added.
- **ConcreteComponent**: The original object to which new functionalities can be added.
- **Decorator**: Maintains a reference to a Component object and defines an interface conforming to Component's interface.
- **ConcreteDecorator**: Adds responsibilities to the component.

## Example (Python)

```python
class Coffee:
     def cost(self):
          return 5

class MilkDecorator:
     def __init__(self, coffee):
          self._coffee = coffee

     def cost(self):
          return self._coffee.cost() + 2

coffee = Coffee()
milk_coffee = MilkDecorator(coffee)
print(milk_coffee.cost())  # Output: 7
```

## When to Use

- To add responsibilities to objects without subclassing.
- When extension by subclassing is impractical.

## Advantages

- More flexible than static inheritance.
- Responsibilities can be added or removed at runtime.

## Disadvantages

- Can result in many small objects.
- Complexity increases with many decorators.

## Related Patterns

- Adapter
- Composite
- Proxy
