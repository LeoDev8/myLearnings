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


