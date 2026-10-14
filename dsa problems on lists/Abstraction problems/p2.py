from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calculate_area(self):
        area = self.length * self.width
        return area
r = Rectangle(10,5)
result = r.calculate_area()
print(result)
