# Factory Design Pattern

The **Factory Design Pattern** is a creational pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

## Intent

- Encapsulate object creation logic.
- Promote loose coupling by eliminating the need to bind application-specific classes into the code.
- Client code and Concrete classes are loosely coupled.

## Structure

```
Creator (Factory)
│
├── Factory Method
│
└── Product (Interface/Abstract Class)
    ├── ConcreteProductA
    └── ConcreteProductB
```

## Participants

- **Product**: Defines the interface of objects the factory method creates.
- **ConcreteProduct**: Implements the Product interface.
- **Creator (Factory)**: Declares the factory method.
- **ConcreteCreator**: Overrides the factory method to return an instance of a ConcreteProduct.

## When to Use

- When a class can't anticipate the class of objects it must create.
- To delegate responsibility of instantiation to subclasses.

## Advantages

- Promotes code reusability and scalability.
- Reduces tight coupling between code and specific classes.

## Related Patterns

- Abstract Factory
- Singleton
- Builder

## Potential doubts
1) Why we need creator class which just returns Concrete class?. We can directly use that object in demo right!?
Encapsulation of Creation Logic: The Creator class encapsulates the logic for creating specific types of notifications. If the creation process becomes more complex (e.g., setting defaults, dependencies, or configuration), it is managed in one place.

Decoupling: The demo code does not need to know the details of how each notification is created. It only interacts with the Creator interface, making the code more modular and easier to maintain.

Extensibility: If you want to add new types of notifications, you can simply add new Creator classes without changing the demo or other client code.

Adherence to Open/Closed Principle: The pattern allows you to extend the system with new notification types without modifying existing code, which is a key principle of good software design.

Testing and Reusability: Creation logic can be reused and tested independently from the rest of the application.

In summary, the Creator class is useful for managing object creation, especially as the system grows or the creation process becomes more complex. For very simple cases, it may seem like extra code, but it pays off as requirements evolve.
