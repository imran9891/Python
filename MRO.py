#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Method Resolution Order 
class A:
    #pass
    num = 10
        
class B(A):
    pass

class C(A):
    #pass
    num = 1
    
class D(B,C):
    pass

print(D.num)
print(D.mro())

# print(D.num) # error-out
# D.__str__

