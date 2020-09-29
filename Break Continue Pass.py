#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Break Continue Pass</h3>

# In[ ]:


for i in range(10):
    print(i)
    break
    
# 'continue' will skip the lines below it and continue to loop.
for i in range(0,5): # 0,1,2,3,4
    print(i)
    continue
    print("I will never be printed")
    
for i in range (10):
    pass    # it can be used to avoid error and when we have not yet decided on the code to write.

