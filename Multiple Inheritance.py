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

        def check_arrow(self):
            print(f"{self.arrow} remaining")
            
        def run(self):
            print('ran really fast')

class HybridBorg(Wizard, Archer):
     def __init__(self, name, power, arrow):
         Archer.__init__(self, name, arrow)
         Wizard.__init__(self, name, power)
    

hb1 = HybridBorg('borgie', 50, 100)

hb1.check_arrow()
hb1.attack()
hb1.sign_in()

