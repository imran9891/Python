#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Tuples</h3>

# In[ ]:


my_tuple = (1,2,3,4,5,2)
print(my_tuple[0])
print(my_tuple[1:2])    # be careful here, we also get a 'comma' when we just store a single tuple value
print(my_tuple[0:2])
print(my_tuple[::-2])
print(2 in my_tuple)

# my_tuple[0] = 4     # it will be an error, because tuple are immutable
print(my_tuple)

print(my_tuple.count(2))
print(my_tuple.index(5))

my_dict = {
    "age": 45,
    (1,2): "hello"    # passing tuple as key
    }
print(my_dict)
print(my_dict.items())   # returns key:value pair as a tuple inside the list
print(my_dict[(1,2)])

a,b,c,*other = (1,2,3,4,5,6,7,8,9)  # it stores as list if the variable has more than 1 item, otherwise as int.
print(a)
print(type(a))
print(other)
print(type(other))

