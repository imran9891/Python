#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    try:
        age = int(input('What is your Age: '))
        10/age
        # raise ValueError('hey cut it out')
    except ValueError:
        print("Please enter the number")
        
    except ZeroDivisionError:
        print("Please enter age higher than 0")
        
    else:
        print("Thank you !!!")
        break
    finally:
        print('Ok! I\'m finally done')
print('Can you hear me?')

