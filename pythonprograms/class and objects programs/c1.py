class ClassName:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sample_method(self):
        print(self.name.upper())
c1 = ClassName("ravi",20)
print(c1.name,c1.age)
c1.sample_method()
