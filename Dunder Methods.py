#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# It's a bad practise to modify the dunder methods since dunder methods are predefined for a
# particular purpose
class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'YOYO',
            'has_pets': False
        }
    
    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return 5
    
    def __call__(self):
        return 'yess?'
    
    def __getitem__(self,i):
        return self.my_dict[i]
    
action_figure = Toy('red',0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])

