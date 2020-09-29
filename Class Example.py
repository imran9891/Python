#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class rectangle():
    
    def __init__(self,width,height):
        self.width=width
        self.height=height
        
    def getwidth(self):
        return self.width
    
    def getheight(self):
        return self.height
    
    def getarea(self):
        area=self.width*self.height
        return area
    
    def getperimeter(self):
        per=2*self.width+2*self.height
        return per
    
    def enlarge(self,factor):
        self.width=self.width*factor
        self.height=self.height*factor
        
obj=rectangle(10,20)

print(obj.getwidth())
print(obj.getheight())
print(obj.getarea())
print(obj.getperimeter())

obj.enlarge(3)
print(obj.getwidth())
print(obj.getheight())
print(obj.getarea())
print(obj.getperimeter())

obj.enlarge(4)
print(obj.getwidth())
print(obj.getheight())
print(obj.getarea())
print(obj.getperimeter())

