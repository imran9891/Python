#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Each .py file is a module
# While importing a module a " __pycache__" file is generated
# Import either package (folder) or modules 

import Modules.utility
import Modules.shopping_cart
if __name__ == '__main__':
    print(Modules.shopping_cart.buy('apple'))
    print(Modules.utility.div(10,2))
    print(Modules.utility.mul(5,5))
    

# Different ways to Import Modules
# from Modules.shopping_cart import buy
# from Modules.utility import mul, div
# print(buy('kela'))
# print(mul(2,3))
# print(div(5,2))

class Student:
    pass

st1 = Student()
print(type(st1))   # <class '__main__.Student'>
# print(type(utility.st1))  # <class '__utility__.Student'>

