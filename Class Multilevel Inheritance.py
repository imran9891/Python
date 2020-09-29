#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Multilevel Inheritance: (1 Base Class, 1 Derived Class, 1 Sub-Derived)
class Animals():
    def __init__(self,name):
        self.name=name
        
    def eat(self,food):
        print("%s is eating %s" %(self.name,food))
        
class Dog(Animals):
    def fetch(self,thing):
        print("%s goes after the %s" %(self.name,thing))
        
class Cat(Dog):
    def swatstring(self):
        print("%s shreds the string" %(self.name))
        
f=Cat('fluffy')
f.eat('cat food')
f.fetch('paper')
f.swatstring() 

