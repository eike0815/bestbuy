import products


class Store:
    def __init__(self, product_list):
        """
        this function initiates the store
        """
        self.product_list = product_list


    def add_product(self, product):
        """
        this function adds a product object to the store
         by appending it to the store-list(product_list)
        """
        products.product = product
        self.product_list.append(product)


    def remove_product(self, product):
        """
        this function removes a product.
        it takes a product-list as an input and returns a product-list
        without the chosen product.

        """
        self.product_list.remove(product)


    def get_total_quantity(self):# -> int
        """
        this function counts the total quantity of all products in the store.
        it takes a product list and returns an integer.
        """
        total = 0
        for product in range(len(self.product_list)):
            total += self.product_list[product].quantity
        print(f"Total of {total} items in store")


    def get_all_products(self):
        """
        this function checks the status of each product and
        prints afterward the active products of the store.
        to do so it communicates with the "quantitative" functions of the product class
        """
        print("------")
        counter = 1
        for index in range(len(self.product_list)):
            if self.product_list[index].is_active():
                print(f"{counter}.", end=" ")
                print(f"{self.product_list[index].name},"
                       f" Price: ${self.product_list[index].price}, "
                        f"Quantity: {self.product_list[index].quantity}")
                counter += 1
        print("------")


    total = 0
    def order(self, shopping_list):
        """
        this function is handed a shopping list and by using the buy function from the product class, it
        adds all the prices for the products to one full total amount.
        """
        for index in range(len(shopping_list)):
            for topic in range(len(self.product_list)):
                if shopping_list[index][0].name == self.product_list[topic].name:
                    try:
                        Store.total += self.product_list[topic].buy(shopping_list[index][1])
                    except TypeError:
                        return
        print("*********")
        print(f"Order made! Total payment: ${Store.total}")
