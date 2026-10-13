class Person:
    def show_name(self):
        print("my name is venu")
class Employee(Person):
    def show_salary(self):
        print("salary is 30000")
class Developer(Employee):
    def show_role(self):
        print("iam a python developer")
d = Developer()
d.show_name()
d.show_salary()
d.show_role()
