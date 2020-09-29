#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# def make_list(num):
#     li = []
#     for i in range(num):
#         li.append(i*2)
#     return li

# print(make_list(100))

# iterable: which can be looped through
# iterate: process
# generators: are actually iterables. 
# Every generator is iterable but not every iterable is generator
# ex. range (generator), list(iterable)
# Generator is a subset of iterable

def generator_function(num):
    for i in range(num):
        yield i          # pauses the function

for item in generator_function(1000):
    print(item, end=',')

# g = generator_function(4)
# next(g)
# next(g)
# print(next(g)) # StopIteration Error: if we do next() after range expires
    

