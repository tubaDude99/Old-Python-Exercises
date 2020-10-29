#!/usr/bin/env python
# coding: utf-8

# #  Module 2 Project  
# 
# Course 40461: Introduction to Python, Unit 2
# 
# This is an activity based on the Module 2 Lab, which you may have already completed.
# 
# | Important Assignment Requirements |  
# |:-------------------------------|  
# | **NOTE:** This program requires creating a function using **`def`** and **`return`**, using **`print`** output, **`input`**, **`if`**, **`in`** keywords, **`.append()`**, **`.pop()`**, **`.remove()`** list methods.  As well as other standard Python. |   
# 
# ## Program: list-o-matic  
# This program takes string input and checks if that string is in a list of strings.    
# - If the string is in the list it removes the first instance from list  
# - If the string is not in the list the input gets appended to the list  
# - If the string is empty then the last item is popped from the list 
# - If the **list becomes empty** the program ends  
# - If the user enters "quit" then the program ends  
# 
# The program has two parts:  
# - **program flow** which can be modified to ask for a specific type of item.  This is the programmers choice.  Add a list of fish, trees, books, movies, songs.... your choice.  
# - **list-o-matic** Function which takes arguments of a string and a list.  The function modifies the list and returns a message as seen below.  
# 
# ![TODO: upload image to blob](https://q4tiyg-ch3302.files.1drv.com/y4mkvwrxHSIqinTvp_nNGFiMn_yyJ0dsEtCzPpG_hsFMRdyEED4ExPdsWmbdPIKRpgU25VxFIUAGBdz0yzqumtxw7wy_pAJMJ3MeZ6PJQKyej6UwN6N6zOmnRq6106aqvXJB43RKRJgB2oMmidb9Zl0OBjmvFVowm-XtD2wUW5bJrgd4LS8I5Nso_vXqfpNCANRYcKe4WnjIWds4KoV4sjPIg?width=717&height=603&cropmode=none)
# 
# **[ ]** initialize a list with several strings at the beginning of the program flow and follow the flow chart and output examples
# 
#  *example input/output*  
#  ```
# look at all the animals ['cat', 'goat', 'cat']
# enter the name of an animal: horse
# 1 instance of horse appended to list
# 
# look at all the animals ['cat', 'goat', 'cat', 'horse']
# enter the name of an animal: cat
# 1 instance of cat removed from list
# 
# look at all the animals ['goat', 'cat', 'horse']
# enter the name of an animal: cat
# 1 instance of cat removed from list
# 
# look at all the animals ['goat', 'horse']
# enter the name of an animal:          (<-- entered empty string)
# horse popped from list
# 
# look at all the animals ['goat']
# enter the name of an animal:          (<-- entered empty string)
# goat popped from list
# 
# Goodbye!
# ```  
# 
# *example 2*
# ```
# look at all the animals ['cat', 'goat', 'cat']
# enter the name of an animal: Quit
# Goodbye!
# ```  
# 
# 

# In[2]:


# [] create list-o-matic
mList = ['red', 'green', 'yellow', 'orange', 'blue', 'purple']
def listMatic(item):
    if not(item):
        mList.pop()
    elif item in mList:
        mList.remove(item)
    else:
        mList.append(item)

while mList:
    print(mList)
    item = input('What is a color? ').lower()
    if item == "quit":
        break
    else:
        listMatic(item)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
