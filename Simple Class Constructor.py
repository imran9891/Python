#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Data initialize using constructor __init__():

class rectangle():
    def __init__(self,h,b):
        self.h=h
        self.b=b
    def height(self):
        return self.h
    def width(self):
        return self.b
    def area(self):
        return self.h*self.b
    
d=rectangle(10,5)      # object created

print(d.height())
print(d.width())
print(d.area())

