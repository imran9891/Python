#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Function Example</h3>

# In[ ]:


def checkDriverAge(age=0):
    age = int(input('What is your age?: '))
    if age < 18:
        print("Sorry, you are too young to drive this car. Powering Off!!")
    elif age > 18:
        print("Powering On. ENjoy the ride !!!")
    elif age==18:
        print("First ride. Enjoy!!")
checkDriverAge()

