#!/usr/bin/env python
# coding: utf-8

# <h3 align="center">Dictionary Method 3</h3>

# In[ ]:


user = {
        "name": "imran",
        "sex": "M",
        "age": 25
        }

print("imran" in user.items()) # items is a (key, value) pair
print("sex" in user)

print("imran" in user.values())
print("sex" in user.keys())

print(user.items())     # returns a list containing a tuple for each key value pair

print(user.clear())     # removes all items in a dictionary & returns None
print(user)             # returns empty dictionary

print("\n")

user2 = {
        "name": "pepy",
        "sex": "F",
        "age": 45
        }

print(user2.pop("age")) # removes value at the given key
print(user2)

print(user2.update({"sex": "M"}))
print(user2)

print(user2.update({"size": 32}))
print(user2)

print(user2.popitem())  # it randomly pops an item
print(user2)

print(user2.keys())
print(user2.values())

print("\n")
user3 = {
        'age': 25, 
        'username': "imran", 
        'weapons': ["gun"], 
        'is_active': True,
        'clan': "army"
        }

user3['weapons'].append('shield')
user3["weapons"] = user3["weapons"] + ["pistol"] # Dict is mutable
print(user3)

