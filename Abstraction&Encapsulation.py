#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def run(self):
        print('run')
        
    def speak(self):
        print(f'my name is {self.name} and i\'m {self.age} years old')
    
player1 = PlayerCharacter('imran',25)  # object instantiated
player1.speak()

