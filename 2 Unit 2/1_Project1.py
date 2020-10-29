#!/usr/bin/env python
# coding: utf-8

# 
# #  Module 1 Project  
# 
# Course 40461: Introduction to Python, Unit 2
# 
# This is an activity based on the Module 1 Lab, which you may have already completed.
# 
# | Important Assignment Requirements |  
# |:-------------------------------|  
# |  **NOTE:** This program **requires** **`print`** output and using code syntax used in Module 1 such as keywords **`for`**/**`in`** (iteration), **`input`**, **`if`**, **`else`**, **`.isalpha()`** method, **`.lower()`** or **`.upper()`** method. |  
# 
# 
# ## Program: Words after "G"/"g"
# Create a program that inputs a phrase (like a famous quotation) and prints all of the words that start with h-z.
# 
# Sample input:  
# `Enter a 1 sentence quote, non-alpha separate words:` **`Wheresoever you go, go with all your heart`**  
# 
# Sample output:
# ```
# WHERESOEVER
# YOU
# WITH
# YOUR
# HEART
# ```  
# ![words_after_g flowchart](https://ofl1zq-ch3302.files.1drv.com/y4msZuRt9FLMg2HrIVri9ozb5zM0Z9cwrgFg0OanRG3wThbKGRTjxf6vEmvDgiQzAthvLq4KDpiOfd5S74i-vsCDYha-Ea5B1d4MJD5tx6obEpFj3Slks3bCFbjltvV_BYQ8mlbmyoAhujPM6nHRbOxNeO2Lb6dvmW0EbS-D3QXR7lRb-whNWwquwwzO4znPMmQ4Jkf4ujqTlSpjGuaKzwTSQ?width=608&height=371&cropmode=none) 
# 
# - Split the words by building a placeholder variable: **`word`**  
#   - Loop each character in the input string  
#   - Check if character is a letter  
#   - Add a letter to **`word`** each loop until a non-alpha char is encountered  
# 
# - **if** character is alpha 
#   - Add character to **`word`**    
#   - Non-alpha detected (space, punctuation, digit,...) defines the end of a word and goes to **`else`**    
# - **`else`**  
#   - Check **`if`** word is greater than "g" alphabetically
#       - Print word 
#       - Set word = empty string
#   - or **else** 
#     - Set word = empty string and build the next word  
# 
# Hint: use `.lower()`.
# 
# Consider how you will print the last word if it ends with a non-alpha character such as a space or punctuation.
# 
# 

# In[1]:


# [] create words after "G" following the Assignment requirements use of functions, menhods and kwyowrds
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
quote = input("Quote: ")
word = ""
for l in quote:
    if l.isalpha():
        word += l
    else:
        if word.lower() > "g":
            print(word)
        word = ""
print(word)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
