#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Email Validation
import re
string = "imranekbal9891@gmail.com"
x = re.findall(r"(^[\w\W]+@[a-z]+\.[\w]+$)", string)
print(x)

# Password Checker
# Atleast 8 characters long
# Contains any sort of letters, numbers, $%#@
# end with digit
guess = 'Madalisha@007'
a = re.fullmatch(r"(^[a-zA-Z0-9@#$%]{7,}\d$)",guess)
print(a)

