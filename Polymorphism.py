#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class User():
    def __init__(self, email):
        self.email = email
        
        
    def sign_in(self):
        print('logged in')
    
        
    def attack(self):
        print('do nothing')

class Wizard(User):
        def __init__(self, name, power, email):
            super().__init__(email)     # super class attribute
            self.name = name
            self.power = power
            

        def attack(self):
            User.attack(self)     # calling attack() of User class
            print(f"attacking with power of {self.power}")
    
class Archer(User):
        def __init__(self, name, arrow):
            self.name = name
            self.arrow = arrow
            

        def attack(self):
            print(f"arrows left {self.arrow}")

wizard1 = Wizard('Imran', 50, 'imranekbal9891@gmail.com')
archer1 = Archer('Robin', 10)

# def player_attack(char):           # Polymorphism
#     char.attack()

# player_attack(wizard1)
# player_attack(archer1)

for char in [wizard1,archer1]:      # Polymorphism 
    char.attack()

print(dir(wizard1))                 # Object Introspection
wizard1.attack()
print(wizard1.email)

