class Product:
    def __init__(self):
        self.__price = 500
    def set_price(self,price):
        if price > 0:
            self.__price = price
            print("price updated successfully")
        else:
            print("invalid price")
    def show_price(self):
        print(self.__price)
p = Product()
p.show_price()

p.set_price(800)
p.show_price()

p.set_price(-100)
p.show_price()
