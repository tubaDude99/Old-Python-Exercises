#!/usr/bin/env python
# coding: utf-8

# #  Module 4 Required Coding Activity  
# Introduction to Python Unit 1 
# 
# The activity is based on Modules 1 - 4 and is similar to the Jupyter Notebooks for Module 4 practice, which you may have completed.  This activity is a new version of the str_analysis() function.
# 
# | Some Assignment Requirements |
# |:-------------------------------|
# |This program requires the use of:
# - **`while`** loop to get non-empty input
# - **`if, else`**
# - **`if, else`** (nested)
# - **`.isdigit()`** check for integer only input
# - **`.isalpha()`** check for alphabetic only input
# 
# The program should **only** use code syntax covered in modules 1 - 4.
# The program must result in printed message analysis of the input.  |
# 
# 
#   
# ## Program: `str_analysis()` Function  
# 
# Create the str_analysis() function that takes 1 string argument and returns a string message.  The message will be an analysis of a test string that is passed as an argument to str_analysis(). The function should respond with messages such as:  
# - "big number"
# - "small number"
# - "all alphabetic"
# - "multiple character types"
# 
# The program will call str_analysis() with a string argument from input collected within a while loop.  The while loop will test if input is empty (an empty string "") and continue to loop and gather input until the user submits at least 1 character (input cannot be empty).  
# 
# The program then calls the str_analysis() function and prints the **return** message.
# 
# 
# 
# #### Sample input and output:  
# Enter nothing (twice) then enter a word  
# ```
# enter word or integer: 
# enter word or integer: 
# enter word or integer: Hello
# "Hello" is all alphabetical characters!
#   
# ```  
# -----    
#   
# Alphabetical word input 
# ```
# enter word or integer: carbonization
# "carbonization" is all alphabetical characters!
#   
# ```  
# -----     
#    
# Numeric inputs
# ```
# enter word or integer: 30
# 30 is a smaller number than expected
# 
# enter word or integer: 1024
# 1024 is a pretty big number
# ```  
# -----  
# 
# 
# ### Loop until non-empty input is submitted  
# This diagram represents the input part of the assignment - it is the loop to keep prompting the user for input until they submit some input (non-empty).  
# 
# ![image of while Loop with nested if statements described in bulleted text above](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/input_loop_sketch.png)  
# 
# Once the user gives input with characters use the input in calling the str_analysis() function.
# 
# ### Additional Details
# In the body of the str_analysis() function:
# - Check `if` string is digits  
#   - if digits: convert to `int` and check `if` greater than 99  
#     - if greater than 99 print a message about a "big number"  
#     - if not greater than 99 print message about "small number"  
#   - check if string isalpha then (since not digits)
#     - if isalpha print message about being all alpha
#   - if not isalpha print a message about being neither all alpha nor all digit  
#     
# call the function with a string from user input 
# - Run and test your code before submitting

# In[3]:


# [ ] create, call and test the str_analysis() function  
def strAnalysis(inp):
    if inp.isalpha:
        print("That is all words congrats")
    elif inp.isdigit:
        if -100 < int(inp) < 100:
            print("Why number so small")
        else:
            print("Why number so big")
    else:
        print("What is this? You call this a string?")
strAnalysis(input("Input a string: "))


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
