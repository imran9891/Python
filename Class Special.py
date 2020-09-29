#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class M():
    def __init__(self,d):
        self.d=d
    def square(self):
        return self.d*self.d
    
class N():
    def __init__(self,d):
        self.d=d
    def cube(self):
        return self.d*self.d*self.d
    
m = M(3)
print(type(M))
print(m.__class__)
print(m.square())
# print(m.cube())  # shows err since M obj has no attribute cube

m.__class__ = N
print(m.cube())
print(m.__class__)
# print(m.square())  # shows err since M now obj has no attribute square

