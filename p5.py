


class Employee:
    def show_company(self):
        print("working at ABC company")
class Developer(Employee):
    def write_code(self):
        print("writing code")
class Tester(Employee):
    def test_code(self):
        print("Testing code")
d = Developer()
t = Tester()
d.write_code()
t.test_code()
d.show_company()
