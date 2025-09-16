import threading

'''
__new__ will be called when a new instance of the class is created, prior to __init__.
This allows us to control the instantiation process and ensure that only one instance of the class is created.
'''

class Singleton:
    _instance = None  # protected class attribute
    _lock = threading.Lock()  # class-level lock for thread safety

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, '_initialized'):
            self._value = value  # protected instance attribute
            self._initialized = True  # protected instance attribute

    def get_value(self):
        return self._value  # public method

    def set_value(self, value):
        self._value = value  # public method


if __name__ == "__main__":
    # Example usage
    singleton1 = Singleton(10)
    print(singleton1.get_value())  # Output: 10

    singleton2 = Singleton(20)
    print(singleton2.get_value())  # Output: 10 (still the same instance)

    singleton1.set_value(30)
    print(singleton2.get_value())  # Output: 30 (both refer to the same instance)
