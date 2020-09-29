#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from functools import reduce

# 1. Capitalize all of the pet names and print the list
my_pets = ['sisi','bibi','titi','carla']
print(list(map(lambda x: x.upper(), my_pets)))

# 2. Zip the 2 lists into a list of tuples, but sort the numbers from lowest ot highest
my_strings = ['a','b','c','d','e']
my_numbers = [5,4,3,2,1]
print(list(zip(my_strings, sorted(my_numbers))))

# 3. Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(lambda x: x > 50, scores)))

# 4. Combine all of the numbers that are in a list  on this list using reduce (my_numbers and scores). What is the total?
def total(acc, item):
    return acc + item
print(reduce(total, (my_numbers + scores),0))

