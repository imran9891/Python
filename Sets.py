#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Sets</h3>

# In[ ]:


my_set = {1,2,3,4,5,5,5}
my_set.add(100)     # add 100 at the last index
my_set.add(2)       # add 2 at the next index of 100
print(my_set)
# print(my_set[0])  # we cannot do this, it produces an error, because set is an unordered collection of objects
print(len(my_set))

print(5 in my_set)
print(my_set)

print(list(my_set))     # converted to list

new_set = my_set.copy()
print(my_set.clear())   # returns None
print(my_set)           # returns empty set()
print(new_set)

my_list = [1,2,3,4,5,5,5]
print(set(my_list))     # this way we can remove the duplicate items from the list
# Sets doesn't support indexing

