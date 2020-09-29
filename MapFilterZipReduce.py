#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Map
def multiply_by2(item):
    return item*2

print(map(multiply_by2, [1,2,3])) # returns map memory 
print(list(map(multiply_by2,[1,2,3]))) # no function calling

print(list(map(lambda x:x*2,[1,2,3])))
print(list(map(lambda x:x.upper(),['a','b','c'])))

print("\n")
# Filter
def only_odd(item):
    return item % 2 != 0
    
print(list(filter(only_odd,[1,2,3,4,5])))
print(list(filter(lambda x: x < 4, [1,2,3,4,5])))

print("\n")
# Zip
my_list = [1,2,3]
your_list = [10,20,30]
print(zip(my_list,your_list)) # returns memory address
print(list(zip(my_list,your_list))) # returns tuple inside the list

print("\n")
# Reduce
my_list = [1,2,3,4,5]
from functools import reduce
def accumulator(acc, item):
    print(acc,item)
    return acc + item

print(reduce(accumulator, my_list,0))   # function, iterable, initial
print(reduce(accumulator, my_list, 10))

