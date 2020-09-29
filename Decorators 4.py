#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        return f'{t2-t1} sec'
    return wrapper

@performance
def long_time():
    for i in range (1000000):
        i*5

long_time()
# performance(long_time)()  # same as doing above

