#!/usr/bin/env python
# coding: utf-8

# # Lab 4a
# ## Nested Conditionals
# 
# -----
# 
# ### Student will be able to
# - Create nested conditional logic in code  
# - Print format print using escape sequence (**\**)

# ## Tasks

# In[1]:


# [ ] print a string that outputs the following exactly: The new line character is "\n"
print("The new line character is \"\\n\"")


# In[2]:


# [ ] print output that is exactly (with quotes): "That's how we escape!"
print("\"That's how we escape!\"")


# In[4]:


# [ ] with only 1 print statement and using No Space Characters, output the text commented below  

# 1       one
# 22      two
# 333     three

print("1\tone\n22\ttwo\n333\tthree")


# ## Program: quote_me() Function
# quote_me takes a string argument and returns a string that will display surrounded with **added double quotes** if printed  
# - Check if the passed string starts with a double quotation mark (`"\""`).
# - If it does, then surround the string with single quotation marks 
# - If the passed string starts with a single quotation mark, or it if doesn't start with a quotation mark, then surround it with double quotation marks.
# 
# Test the function code passing string input as the argument to quote_me(). 

# In[7]:


# [ ] create and test quote_me()

def quote(s):
    if s.startswith("\""):
        return("'" + s + "'")
    else:
        return('"' + s + '"')
print(quote(input()))


# ## Program: shirt order 
# First get input for color and size: 
# - White has sizes L, M 
# - Blue has sizes M, S  
# 
# Print available or unavailable, then print the order confirmation of color and size.  
# 
# **Hint**: set a variable "available = False" before nested if statements 
# and change to True if color and size are available.

# In[10]:


# [ ] create shirt order using nested if
c = input("What color? (White or Blue) ").lower()
if c == "white":
    s = input("What size? (L, M) ")
    print("You have placed an order for a %s shirt of size %s." %(c,s))
if c == "blue":
    s = input("What size? (M, S) ")
    print("You have placed an order for a %s shirt of size %s." %(c,s))
    


# ## Program: str_analysis() Function
# Create the str_analysis() function that takes a string argument.  In the body of the function:
# - Check `if` string is digits  
#   - If digits: convert to `int` and check `if` greater than 99  
#     - If greater than 99 print a message about a "big number"  
#     - If not greater than 99 print message about small number  
#   - If not digits: check if string isalpha
#     - If isalpha print message about being all alpha
#     - If not isalpha print a message about being neither all alpha nor all digit  
#     
# Call the function with a string from user input. 

# In[14]:


# [ ] create and test str_analysis()
def strAn(s):
    if s.isdigit():
        s = int(s)
        if s > 99:
            print("bIg number")
    elif s.isalpha():
        print("those are All letters")
    else:
        print("that's not numbers Or letters!!!!!!")
strAn(input())


# ## Program: ticket_check() - finds out if a seat is available  
# Call ticket_check() function with 2 arguments: *section* and *seats* requested and return True or False  
# - **section** is a string and expects: general, floor
# - **seats** is an integer and expects: 1 - 10  
# 
# Check for valid section and seats:
# - If section is *general* (or use startswith "g")  
#   - If seats is 1-10 return True 
# - If section is *floor* (or use starts with "f")
#   - If seats is 1-4 return True  
# 
# Otherwise return False.

# In[18]:


# [ ] create and call ticket_check()
def tktChk(sect,sts):
    if sect.lower() == "general":
        if 1 <= sts <= 10:
            return(True)
        else:
            return(False)
    elif sect.lower() == "floor":
        if 1 <= sts <= 4:
            return(True)
        else:
            return(False)
    else:
        return(False)
print(tktChk(input("What section? "), int(input("How many seats? "))))


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
