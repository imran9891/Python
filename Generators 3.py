#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            print("Stopped")
            break
    
special_for([1,2,3])

# same as doing above
# iterator = iter([1,2,3])
# next(iterator)
# next(iterator)
# next(iterator)
# print(next(iterator))

