#!/usr/bin/env python
# coding: utf-8

# # Section 2.2
# ## List Append
# - List Creation
# - List Access
# - **List Append**
# - List Insert
# - List Delete
# 
# ----- 
# 
# ### Student will be able to
# - Create lists
# - Access items in a list
# - **Add items to the end of a list**
# - Modify and insert items into a list
# - Delete items from a list
# 

# ## Concept: Appending to Lists
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/121939c6-f81e-4787-a7a9-15ab15c69168/Unit2_Section2.2a-Appending_to_Lists.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/121939c6-f81e-4787-a7a9-15ab15c69168/Unit2_Section2.2a-Appending_to_Lists.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# **`.append()`** method adds an item to the end of a list   
# ```python
# party_list.append("Alton")
# ```

# ### Examples

# In[1]:


# [ ] review and run example
# the list before append
sample_list = [1, 1, 2]
print("sample_list before: ", sample_list)

sample_list.append(3)
# the list after append
print("sample_list after:  ", sample_list)


# In[2]:


# [ ] review and run example
# append number to sample_list
print("sample_list start:  ", sample_list)
sample_list.append(3)
print("sample_list added:  ", sample_list)

# append again
sample_list.append(8)
print("sample_list added:  ", sample_list)

# append again
sample_list.append(5)
print("sample_list added:  ", sample_list)

# [ ] run this cell several times in a row 
# [ ] run cell above, then run this cell again


# In[3]:


# [ ] review and run example
mixed_types = [1, "cat"]
# append number
mixed_types.append(3)
print("mixed_types list: ", mixed_types)

# append string
mixed_types.append("turtle")
print("mixed_types list: ", mixed_types)


# ## Task 1: `.append()`

# In[6]:


# Currency Values
# [ ] create a list of 3 or more currency denomination values, cur_values
# cur_values, contains values of coins and paper bills (.01, .05, etc.)
curVal = [.01,.05,.1,.25,1,5,10,20,50]
# [ ] print the list
print(curVal)

# [ ] append an item to the list and print the list
curVal.append(100)
print(curVal)


# In[7]:


# Currency Names
# [ ] create a list of 3 or more currency denomination NAMES, cur_names
# cur_names contains the NAMES of coins and paper bills (penny, etc.)
curNames = ["penny","nickel","dime","quarter"]
# [ ] print the list
print(curNames)

# [ ] append an item to the list and print the list
curNames.append("half dollar")
print(curNames)


# ## Task 2: Append items to a list with `input()` 

# In[9]:


# [ ] append additional values to the Currency Names list using input()
curNames.append(input())
# [ ] print the appended list
print(curNames)


# ## Task 3: `while` loop `.append()`
# - define an empty list: **`bday_survey`**
# - get user input, **`bday`**, asking for the day of the month they were born (1-31) or "q" to finish
# - using a **`while`** loop
#   - get user input, **`bday`**, asking for the day of the month they were born (1-31) or "q" to finish
#   - append the **`bday`** input to the **`bday_survey`** list
#   - repeat input until a user enters **"q"** to quit
# - print bday_survey list

# In[13]:


# [ ] complete the Birthday Survey task above
bDaySurv = []
while 1:
    day = input("What is the day of the month on which you were born? ")
    if day.isalpha():
        break
    else:
        bDaySurv.append(day)
print(bDaySurv)


# ## Task 4: Fix the error
# 

# In[28]:


# [ ] Fix the Error
import random
three_numbers = [1, 1, 2]
print("an item in the list is: ", three_numbers[random.randint(0,2)])


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
