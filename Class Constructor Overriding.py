#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Constructor overriding:
class Person():
    def __init__(self,first,last):
        self.firstname=first
        self.lastname=last
    
    def Name(self):
        return self.firstname + " " + self.lastname
    
class Employee(Person):
    def __init__(self,first,last,staffnum):
        # Person.__init__(self,first,last)
        super().__init__(first,last)
        self.staffnum=staffnum
    def GetEmployee(self):
        return self.Name() + "," + self.staffnum

x = Person("Marge","Simpson")
print(x.Name())
y = Employee("Homer","Simpson","1007")
print(y.GetEmployee())
print(y.Name())

