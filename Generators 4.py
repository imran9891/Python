#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Creating range using Generators
class MyGen():
    current = 0    # class object attribute
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __iter__(self):     # to iterate through the object
        return self
    
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1     # for next location
            return num
        raise StopIteration

gen = MyGen(0,5)
for i in gen:
    print(i, end=' ')  

# or check by the following codes
# iter(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))    # shows StopIteration

