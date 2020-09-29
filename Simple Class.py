#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class duck():
    def walk(self):
        print('Walk like a duck')
    def quack(self):
        print('Quackkkk')

donald=duck()
donald.walk()
donald.quack()

# Types of Method:
# 1. Instance Method
# 2. Static Method

# 1. Instance Method
class duck():
    def walk(donald1):    # instead of self objectname(instance) is given
        print('Walk like a duck')
    def quack(self):
        print('Quackkkk')
        
donald1=duck()
donald2=duck()

donald1.walk()
donald1.quack()
donald2.walk()
donald2.quack()

# 2. Static Method
class duck():
    def walk(self):
        print('Walk like a duck')
    @staticmethod
    def quack():
        print('Quackkkk')
        
donald1=duck()
donald2=duck()

donald1.walk()
donald1.quack()
duck.quack()
donald2.walk()
donald2.quack()

