#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f"Please enter numbers {err}")

sum(1,0)
sum(1,'2')
sum(1,2)

