#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Depth First Search : Algorithm for MRO
class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass
print(M.__mro__)

