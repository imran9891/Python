#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Modes:

# r: reading (by default)
# w: writing into a file & creates a new file it it doesn't exists
# a: append to the end of the file & creates a new file it it doesn't exists
# r+: read & write both

with open("Files/test.txt", mode='r+') as my_file:
    text = my_file.write('Hey! It\'s me. ')
    print(text) # writes to the file but at the start and overlaps

# with open("Files/test.txt", mode='a') as my_file:
#     text = my_file.write('Hope you are doing good.')
#     print(text) # writes to the file but at the end 

# with open("Files/test.txt", mode='w') as my_file:
#     text = my_file.write(':)')
#     print(text) # assumes file as new and write

# with open("Files/sad.txt", mode='r+') as my_file:
#     text = my_file.write(':)')
#     print(text) # returns FileNotFoundError

# with open("Files/sad.txt", mode='w') as my_file:
#     text = my_file.write(':)')
#     print(text) # creates a new txt file and write into it

# with open("Files/happy.txt", mode='a') as my_file:
#     text = my_file.write(':(')
#     print(text) # creates a new txt file and write into it

# with open("./Files/happy.py", mode='w') as my_file:  # File Paths ./ from the current folder
#     text = my_file.write(':(')
#     print(text) # creates a new txt file and write into it

