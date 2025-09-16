def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Singleton:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


if __name__ == "__main__":
    # Example usage
    singleton1 = Singleton(10)
    print(singleton1.get_value())  # Output: 10

    singleton2 = Singleton(20)
    print(singleton2.get_value())  # Output: 10 (still the same instance)

    singleton1.set_value(30)
    print(singleton2.get_value())  # Output: 30 (both refer to the same instance)
