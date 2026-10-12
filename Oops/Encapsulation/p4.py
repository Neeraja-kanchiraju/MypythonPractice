class Employee:
    def __init__(self):
        self.__salary = 25000
    def get_salary(self):
        return self.__salary
    def set_salary(self,amount):
        if amount > 0:
           self.__salary += amount
        else:
            print("Invalid salary")
e = Employee()
print(e.get_salary())
e.set_salary(5000)
print(e.get_salary())
