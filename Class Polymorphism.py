#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Polymorphism
class duck():
    def quack(self):
        print('quackkkk')
    
    def walk(self):
        print('walks like a duck')
        
    def bark(self):
        print('the duck cannot bark')
        
    def fur(self):
        print('the duck has feathers')
        
class dog():
    def bark(self):
        print('wooofff')
        
    def fur(self):
        print('the dog has white and brown fur')
        
    def walk(self):
        print('walks like a dog')
        
    def quack(self):
        print('dog cannot quack')
        
donald = duck()
fido = dog()
for i in (donald,fido):
    i.quack()
    i.walk()
    i.bark()
    i.fur()

