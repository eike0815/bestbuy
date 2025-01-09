import products
#product_list
class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        self.product = product
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self):# -> int
        total = 0
        for product in range(len(self.product_list)):
            total += self.product_list[product].quantity
        print(f"Total of {total} items in store")

    def get_all_products(self):
        all_products = filter(products.Product.is_active , self.product_list)
        print('this are all products:')
        for product in all_products:
            print(f"Name: {product.name} , Price: {product.price}, Quantity: {product.quantity}")

    def order(self, shopping_list):  #
        for index in range(len(shopping_list)):
            for topic in range(len(product_list)):
                if shopping_list[index][0] == product_list[topic].name:
                    total_price = product_list[topic].price * 3
                    new_quantity = product_list[topic].quantity - shopping_list[index][1]
                    if new_quantity >= 0:
                        print(total_price)
                        print(new_quantity)
                    else:
                        print("THERE IS NOT ENOGUH PRODUCT TO PELASE your ORDER")


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

#store = Store(product_list)
#print(store.product_list[2].name)
#store = Store(product_list)
#shoing_list = [("MacBook Air M2", 20),("Google Pixel 7", 20)]
#store.order(shoing_list)
#print(f'this are all products: {store.get_all_products()}') #hier fehlt ein retunt?
#products.Product.get_quantity()
"""
store = Store(product_list)
products = store.get_all_products()
print(store.get_total_quantity())
print([(product_list[0].name, 1), (product_list[1].name, 2)])
shoing_list = [("MacBook Air M2", 20),("Google Pixel 7", 20)]
store.order(shoing_list)




#bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=0)
#mac = products.Product("MacBook Air M2", price=1450, quantity=100)
thing= products.Product("thing", price=123, quantity= 20)
#store = Store([bose, mac, thing])
#pixel = products.Product("Google Pixel 7", price=500, quantity=100)
#store.add_product(pixel)
#print(store.product_list[2].name)
#print(store.list_of_products[0].name)
#print(store.order([(products[0], 1), (products[1], 2)]))
#store.add_product(mac)
#print(store)
#print(bose.name)
#print(store.add_product(thing))
#store.remove_product(thing)
#print(store.get_total_quantity())
#store.get_all_products()


#print(store.order([(store.product_list[2].name,3),(store.product_list[1].name,4)]))
"""
bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=0)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)
thing= products.Product("thing", price=123, quantity= 0)
store = Store([bose, mac, thing])
pixel = products.Product("Google Pixel 7", price=500, quantity=100)
store.add_product(pixel)
store.get_all_products()
shoing_list = [("MacBook Air M2", 20),("Google Pixel 7", 20)]
store.order(shoing_list)