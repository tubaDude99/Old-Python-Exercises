#!/usr/bin/env python
# coding: utf-8

# #  Module 2 Project  
# Course 40460: Introduction to Python, Unit 1  
# 
# The activity is based on Modules 1 and 2 and is similar to the Jupyter Notebook for Module 2 practice, which you may have completed.
# 
# | Some Assignment Requirements |  
# |:-------------------------------|  
# | **NOTE:** This program requires that a **function** be defined, created and called. The call will send values based on user input.  The function call must capture a `return` value that is used in print output.  The function will have parameters and `return` a string and should otherwise use code syntax covered in Module 2.  |  
#  
# ## Program: fishstore()
# Create and test fishstore().
# - **fishstore() takes 2 string arguments: fish & price**
# - **fishstore returns a string in sentence form**  
# - **Gather input for fish_entry and price_entry to use in calling fishstore()**
# - **Print the return value of fishstore()**
# >Example of output: **`Fish Type: Guppy costs $1`**

# In[2]:


# [ ] create, call and test fishstore() function 
def fishStore(fish,price):
    return("The fish " + fish + " costs $" + price)

print(fishStore(input("What fish? "),input("How much? ")))


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
