import EsraQasemi_python_L2_02 as classes

my_user = classes.User("","","")
users_list = my_user.users_list

my_store = classes.store()  #to recall this class 
list_store = my_store.list_of_products #renaming the list

cart = classes.cart() #to racall the class

while True :
    try:
        print("1.sign in")
        print("2.log in")
        print("3.End code")
        choise = int(input("enter your choise: "))
        print("")
    except TypeError:
        print("enter the number of your choise")
        continue

    match choise:

        case 1:
            role = ""
            while role not in ['customer','customer','manager','Manager']:
                role = input("Enter your role: (Manager/Customer) ")
            user_name = input("Enter your UserName: ")
            password = input("Enter your password: ")

            my_user.sign_in(role,user_name,password)
            print("")

        case 2:
            try:
                user_name = input("Enter your UserName: ")
                password = input("Enter your password: ")
                my_user.login(user_name,password)
            except ValueError: #the ValueError is raised manually in login function
                continue
            else:
                pass
            print("")

        case 3:
            break

        case _:
            print("invalid input!")
            print("")
            continue

    for user in users_list:
        while user.is_logged_in:
            if user.role in ["Manager","manager"]:
                try:
                    print("Manager menu")
                    print("1. add a product")
                    print("2. see the store products")
                    print("3. back to main menu")
                    choise = int(input("Enter your choise: "))
                    print("")
                except TypeError:
                    print("enter the number of your choise")
                    continue

                match choise:
                    case 1:
                    #giving input to creat a new product
                        try:
                            product_name = input("Enter the name of product: ")
                            product_price = input("Enter the price of product: ")
                            product_stock = int(input("Enter the stock quantity: "))
                        except TypeError:
                            print("enter an appropriate number for stock")

                    #creating an object of class product and adding it to list store
                        new_product = classes.product(product_name, product_price, product_stock)
                        my_store.add_product(new_product)
                        print("added successfully")
                        print("")

                    #here the manager can see the list of store products
                        print("َShop products:")
                        for index,object in enumerate(list_store):
                            print(f"{index+1}. {object}")
                        else:
                            print("")  

                    case 2:
                    #to show list of products
                        print("َShop products:")
                        for index,object in enumerate(list_store):
                            print(f"{index+1}. {object}")
                        else:
                            print("")  

                    case 3:
                    #it breaks the current loop and backs to main menu
                        user.is_logged_in = False

                    case _:
                        print("invalid input!")


            elif user.role in ["customer","Customer"]:
                print("..Welcome to our shop..")
                print("")
                
                print("Available products:")
                for index,product in enumerate(list_store):
                    print(f"{index+1}. {product}")
                else:
                    print("")

                while True:
                    try:
                        print("what do you want to do?")
                        print("1. add item to cart")
                        print("2. remove item from cart")
                        print("3. view cart")
                        print("4. checkout")
                        print("5. return to main menu")
                        task = int(input("Enter the number of your choise: "))
                        print("")
                    except TypeError:
                        print("enter a valid choise")


                    match task:

                    #adding product to cart
                        case 1:
                            try:
                                item_name = input("enter the product name: ")
                                quantity = int(input("enter the quantity: "))
                                cart.add_to_cart(item_name, quantity, my_store)
                                print(f"{item_name} was added to cart successfuly.")
                                print("")
                            except TypeError:
                                print("enter a valid number as quantity")

                    #removing a product from cart
                        case 2:
                            item_name = input("enter the product name: ")
                            cart.remove_from_cart(item_name, my_store)
                            print(f"{item_name} was removed from cart successfuly.")
                            print("")

                        case 3:
                            cart.view_items()

                        case 4:
                            cart.Checkout()

                    #to go back to main menu
                        case 5:
                            user.user_logout()
                            user.is_logged_in = False
                            break

    





        



