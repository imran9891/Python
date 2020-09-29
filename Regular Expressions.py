#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Used in validation or checking

import re
string = "search this inside of this text please"
# print("search" in string)

pattern = re.compile('this')
a = pattern.search(string)     # return Match object with span
print(a.span())                # returns tuple of starting & end index
print(a.start())               # returns the starting index
print(a.end())                 # returns the end index
print(a.string)                # returns the original string 
print(a.group())               # returns the part of the string where there was a match

# b = pattern.findall(string)    # returns all instances of pattern in the string
# print(b)

# string = "search this inside of this text please"
# pattern = re.compile('search this inside of this text please')
# c = pattern.fullmatch(string)  # for fullmatch whole string should be passed in parameter
# print(c)

# string = "search this inside of this text please! Imran"
# pattern = re.compile('search this inside of this text please!')
# d = pattern.match(string)
# print(d)

