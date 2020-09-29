#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Linting: Errors pop up before running code
# IDE ~ Pycharm PEP-8: Flashes errors before we run our code
# Read errors
# pdb module

import pdb

def tot(n1, n2):
    pdb.set_trace()
    t = 4*5
    return n1 + n2

tot(4,5)

# commands in pdb:
# a: returns all arguments
# w: previous line, current line and next line content
# step: step to the next line
# continue: to continue till the end & return something
# help: write help with keywords gives documentation
# clear: brings to the top
# exit: come out of pdb
# next: Continue execution until the next line in the current function is reached or it returns.    
# We can change the variables value in the console window as well.
# we can type in the variable name to get its value

