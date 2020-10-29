#!/usr/bin/env python
# coding: utf-8

# # Section 2.3
# ## Functions, Arguments, and Parameters
# - Creating a simple function with parameters
# - Exploring functions with `return` values 
# - Creating functions with multiple parameters
# - **Sequence in python**  
# 
# -----
# 
# ### Student will be able to
# - Create functions with a parameter  
# - Create functions with a `return` value 
# - Create functions with multiple parameters
# - **Use knowledge of sequence in coding tasks**  
# - **Use coding best practices** 

# ## Concept: Sequence
# In programming, **sequence** refers to the order that code is processed.  Objects in Python, such as variables and functions, are not available until they have been processed. 
# 
# Processing sequence flows from the top of a page of code to the bottom. This often means that **Function definitions are placed at the beginning of a page of code.**
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/29ebdee3-33e8-487f-9c73-621219e5e6d2/Unit1_Section3.3-Object_Sequence.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/29ebdee3-33e8-487f-9c73-621219e5e6d2/Unit1_Section3.3-Object_Sequence.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# In the sample below, the function **`hat_color`** cannot be accessed since it is initialized after it is called at the bottom of the code.  
# ```python
# have_hat = hat_available('green')  
#   
# print('hat available is', have_hat)
# 
# def hat_available(color):
#     hat_colors = 'black, red, blue, green, white, grey, brown, pink'
#     return(color.lower() in hat_colors)
# ```  
# This results in an error - the code flows from top to bottom is in the incorrect **sequence**. 
# ```python
# NameError: name 'hat_available' is not defined
# ```
# In the statement &nbsp; **`have_hat = hat_available('green')`** &nbsp; the function &nbsp; **`hat_available()`** &nbsp; needs to be called after the function has been defined.
# > **Note:** an argument or variable is said to be **hard coded** when assigned a literal or constant value.  
#     It is a good habit to avoid creating hard coded values in functions, such as  
#     `hat_colors = 'black, red, blue, green, white, grey, brown, pink'`.

# ### Examples

# In[1]:


# review and run code - note: fix error in the following "tasks" section
have_hat = hat_available('green')  
  
print('hat available is', have_hat)

def hat_available(color):
    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
    # return Boolean
    return(color.lower() in hat_colors)


# ## Task 1: Change the Sequence to fix the `NameError`
# - [ ] Fix the code **sequence** so the &nbsp;**`hat_available()`** &nbsp;function is availabe when called and the code runs without error

# In[2]:


# [ ] fix the sequence of the code to remove the NameError

def hat_available(color):
    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
    return(color.lower() in hat_colors)

have_hat = hat_available('green')  
  
print('hat available is', have_hat)


# ## Concept: Avoid Hard-Coding
# ### "Hard-coding" is placing data values directly into code
# An example of hard-coding from above is **`have_hat = hat_available('green')`**  where the argument `'green'` is hard-coded.
# 
# A programming best practice is to **avoid hard-coding values when possible**.
# - Use variables and verse hard-coded 
# - Often preferable to use input such as a configuration file (advanced topic) or user input.
# These practices allow changing the data without disturbing the main code and makes code more reusable.
# 

# ## Task 2 (program): bird_available
# The program should ask for user to "input a bird name to check for availability" and print a statement informing of availability.
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/767e4db3-7909-4829-99db-fd6750ea5d54/Unit1_Section3.3-Bird_Available.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/767e4db3-7909-4829-99db-fd6750ea5d54/Unit1_Section3.3-Bird_Available.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Create this program with a Boolean function `bird_available()`
# - Has parameter that takes the name of a type of bird
# - For this exercise the variable `bird_types = 'crow robin parrot eagle sandpiper hawk piegon'`
# - Return `True` or `False` (we are making a Boolean Function)
# - Call the function using the name of a bird type from user input
# - Print a sentence that indicates the availablity of the type of bird checked
# 

# In[4]:


# [ ] create function bird_available
bird_types = 'crow robin parrot eagle sandpiper hawk piegon'
def bird_available(bird):
    return(bird in bird_types)
# [ ] user input

# [ ] call bird_available
available = bird_available(input("What bird do you want? "))
# [ ] print availbility status
if available:
    print("We have that bird.")
else:
    print("We do not have that bird.")


# ## Task 3: Fix the error
# 

# In[6]:


# define function how_many
def how_many():
    requested = input("enter how many you want: ")
    return requested

# get the number_needed
number_needed = how_many()
print(number_needed, "will be ordered")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
