import products
import store
pro_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]

pixel = products.Product("Google Pixel 7", price=500, quantity=250)
best_buy = store.Store(pro_list)
thing = products.Product("thing", 234, 345)
best_buy.add_product(thing)
#print(best_buy.product_list[0].name)




def menu():
    print("     Store Menu")
    print("     ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def ordering():
   # artikel=1
    best_buy.get_all_products() #hieraus den input artikel bauen,
    shopping_list = []
    print("When you want to finish order, enter empty text.")
    while True:
            article = input("which product # do you want? ")
            amount = input("what amount do you want? ")
            if amount == "" and article == "":
                print("empty") #hier best_buy.get_order(shopping_list)
            else:
                article = int(article)
                #print(type(article))
                amount = int(amount)
                product = (best_buy.get_all_products()[article-1], amount)
                if product == ():
                    print(product)
                    shopping_list.append(product)
                    print(shopping_list)


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
            ordering()
        if user_wish == 4:
            break

manual()



def main():
    pass


if __name__ == '__main__':
    main()
