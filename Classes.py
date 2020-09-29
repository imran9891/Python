#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class PlayerCharacter:
    membership = True   # class object attribute (actual static attribute)
    def __init__(self, name, age):    # constructor method automatically called 
        self.name=name   # attributes
        self.age=age
        
    def shout(self):
        print(f'my name is {self.name} & i\'m {self.age} years old')
        return 'done'
    
    @classmethod   # can be accessed without creating object
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)
    
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2
    
print(PlayerCharacter.adding_things(2,3))
player1 = PlayerCharacter.adding_things(2,3) # not instantiate object
print(player1.age)
print(player1.name)
           
player2 = PlayerCharacter("imran",25)   # object instantiated
print(player2.shout())
print(player2.adding_things2(5,5))

print(PlayerCharacter.membership)
print(player1.membership)
print(player2.membership)

