class Person:
    def __init__(self, name="", age=0):
        self._name = name
        self.age = age

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        self.name = value
    
    def __str__(self):
        return f"Name: {self._name}\nAge: {self.age}"