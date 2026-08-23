class User:
#any info about the user
    def __init__(self, role:str , userName:str , password:str ):
        self.role = role
        self.userName = userName
        self.password = password
        is_logged_in = False

    def login(self, userName, password):
    #checking if input information is true, and logging in
        if self.userName==userName and self.password==password:
            is_logged_in = True
        else:
            print("user name or password is incorrect")
            is_logged_in = False



class product:
#'information' of 'each product' will be defined here
    def __init__(self, name:str , price:float ,stock:int):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Product Name:{self.name} _ Price:{self.price}$ _ Stock:{self.stock}"

class store:
    def __init__(self):
        self.prod_list = []
        #a list to store product objects in it

    def add_product(self, prod:product):
        self.prod_list.append(prod)


class cartItem:
#cart Items contain an object of product and quantity. then we save theme in a list of the next class
    def __init__(self, prod:product , quantity ):
        self.prod = prod
        self.quantity = quantity

    def __str__(self):
        return f"name:{self.prod.name} _ price:{self.prod.price} _ quantity:{self.quantity} _ total price:{int(self.prod.price)*int(self.quantity)} "

class cart:
#to define operations on cart
    def __init__(self):
        self.items = []
        #a list to store items of cart in it

    def add_to_cart(self, product_name:str, quantity:int, store):    
        for obj in store.prod_list:
            if obj.name == product_name:
            #when the wanted object found in store list

                #if an object of class cartItem, containing the product, exist in cart
                for i in self.items:
                    if i.prod == obj:
                        if i.prod.stock < quantity :
                            raise ValueError("Sorry, the product inventory is not enough")
                        else:
                            i.quantity += quantity
                            i.prod.stock -= quantity
                            print("{product_name} was added to cart successfuly")
                            return
                
                #when the product doesn't exist in cart and we have to creat an object for it      
                else: 
                    item = cartItem(obj, quantity)
                    self.items.append(item)
                    print(f"{product_name} was added to cart successfuly")
                    obj.stock -= quantity
                    return 
        else:
            print("Sorry, we don't have this product")
    """the first two lines find the object in store list
    if it's not availabe, the loop will end and else raises an error
    if it was foud, we ceck if there is the object in cart or not"""

            
    def remove_from_cart(self, product_name:str, store):
        for i in self.items:
            if i.prod.name == product_name:
                self.items.remove(i)
                for p in store.prod_list:
                    if p == i.prod:
                        p.stock += i.quantity
                #to find the product in store list and return its quantity
                print(f"{product_name} removed from cart successfuly")
                return
        else:
            raise ValueError("there isn't this item in your cart")
    """the first two lines find the object in store list
    if it's not availabe, the loop will end and else raises an error
    if it was foud, we remove it from item list and the next lines are about fixing stock of product object"""

    def view_items(self):
        for item,index in zip(self.items,range(len(self.items))):
            print(f"{index + 1}. ", item)
        print("")
        











        


        
        

                







    

        
