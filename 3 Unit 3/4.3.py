#!/usr/bin/env python
# coding: utf-8

# # Section 4.3: Documenting Functions (Docstring)
# * Docstrings
# * """ """
# * \_\_doc\_\_ , help()
# 
# ### Students will be able to:
# * Write one-line docstrings
# * Write multi-line docstrings
# * Access docstrings

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# ## Documenting Code by Using Docstrings
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/10768402-b5dd-4d03-b112-12489c8fb601/DEV330x-4_3a_docstring.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/df3893d2-4d80-4b94-9f7c-fc0bc67abfd1/DEV330x-4_3a_docstring.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# Documenting code is an essential part of software development. It is the way developers record information for later reference or to communicate ideas to other developers who will be using the code. Documenting code in Python is easily done using documentation strings (_docstrings_). Docstrings are string literals that are used to document modules, classes, functions, and methods. Docstrings start and end with triple quotes `""" some string """`. In this section, the focus is on using docstrings to document functions.
# 
# In Python, documentation should communicate what your code does, not how it works. There are different documentation conventions for every development community or company. The following is adapted from Python Enhancement Proposal 257 (PEP 257), which can be found at https://www.python.org/dev/peps/pep-0257/.
# 
# ### One-line docstrings
# 
# Used for simple functions with clear functionality:
# 
# ```python
# def double(x):
#     """Return doubled x."""
#     return x * 2
# ```
# 
# General notes:
# * Use triple quotes even though it's only a single line docstring.
# * Describe the function as a command, not as a description (i.e. return x, compute b...).
# * End the string with a period.
# 
# ### Multi-line docstrings
# 
# Used to describe functions more elaborately:
# 
# ```python
# def vowel_count(word):
#     """
#     Count the number of vowels in a word.
#     
#     args:
#         word: string under test
#         
#     returns:
#         count: number of counted vowels
#     """
#     
#     count = 0
#     for c in word:
#         if c in "AEIOUYaeiouy":
#             count = count + 1
#     return count
# ```
# 
# General notes:
# * Start with triple quotes.
# * Write a summary line as in the one-line docstring (as a command, ends with a period).
# * Follow the summary with a blank line.
# * You can write more description after the blank line, but this is optional.
# * List the function arguments, return values, and exceptions raised (if any).
# * End the docstring with triple quotes and a blank line.
# 
# ### Accessing docstrings
# Each function contains an attribute `__doc__` that contains its docstring. A function's docstring can be accessed through this attribute or by using the `help()` function in a Python interpreter.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# In this example, you will explore how to write and access one-line and multi-line docstrings.

# ## Converting Celsius to Fahrenheit

# In[1]:


def C2F(degrees_celsius):
    """ Convert Celsius to Fahrenheit"""
    return degrees_celsius * (9/5) + 32

print("Accessing docstrings using __doc__:\n")
print(C2F.__doc__)


# In[2]:


def C2F(degrees_celsius):
    """ Convert Celsius to Fahrenheit"""
    return degrees_celsius * (9/5) + 32

print("Accessing docstrings using help:\n")
help(C2F)


# ## Converting Kilograms (kg) to Pounds (lb)

# In[3]:


def kg2lb(kilograms):
    """
    Convert kilograms to pounds
    
    args:
        kilograms: weight in kg 
    
    returns:
        pounds: weight in lb
    """
    
    pounds = kilograms * 2.20462262185
    return pounds

print("Accessing docstrings using __doc__:\n")
print(kg2lb.__doc__)


# In[4]:


def kg2lb(kilograms):
    """
    Convert kilograms to pounds
    
    args:
        kilograms: weight in kg 
    
    returns:
        pounds: weight in lb
    """
    
    pounds = kilograms * 2.20462262185
    return pounds

print("Accessing docstrings using help:\n")
help(kg2lb)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Documenting Code by Using Docstrings

# In[7]:


# [ ] The following function generates a single die roll
# Document the function using a one-line docstring

from random import randint

def die_roller ():
    '''Return the result of rolling a die.'''
    return (randint(1, 6))


# In[8]:


# [ ] The following function computes the area of a circle
# Document the function using a one-line docstring

from math import pi

def circle_area(r):
    '''Calculate the area of a circle with radius (r).'''
    return pi * (r ** 2)


# In[9]:


# [ ] The following program counts the number of times the value in `a` appears in `lst`
# Document the function using a multi-line docstring

def count_occurrences(a, lst):
    '''Count the number of times (a) appears in list (lst).
    
    args:
        a: number to search for
        lst: container to look in
        
    returns:
        count: number of times a appears in lst'''
    count = 0
    for element in lst:
        if a == element:
            count = count + 1
    
    return count


# In[11]:


# [ ] The following program prints out the date `d` number of days after today
# Document the function using a multi-line docstring

from datetime import date, timedelta
def future_date(d):
    '''Print the date (d) days from today's date.
    
    args:
        d: number of days in the future
        
    returns:
        None'''
    today = date.today()
    td = timedelta(days = d)
    future = today + td
    print("Date {:d} from today is: {:s}".format(d, future.strftime("%a %h %d, %Y")))
    
# Date 10 days from today
future_date(10)

