#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Functions</h3>

# In[ ]:


# Positional Parameters
def say_hello(name, age):
    print(f'Hi {name}, your age is {age}')
    
# Default Parameters
def say_hello2(name="jojo", age=25):
    print(f'Hi {name}, your age is {age}')

# Positional Arguments
say_hello("imran", 27)          # Function call

# Default Arguments
say_hello2()
say_hello2("imran")

# Keyword Arguments
say_hello(age = 89, name = "YOHO")

