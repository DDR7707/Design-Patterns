# Observer Design Pattern

The Observer design pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

## Structure

- Subject: Maintains a list of observers and notifies them of state changes.
- Observer: Defines an updating interface for objects that should be notified of changes in a subject.
- ConcreteSubject: Stores state of interest to ConcreteObserver objects and sends notifications.
- ConcreteObserver: Implements the Observer interface to keep its state consistent with the subject.

## Example Use Cases

- Event handling systems (GUI frameworks)
- Model-View-Controller (MVC) architectures
- Distributed event-driven systems
- Kafka

## Benefits

- Loose coupling between subject and observers
- Dynamic subscription of observers

## Drawbacks

- Can lead to memory leaks if observers are not properly removed
- Notification order is not guaranteed

## References

- [Refactoring Guru: Observer Pattern](https://refactoring.guru/design-patterns/observer)
- [Wikipedia: Observer Pattern](https://en.wikipedia.org/wiki/Observer_pattern)
- [AlgoMaster: Observer Pattern](https://blog.algomaster.io/p/bc60ce42-3f17-486f-aa36-4bd5264837e8)

## Identification
- Broadcasting information.
