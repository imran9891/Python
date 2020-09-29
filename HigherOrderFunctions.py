#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Higher Order Function (HOF) is a function which returns another function,
# or accepts another function example: map, filter, reduce

def greet(func):
    func()
    return 'imran'
    
def greet2():
    def hello():
        print("hello!")
    return hello()
print(greet(greet2))

