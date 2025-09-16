Inheritance vs composition
Composition: 'Has-in'
class Engine:
    def start(self):
        return "Engine starts"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an Engine

    def start(self):
        return self.engine.start()  # Delegates the start action to the Engine

# Usage
my_car = Car()
print(my_car.start())  # Output: Engine starts
