class Singleton:
    _instance = None

    def __init__(self, value):
        if Singleton._instance is not None:
            raise Exception("This class is a singleton!")
        Singleton._instance = self
        self.value = value

    @staticmethod
    def get_instance(value):
        if Singleton._instance is None:
            Singleton(value)
        return Singleton._instance

if __name__ == "__main__":
    # Example usage
    singleton1 = Singleton.get_instance(10)
    print(singleton1.value)  # Output: 10

    singleton2 = Singleton.get_instance(20)
    print(singleton2.value)  # Output: 10 (still the same instance)

    assert singleton1 is singleton2  # Both should be the same instance
