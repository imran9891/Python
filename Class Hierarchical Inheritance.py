#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Hierarchical Inheritance: (1 Base Class, 2 Derived Class)
class Animals():
    def __init__(self,name):
        self.name=name
        
    def eat(self,food):
        print("%s is eating %s" %(self.name,food))
        
class Dog(Animals):
    def fetch(self,thing):
        print("%s goes after the %s" %(self.name,thing))
        
class Cat(Animals):
    def swatstring(self):
        print("%s shreds the string" %(self.name))
        
r=Dog('rover')
f=Cat('fluffy')

r.fetch('paper')
f.swatstring()
r.eat('dog food')
f.eat('cat food')

