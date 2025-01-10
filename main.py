import products
import store


pro_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
dingens =  products.Product("dingens", 23, 34)
best_buy = (store.Store(pro_list))
best_buy.add_product(dingens)
best_buy.remove_product(dingens)

def menu():
    print("     Store Menu")
    print("     ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def ordering():
    best_buy.get_all_products()
    shopping_list = []
    print("When you want to finish order, enter empty text.")
    while True:
            article = input("which product # do you want? ")
            amount = input("what amount do you want? ")
            if amount == "" and article == "":
                best_buy.order(shopping_list)
                break
            else:
                article = int(article)
                amount = int(amount)
                try:
                    prod = best_buy.product_list[article-1]
                    product = (prod, amount)
                    shopping_list.append(product)
                    print("Product added to list!")
                except IndexError:
                    print("Error adding product!")


def manual():
    while True:
        menu()
        user_wish = int(input("Please choose a number: "))
        if user_wish == 1:
            best_buy.get_all_products()
            print("\n")
        if user_wish == 2:
            best_buy.get_total_quantity()
        if user_wish == 3:
            ordering()
        if user_wish == 4:
            break


def main():
    manual()


if __name__ == '__main__':
    main()
