class Animal:
    def __init__(self,name):
        self.name = name
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
d = Dog("tommy","labrador")
print(d.name)
print(d.breed)
