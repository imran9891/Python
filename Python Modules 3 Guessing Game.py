#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Guessing Game
import sys
import random
answer = random.randint(1,10)
while True:
    try:
        guess = int(input("Enter any number between 1-10: "))
        if guess != answer:
            print('Try Again')
            continue
        else:
            print('You won')
            break
    except ValueError:
        print('Please enter only numbers')
# pypi ~ python package index

