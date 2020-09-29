#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Method Overloading:
class Human():
    def sayHello(self,name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello')
            
obj=Human() 
obj.sayHello()            # method call
obj.sayHello('Imran')     # method call with parameter

