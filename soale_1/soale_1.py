# Straightforward implementation of the Singleton Pattern
class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


# The object is created on the first call to the class
a = Singleton()

# But the second call returns the same instance. The message “Creating the object” does not print, nor is a different object returned
b = Singleton()
print(a)
print(b)
print(a is b)
