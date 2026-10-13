#method overriding
class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def work(self):
        print("Developer is writing code")
d = Developer()
d.work()
