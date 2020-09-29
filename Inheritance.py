#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class User():
    def sign_in(self):
        print('logged in')

class Wizard(User):
        def __init__(self, name, power):
            self.name = name
            self.power = power

        def attack(self):
            print(f"attacking with power of {self.power}")
    
class Archer(User):
        def __init__(self, name, arrow):
            self.name = name
            self.arrow = arrow

        def attack(self):
            print(f"arrows left {self.arrow}")

wizard1 = Wizard('Imran', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()

print(isinstance(wizard1,Wizard))
print(isinstance(archer1,User))
print(isinstance(wizard1,object)) # object base class

