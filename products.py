class Product:
    def __init__(self, name, price, quantity):
        try:
            self.name = name
        except TypeError:
            print("product needs valid name")
        if price <0.01:
            print("this price is invalid")
        else:
            self.price = price
        if quantity < 0:
            print("there is logically no product")
        else:
            self.quantity= quantity
        self.active = True


    def get_quantity(self)-> float:
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        return quantity

    def is_active(self):
        if self.quantity <=0:
            self.deactivate()
        else:
            self.activate()
        return self.active


    def activate(self):
        self.active = True
        return self.active

    def deactivate(self):
        self.active = False
        return self.active

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        "MacBook Air M2, Price: 1450, Quantity: 100"



    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            print(f"there is not enough {self.name} in stock")
            return
        else:
            total_price = self.price * quantity
            new_quantity = self.quantity - quantity
            self.set_quantity(new_quantity)
            return total_price, new_quantity

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=00)

print(bose.is_active())
"""
mac = Product("MacBook Air M2", price=1450, quantity=100)
print(mac.buy(100))
print(mac.is_active())

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
print(bose.deactivate)

bose.set_quantity(1000)
print(bose.show())
"""