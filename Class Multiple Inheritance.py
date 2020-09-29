#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Multiple Inheritance
class A():
    def show1(self):
        print('This is Class A')

class B():
    def show2(self):
        print('This is Class B')
        
class C(A,B):
    def show3(self):
        print('This is Class C')
        
obj = C()
obj.show1()
obj.show2()
obj.show3()

