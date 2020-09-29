#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

# Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)     # .(single character), .* (many characters)
if x:
  print("YES! We have a match!")
else:
  print("No match")
print("\n")

# Find all digit characters:import re

# Check if the string starts with "The":
txt = "The rain in Spain"
x = re.findall("\AThe", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")
print("\n")

# Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

# Check if "ain" is present at the end of a WORD:
x = re.findall(r"ain\b", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

# Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

# Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

# Check if the string contains any digits (numbers from 0-9):
x = re.findall("\d", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

# Return a match at every no-digit character:
x = re.findall("\D", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

# Return a match at every white-space character:
x = re.findall("\s", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

# Return a match at every NON white-space character:
x = re.findall("\S", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

# Return a match at every word character (characters from a to Z, digits from 0-9, and the
# underscore _ character):
x = re.findall("\w", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

# Return a match at every NON word character (characters NOT between a and Z. Like "!", "?"
# white-space etc.):
x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

# Check if the string ends with "Spain":
x = re.findall("Spain\Z", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")
txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)
print("\n")

# Find all lower case characters alphabetically between "a" and "m":
txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)
print("\n")

# Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
txt = "hello world"
x = re.findall("he..o", txt)
print(x)
print("\n")

# Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
print("\n")

# Check if the string ends with 'world':
x = re.findall("world$", txt)
if x:
  print("Yes, the string ends with 'world'")
else:
  print("No match")
print("\n")

# Check if the string contains "ai" followed by 0 or more "x" characters:
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("aix*", txt)   # x may be 0 or more
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

# Check if the string contains "ai" followed by 1 or more "x" characters:
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("aix+", txt)   # x may be 1 or more
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

# Check if the string contains "a" followed by exactly two "l" characters:
x = re.findall("al{2}", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")

