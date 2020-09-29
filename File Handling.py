#!/usr/bin/env python
# coding: utf-8

# In[ ]:


my_file = open("Files/test.txt")

print(my_file)

print(my_file.read())         # read complete file
my_file.seek(0)               # seeks to the start of the cursor

print(my_file.readline())     # read single line
print(my_file.readlines())    # read whole file in the list form

my_file.close()               # close the file

# standard way to read a file:
with open("Files/test.txt") as my_file:
    print(my_file.readlines())

