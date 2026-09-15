class User:
    def __init__(self, role:str , userName:str , password:str ):
        self.role = role
        self.userName = userName
        self.password = password
        self.is_logged_in = False
        self.cart_items = []


    users_list = []

    def login(self, userName, password):
    #checking if input information is true, and logging in
        try:
            for user in self.users_list:
                if user.userName==userName and user.password==password:
                    user.is_logged_in = True
                    break
            else:
                raise ValueError
        except:
            print("user name or password is incorrect")
            user.is_logged_in = False


    def sign_in(self, role, userName, password):
        try:
            for user in self.users_list:
                if user.userName == userName and user.password == password:
                    raise ValueError("already signed in")
            else:
                user = User(role, userName, password)
                self.users_list.append(user)
        except ValueError:
            print("already signed in")

    def user_logout(self):
        for user in self.users_list:
            if user.is_logged_in:
                for item in user.cart_items:
                    for product in store.list_of_products:
                        if item == product:
                            product.stock += item.quantity
                user.cart_items.clear()  

class product:
#information of each product will be defined here
    def __init__(self, name:str , price:float ,stock:int):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Product Name:{self.name} _ Price:{self.price}$ _ Stock:{self.stock}"

class store:
    def __init__(self):
        self.list_of_products = []
        #a list to store product objects in it

    def add_product(self, product:product):
        try:
            if product in self.list_of_products:
                raise ValueError
            else:
                self.list_of_products.append(product)
        except:
            print("the product already exists")


class cartItem:
#cart Items contain an object of product and quantity. then we save theme in a list of the next class
    def __init__(self, product:product , quantity ):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f"name:{self.product.name} _ price:{self.product.price} _ quantity:{self.quantity} _ total price:{int(self.product.price)*int(self.quantity)} "

class cart:
#to define operations on cart

    def add_to_cart(self, product_name:str, quantity:int, store):  
        for user in User.users_list:
            if user.is_logged_in:  
                for the_product in store.list_of_products:
                    if the_product.name == product_name:
                    #it means the wanted object found in store list

                        #when an object of class cartItem, exists in cart
                        try:
                            for i in user.cart_items:
                                if i.product == the_product:
                                    if i.product.stock < quantity :
                                        raise ValueError("Sorry, the product inventory is not enough")
                                    else:
                                        i.quantity += quantity
                                        i.product.stock -= quantity
                                        print("{product_name} was added to cart successfuly")
                                        return
                        except:
                            print("Sorry, the product is out of stock")
                
                #when the product doesn't exist in cart and we have to creat an object for it      
                else: 
                    item = cartItem(the_product, quantity)
                    user.cart_items.append(item)
                    the_product.stock -= quantity
                    return 
        else:
            print("Sorry, we don't have this product")

            
    def remove_from_cart(self, product_name:str, store):
        for user in User.users_list:
            if user.is_logged_in: 
                for item in user.cart_items:
                    if item.product.name == product_name:
                        user.cart_items.remove(item)
                    #to find the product in store list and return its quantity
                        for product in store.list_of_products:
                            if product == item.product:
                                product.stock += item.quantity
                        return
        else:
            print("there isn't this item in your cart")

        
    def view_items(self):
        for user in User.users_list:
            if user.is_logged_in:
                if not user.cart_items:
                    print("still empty..")
                else:
                    for index, item in enumerate(user.cart_items):
                        print(f"{index+1}. ", item)
                    print("")


    def Checkout(self):
        for user in User.users_list:
            if user.is_logged_in: 
                if user.cart_items:
                    print("--cart--")
                    self.view_items()
                    confirm = input("Are you sure you want to chechout? (y/n)")

                    if confirm.lower() != "y" :
                        print("checkout cancelled!")
                        print("")
                        return

                    else:
                        user.cart_items.clear()
                        print("Thanks for shopping:)")
                else:
                    print("cart is empty")

