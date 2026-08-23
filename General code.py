import EsraQasemi_python_L2_02 as classes

my_store = classes.store()  #to recall this class 
list_store = my_store.prod_list #renaming the list

cart = classes.cart() #to racall the class
cart_items = cart.items #renaming the list

while True :

    role = input("Please select your role. Manager / Customer (or Exit to end the code): ")
    print("")
    #authentication
    if role not in ["Manager","Customer","Exit"]:
        raise ValueError("invalid input!")
    elif role == "Exit":
        break

    if role == "Manager" :
        print("..manager menu..\n")

    while role == "Manager" :
        print("to add the product..")
        print("Enter 0 to change role")
        product_name = input("Enter the name of product: ")
        if product_name == "0":
            break
        product_price = input("Enter the price of product: ")
        if product_price == "0":
                    break
        product_stock = int(input("Enter the stock quantity: "))
        if product_stock == "0":
                    break

    #creating an object of class object and adding it to list store
        new_prod = classes.product(product_name, product_price, product_stock)
        my_store.add_product(new_prod)

    #here the manager can see the list of store products
        print("َShop products:")
        print("added successfuly.\n")
        for obj in list_store:
            print(obj)
        else:
            print("")     


    if role == "Customer":
         print("..Customer Menu..")
         print("welcome\n")
         
    while role == "Customer":

    #showing information to user
        print("Available products:")
        for obj in list_store:
            print(obj)
        else:
            print("")

    #getting input about what is the user going to do
        print("what do you want to do?")
        print("1. add item to cart")
        print("2. remove item from cart")
        print("3. view cart")
        print("4. return to main menu \n")
        task = int(input("Enter character of your choise: "))

    #adding product to cart
        if task == 1:
            item_name = input("enter the product name: ")
            quantity = int(input("enter the quantity: "))
            cart.add_to_cart(item_name, quantity, my_store)
            print(f"{item_name} added successfuly.")

    #removing an object from cart
        if task == 2:
            item_name = input("enter the product name: ")
            cart.remove_from_cart(item_name, my_store)
            print(f"{item_name} was removed from cart successfuly.")

        if task == 3:
            cart.view_items()

    #to go back of customer's loop
        if task == 4:
            break

        





        



