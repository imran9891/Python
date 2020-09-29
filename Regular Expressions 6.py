#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Split
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# Split the string only at the first occurrence
x = re.split("\s", txt, 1)
print(x)

# Sub: The sub() function replaces the matches with the text of your choice
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# Replace the first 2 occurrences
x = re.sub("\s", "9", txt, 2)
print(x)

