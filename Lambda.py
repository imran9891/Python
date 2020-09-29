#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# One line functions
print(list(map(lambda x:x**2, [1,2,3])))
print(list(map(lambda x:x**2, (10,2,3))))
print(list(filter(lambda x:x % 20 == 0, [10,20,30,40,50])))
print(reduce(lambda acc,item : acc + item, [1,2,3], 0))

# List Sorting via index 2
a = [(0,2),(4,-3),(9,9),(10,-1)]
print(sorted(a, key= lambda x: x[1]))

