
class Student:
    def __init__(self,):
        self.__marks = 80
    def show_marks(self):
        print(self.__marks)
    def set_marks(self,marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
            print(self.__marks)
            print("updated marks")
        else:
            print("invalid marks")
student = Student()
student.show_marks()
student.set_marks(95)
