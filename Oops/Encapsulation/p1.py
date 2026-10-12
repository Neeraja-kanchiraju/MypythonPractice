#private variables can access with methods
class BankAccount:
     def __init__(self,balance):
         self.__balance = balance
     def show_balance(self):
         print(self.__balance)
account = BankAccount(1000)
account.show_balance()
