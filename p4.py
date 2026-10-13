class Father:
    def skills1(self):
        print("father knows farming")
class Mother:
    def skills2(self):
        print("mother knows cooking")
class Child(Father,Mother):
    def own_skills(self):
        print("child knows coding")
c = Child()
c.skills1()
c.skills2()
c.own_skills()
