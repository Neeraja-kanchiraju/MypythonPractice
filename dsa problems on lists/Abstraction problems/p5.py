from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self,name,monthly_salary):
        self.name = "venu"
        self.monthly_salary = 50000
    def calculate_salary(self):
        annual_salary = self.monthly_salary * 12
        print(annual_salary)
f = FullTimeEmployee("venu",50000)
f.calculate_salary()
