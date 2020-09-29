#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func

@my_decorator
def hello(name, age):
    print(f"Hello {name}, your age is {age}.")
    
@my_decorator   
def logged_in(username):
    print(f"{username} is logged in.")

hello("imran", 25)
logged_in("imran")

# using decorator is same as doing the below:
# my_decorator(hello)()

