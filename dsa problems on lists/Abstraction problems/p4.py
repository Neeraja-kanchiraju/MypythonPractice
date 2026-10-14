from abc import ABC ,abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self,message):
        pass
class EmailNotification(Notification):
    def send(self,message):
        print("your ordef has been placed!")
class SMSNotification(Notification):
    def send(self,message):
        print("your ordef has been placed!")
e = EmailNotification()
e.send("your order has been placed!")
s = SMSNotification()
s.send("your order has been placed!")

