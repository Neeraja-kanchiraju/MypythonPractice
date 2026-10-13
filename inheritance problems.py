class Vehicle:
    def start(self):
        print("vehicle started")
class Car(Vehicle):
    def drive(self):
        print("car is driving")
c = Car()
c.start()
c.drive()
