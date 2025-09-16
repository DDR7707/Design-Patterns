# Iterator Design Pattern

The **Iterator** design pattern provides a way to access the elements of a collection sequentially without exposing its underlying representation.

## Intent

- Traverse a collection without exposing its internal structure.
- Provide a uniform interface for iteration.

## Structure

- **Iterator**: Defines an interface for accessing and traversing elements.
- **ConcreteIterator**: Implements the Iterator interface.
- **Aggregate**: Defines an interface for creating an Iterator object.
- **ConcreteAggregate**: Implements the Aggregate interface and returns an instance of the ConcreteIterator.

## UML Diagram

```
Aggregate ----> Iterator
    |               |
ConcreteAggregate   ConcreteIterator
```

## Example (Python)

```python
class Iterator:
    def __next__(self):
        pass

class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index < len(self._collection):
            item = self._collection[self._index]
            self._index += 1
            return item
        raise StopIteration

class Aggregate:
    def __iter__(self):
        pass

class ConcreteAggregate(Aggregate):
    def __init__(self, items):
        self._items = items

    def __iter__(self):
        return ConcreteIterator(self._items)

# Usage
aggregate = ConcreteAggregate([1, 2, 3])
for item in aggregate:
    print(item)
```

## Applicability

Use the Iterator pattern when:
- You need to traverse a collection without exposing its internal structure.
- You need multiple traversals of a collection.
- You need a uniform traversal interface for different types of collections.

## Related Patterns

- **Composite**
- **Factory Method**
