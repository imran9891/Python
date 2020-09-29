#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Booleans
# </h3>

# In[ ]:


is_cool = True
is_cool = False
print(bool(-0)) # F
print(bool(0)) # F
print(bool(1)) # T
print(bool(0.5)) # T
print(bool('0')) # T
print(bool('True')) # T
print(bool('False')) # T
print(bool(False)) # F
print(bool('any random thing')) # T

# All values are considered "truthy" except for the following, which are "falsy":
#     None
#     False
#     0
#     0.0
#     0j
#     Decimal(0)
#     Fraction(0, 1)
#     [] - an empty list
#     {} - an empty dict
#     () - an empty tuple
#     '' - an empty str
#     b'' - an empty bytes
#     set() - an empty set
#     an empty range, like range(0)
#     objects for which
#         obj.__bool__() returns False
#         obj.__len__() returns 0

