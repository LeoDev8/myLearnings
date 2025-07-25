# Class Inheritance

class Parent:
    attribute = 1
    def __init__(self, name):
        self.name = name
    def method1(self, param1):
        print(f"Parent Class attribute: {self.attribute}")
        return param1

class Child(Parent):
    attribute = 2
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class MyClass:
    def __init__(self):
        self.__secret = "hidden"

    def __private_method__(self):
        print("This is a private method")

    def public_method(self):
        print("Calling private method from public method:")
        # self.__private_method()
