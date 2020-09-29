#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Single Inheritance Example Date is parent class and Time is Child Class:
class Date():
    def get_date(self):
        return '2020-07-10'
    
class Time(Date):
    def get_time(self):
        return '18:11:20'
    
dt = Date()
print(dt.get_date())
# print(dt.get_time())  # shows err since get_time attribute belongs to Time Class

tm=Time()
print(tm.get_date())
print(tm.get_time())

