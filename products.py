class Product:
    def __init__(self, name, price, quantity):
        """
        this function initialises the object belonging to the class,
         as parameter it needs a name, a price and a quantity.
       when an object is created, it is automatically activated
        """
        self.name = name
        if name == "":
            raise ValueError("Every product needs valid name")
        self.price = price
        if price <=0:
            raise ValueError("Every product needs price higher than zero")
        self.quantity = quantity
        if quantity < 0:
            raise ValueError("A negative quantity is physically impossible")
        self.active = True


    def get_quantity(self):
        """
        the function returns the quantity of the given object.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        the function sets a new quantity to a given object.
        """
        try:
            self.quantity = quantity
            return quantity
        except ValueError:
            return
        except TypeError:
            print("this product doesn´t exist")

    def is_active(self):
        """
        the function checks if an object has  enough quantity to be/stay  activated.
        otherwise it deactivates the object.
        """
        if self.quantity <=0:
            self.deactivate()
        else:
            self.activate()
        return self.active


    def activate(self):
        """
        the function sets the object to active.
        """
        self.active = True
        return self.active


    def deactivate(self):
        """
        this function deactivates the object
        """
        self.active = False
        return self.active


    def show(self):
        """
        the function returns the object name, price and quantity
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """
        the function buy calculates the total price for the order of one product.
        it monitors the quantity and returns an error-message,
         if the quantity of order is higher than the stock in the shop.
        """
        if quantity > self.quantity:
            print(f"there is not enough {self.name} in stock")
        else:
            total_price = self.price * quantity
            new_quantity = self.quantity - quantity
            self.set_quantity(new_quantity)
            if self.quantity == 0:
                self.deactivate()
            return total_price

