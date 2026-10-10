class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name.upper()} says woof woof!")
d1 = Dog("venu",22)
d1.bark()
print(d1.name)
