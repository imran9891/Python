#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Cat:
    species = "mammal" # class-object attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# Instantiate the cat object with 3 cats
obj1 = Cat('Kali Billi',23)
obj2 = Cat('Gori Billi',24)
obj3 = Cat('Mast Billi',25)

# Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(args)
    
# Print out: "The oldest cat is x years old." x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldest_cat(obj1.age, obj2.age, obj3.age)} years old.")

