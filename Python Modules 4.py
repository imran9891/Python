#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Hashable modules
from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]
print(Counter(li))
char = 'my name is imran and i am machine learning expert'
print(Counter(char))

print("\n")
my_dict = {'a':1, 'b':2}
print(my_dict['a'])
# print(my_dict['c'])   # shows keyerror

print("\n")
my_dict2 = defaultdict(lambda: 'does not exists',{'a':1,'b':2})
# print(int())   # returns 0
print(my_dict2['b'])
print(my_dict2['c'])

print("\n")
my_dict3 = OrderedDict({'e':2,'b':0,'m':4,'a':1})
my_dict4 = OrderedDict({'e':2,'b':0,'m':4,'d':1})
print(my_dict3 == my_dict4)     # returns False since order discrepancy

print("\n")
# A dictionary in python has no sense of order but recently it has changed to Ordered
my_dict5 = {'e':2,'b':0,'m':4,'a':1}
my_dict6 = {'b':0,'a':1,'e':2,'m':4}
print(my_dict5 == my_dict6)     # returns True

