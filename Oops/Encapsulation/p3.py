
class BankAccount:
    def __init__(self):
        self.__balance = 1000
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print("deposited successfull")
        else:
            print("Invalid amount")
    def show_balance(self):
        print(self.__balance)
b = BankAccount()
b.deposit(500)
b.show_balance()
