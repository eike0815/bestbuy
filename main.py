import products
import store
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]

pixel = products.Product("Google Pixel 7", price=500, quantity=250)
best_buy = store.Store(product_list)
thing = products.Product("thing", 234, 345)
best_buy.add_product(thing)
print(thing.active)



def menu():
    print("     Store Menu")
    print("     ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

def ordering():
    best_buy.get_all_products()
    print("When you want to finish order, enter empty text.")
    while True:
        article = int(input("which product # do you want: "))
        if article == "":
            break





def manual():
    while True:
        menu()
        user_wish = int(input("Please choose a number: "))
        if user_wish == 1:
            print("------")
            best_buy.get_all_products()
            print("------")
            print("\n")
        if user_wish == 2:
            best_buy.get_total_quantity()
        if user_wish == 3:
            pass
        if user_wish == 4:
            break

manual()

# setup initial stock of inventory

print(best_buy.get_all_products())
print(f" total in shop is {best_buy.get_total_quantity()}")
print(best_buy.order([("MacBook Air M2", 20)]))



def main():
    pass


if __name__ == '__main__':
    main()
