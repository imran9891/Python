#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# create shopping cart objects

class shoppingcart():
    items_in_cart={}       # Class-object attribute
    
    def __init__(self,customer_name):
        self.customer_name=customer_name
        
    def add_items(self,product,price):
        if not product in self.items_in_cart:
            self.items_in_cart[product]=price
            print(product + ' added')
        else:
            print(product + ' is already in the cart')
                  
    def remove_items(self,product):
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + ' removed')
        else:
            print(product + ' is not in the cart')
                  
    def show_items(self):
        return self.items_in_cart
                  
def main():
    
        my_cart=shoppingcart('Imran')
        my_cart.add_items('Laptop',58000)
        my_cart.add_items('Cars',1000000)
        my_cart.add_items('Bike',120000)
        print(my_cart.show_items())
        my_cart.remove_items('Laptop')
        my_cart.remove_items('Bike')
        print(my_cart.show_items())
    
main()

