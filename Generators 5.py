#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Fibonnaci using for loop
a,b = 0,1
limit = int(input("Enter the limit upto which u want fs: "))
for i in range(limit):
    temp = a
    a = b
    b = temp + b
    print(temp,end=' ')
print("\n")

# Using Generation function
def fib(num):
    a,b = 0,1
    limit = int(input("Enter the limit upto which u want fs: "))
    for i in range(limit):
        yield a         # temporary holds the value of a (0)
        temp = a
        a = b
        b = temp + b

for x in fib(21):
    print(x, end=' ')   

