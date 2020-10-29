#!/usr/bin/env python
# coding: utf-8

# # Lab 3b  
# ## Conditionals, Type, and Mathematics Extended   
# 
# -----
# 
# ### Student will be able to
# - Code more than two choices using **`elif`**
# - Gather numeric input using type casting
# - Perform subtraction, multiplication and division operations in code  

# ## Tasks

# ### Rainbow colors
# Ask for input of a favorite rainbow color first letter: ROYGBIV.
# 
# Using `if`, `elif`, and `else`:  
# - Print the color matching the letter  
#     - R = Red  
#     - O = Orange  
#     - Y = Yellow  
#     - G = Green
#     - B = Blue
#     - I = Indigo
#     - V = Violet
#     - Else print "no match"
# 

# In[2]:


# [ ] complete rainbow colors
color = input("ROYGBIV ")
if color == "R":
    print("Red")
elif color == "O":
    print("Orange")
elif color == "Y":
    print("Yellow")
elif color == "G":
    print("Green")
elif color == "B":
    print("Blue")
elif color == "I":
    print("Indigo")
elif color == "V":
    print("Violet")
else:
    print("no match")


# In[3]:


# [ ] make the code above into a function rainbow_color() that has a string parameter, 
# get input and call the function and return the 
def rainbow_color(color):
    if color == "R":
        print("Red")
    elif color == "O":
        print("Orange")
    elif color == "Y":
        print("Yellow")
    elif color == "G":
        print("Green")
    elif color == "B":
        print("Blue")
    elif color == "I":
        print("Indigo")
    elif color == "V":
        print("Violet")
    else:
        print("no match")
rainbow_color(input("ROYGBIV "))


# # &nbsp;  
# **Create function age_20() that adds or subtracts 20 from your age for a return value based on current age** (use `if`) 
# - Call the function with user input and then use the return value in a sentence  
# Example `age_20(25)` returns **5**: 
# > "5 years old, 20 years difference from now"

# In[5]:


# [ ] complete age_20()
def age20(age):
    if age <= 20:
        return(age + 20)
    else:
        return(age - 20)
print(str(age20(int(input()))) + " years old, 20 years difference from now")


# **Create a function rainbow_or_age that takes a string argument**
# - If argument is a digit return the value of calling age_20() with the str value cast as **`int`** 
# - If argument is an alphabetical character return the value of calling rainbow_color() with the str
# - If neither return FALSE

# In[9]:


# [ ]  create rainbow_or_age()
def rainbowOrAge(x):
    if x.isdigit():
        if int(x) <= 20:
            return(str(int(x) + 20) + " years old, 20 years difference from now")
        else:
            return(str(int(x) - 20) + " years old, 20 years difference from now")
    elif x.isalpha():
        if x == "R":
            return("Red")
        elif x == "O":
            return("Orange")
        elif x == "Y":
            return("Yellow")
        elif x == "G":
            return("Green")
        elif x == "B":
            return("Blue")
        elif x == "I":
            return("Indigo")
        elif x == "V":
            return("Violet")
        else:
            return("no match")
    else:
        return(False)
print(rainbowOrAge(input()))


# In[12]:


# [ ]  add 2 numbers from input using a cast to integer and display the answer 
print(str(int(input()) + int(input())))


# In[13]:


# [ ] Multiply 2 numbers from input using cast and save the answer as part of a string "the answer is..."
# display the string using print

print("the answer is " + str(int(input()) * int(input())))


# In[14]:


# [ ] get input of 2 numbers and display the average: (num1 + num2) divided by 2
print(str((int(input()) + int(input()))/2))


# In[18]:


# [ ] get input of 2 numbers and subtract the largest from the smallest (use an if statement to see which is larger)
# show the answer
x = [int(input()),int(input())]
if x[1] > x[0]:
    print(x[1] - x[0])
else:
    print(x[0] - x[1])


# In[ ]:


# [ ] Divide a larger number by a smaller number and print the integer part of the result
# don't divide by zero! if a zero is input make the result zero
# [ ] cast the answer to an integer to cut off the decimals and print the result
x = [int(input()),int(input())]
if x[1] > x[0]:
    print(x[1] / x[0])
else:
    print(int(x[0] / x[1])


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
