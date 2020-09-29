#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
    with open("./Files/test.txt", mode='r') as my_file: 
        print(my_file.read())
except FileNotFoundError as err:
    print('File does not exist ',err)
    # raise err
except IOError as err:
    print('IO ERROR',err)
    # raise err

