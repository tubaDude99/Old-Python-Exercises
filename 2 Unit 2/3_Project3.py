#!/usr/bin/env python
# coding: utf-8

# 
# #  Module 3 Project 
# 
# Course 40461: Introduction to Python, Unit 2
# 
# This is an activity based on the Module 3 Lab, which you may have already completed.
# 
# |  Assignment Requirements |  
# |:-------------------------------|  
# | **NOTE:** This program requires **`print`** output and using code syntax used in Module 3: **`if`**, **`input`**, **`def`**, **`return`**, **`for`**/**`in`** keywords, **`.lower()`** and **`.upper()`** method, **`.append`**, **`.pop`**, **`.split`** methods, **`range`** and **`len`** functions  |  
# 
# ## Program: Poem mixer  
# This program takes string input and then prints out a mixed order version of the string.    
# 
# 
# **Program Parts**  
# - **program flow** gathers the word list, modifies the case and order, and prints.      
#   - Get string input, input like a poem, verse or saying 
#   - Split the string into a list of individual words  
#   - Determine the length of the list
#   - Loop the length of the list by index number and for each list index:  
#     - If a word is short (3 letters or less) make the word in the list lowercase 
#     - If a word is long (7 letters or more) make the word in the list uppercase   
#   - **Call the word_mixer** function with the modified list  
#   - Print the return value from the word_mixer function  
# 
# - **word_mixer** Function has one argument: an original list of string words, containing greater than five words, and the function returns a new list.
#   - Sort the original list  
#   - Create a new list  
#   - Loop while the list is longer than 5 words:  
#     - *In each loop pop a word from the sorted original list and append to the new list*  
#     - Pop the word 5th from the end of the list and append to the new list  
#     - Pop the first word in the list and append to the new list  
#     - Pop the last word in the list and append to the new list  
#   - **Return** the new list on exiting the loop
# 
# 
# 
# ![TODO: upload image to blob](https://qitcyg-ch3302.files.1drv.com/y4mtK8FJlu7bvNCw_NFrJNnMEX05-bGQKZ-ljIB7ofo8jg14zZKLdYrjXQfPcL1PnNKqaBc_v85pd-47J8BBRN3Eg5LXSmxbhZG99zHmQwVTSQBd6n3S1IXgcG0lqjA8PGW1NVMQyPtX-_m_sGry5j1iCJzjiZmUrFmGckPrEYxvjPIHHelgxQ4oVYG32S32otj0cdV8f9aDv3cnvb9AvDKqg?width=727&height=586&cropmode=none)
# 
# 
#  **input example**  *(beginning of William Blake poem, "The Fly")*
# 
#  >enter a saying or poem: `Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?`  
# 
# 
# **output example**   
# >`or BRUSHED thy not Little thou me? SUMMER’S thee? like THOUGHTLESS play i a not hand a my fly am man`
# 
# 
# **alternative output** in each loop in the function that creates the new list add a "\\n" to the list   
# ```
#  or BRUSHED thy 
#  not Little thou 
#  me? SUMMER’S thee? 
#  like THOUGHTLESS play 
#  i a not 
#  hand a my 
#  fly am man
# ```
# 
# 

# In[13]:


# [] create poem mixer
def wMix(orig):
    orig.sort()
    new = []
    while len(orig) > 5:
        new.append(orig.pop(-5))
        new.append(orig.pop(0))
        new.append(orig.pop())
        new.append("\n")
    return(new)
words = input("Poem, verse or saying: ").split()
for x in range(len(words)):
    if len(words[x]) <= 3:
        words[x] = words[x].lower()
    if len(words[x]) >= 7:
        words[x] = words[x].upper()
print()
for x in wMix(words):
    if x == "\n":
        print(x, end = '')
    else:
        print(x, end = " ")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
