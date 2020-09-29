#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def outer():
    x = 'outer' # string passed in variable x
    def inner():
        nonlocal x  # this won't create a new variable 'x', and will modify the parent 'x' only.
        x = 'inner'
        print("inner x: "+x)
    inner()
    print("outer x: "+x)

outer()

def outer2():
    x = 'outer'
    def inner2():
        x = 'inner'  # Here, not using non-local keyword 
        print("inner2 x: "+x)
    inner2()
    print("outer2 x: "+x)

outer2()

# nonlocal - it is used to access parent variables.

