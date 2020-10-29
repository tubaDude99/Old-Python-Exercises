#!/usr/bin/env python
# coding: utf-8

# # Section 1.1
# ## String Sequences
# - **Accessing string characters with index**
# - Accessing substrings with index slicing
# - Iterating through characters of a string
# - More string methods
# 
# ----- 
# 
# ### Student will be able to
# - **Work with string characters by index**
# - Slice strings into substrings
# - Iterate through string characters
# - Use string methods

# ## Concept: Accessing a Single String Character
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/a8044252-4f2f-4960-b37b-70da8fe4769a/Unit2_Section1.1a-String_Index_Address.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/a8044252-4f2f-4960-b37b-70da8fe4769a/Unit2_Section1.1a-String_Index_Address.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Addressing a string index
# Strings are sequences of characters.  Another common sequence type used in this course is a **list**.  Sequences index items counting from 0 for the first item.
# 
# ![string with index for each letter](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/string_indexes.PNG)  
# 
# ```python
# # assign string to student_name
# student_name = "Alton"
# # first character is at index 0
# student_name[0]
# ```  
# 

# ### Examples

# In[1]:


# [ ] review and run example - note the first element is always index = 0
student_name = "Alton"
print(student_name[0], "<-- first character at index 0")
print(student_name[1])
print(student_name[2])
print(student_name[3])
print(student_name[4])


# In[2]:


# [ ] review and run example
student_name = "Jin"
if student_name[0].lower() == "a":
    print('Winner! Name starts with A:', student_name)
elif student_name[0].lower() == "j":
    print('Winner! Name starts with J:', student_name)
else:
    print('Not a match, try again tomorrow:', student_name)


# In[3]:


# [ ] review and run ERROR example
# cannot index out of range
student_name = "Tobias"
print(student_name[6])


# ## Task 1: Work with individual string characters  
# 
# |                                                                 |
# |-----------------------------------------------------------------|
# | **Remember:** The first character in a string is at **index 0**.|
# |                                                                 |
# 

# In[5]:


# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the 1st, 3rd and 5th characters
street_name = "Highview"
print(street_name[0],street_name[2],street_name[4])


# In[6]:


# [ ] Create an input variable: team_name - ask that second letter = "i", "o", or "u"
# [ ] Test if team_name 2nd character = "i", "o", or "u" and print a message
# note: use if, elif and else
teamName = input('Enter a team name that has "i","o", or "u" as its second letter. ')
if teamName[1] in "iou":
    print("yes")
else:
    print("no")


# ## Concept: Using a Negative Index 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/28da3b48-538d-4412-ae7b-ce95e9892ce9/Unit2_Section1.1b-Using_a_Negative_Index.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/28da3b48-538d-4412-ae7b-ce95e9892ce9/Unit2_Section1.1b-Using_a_Negative_Index.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Access the end of a string using -1
# Strings assign an **index** number address to each string character
# 
# - First character in a string is index 0
# - Last character in a string is index **-1**
# 
# ![negative string index counts from the end](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/string_neg_index.PNG)
# 
# To access the last character in a string:
# ```python
# student_name[-1]
# ```
# 

# ### Examples
# 
# 

# #### access the last character with the -1 index
# negative index counts back from the last character in a string  

# In[8]:


# [ ] review and run example
student_name = "Joana"

# get last letter
end_letter = student_name[-1]
print(student_name,"ends with", "'" + end_letter + "'")


# In[9]:


# [ ] review and run example
# get second to last letter
second_last_letter = student_name[-2]
print(student_name,"has 2nd to last letter of", "'" + second_last_letter + "'")


# In[10]:


# [ ] review and run example
# you can get to the same letter with index counting + or -
print("for", student_name)
print("index 3 =", "'" + student_name[3] + "'")
print("index -2 =","'" + student_name[-2] + "'")


# ## Task 2
# 

# In[16]:


# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the last 3 characters of street_name
streetName = "Versailles"
print(streetName[-1], streetName[-2], streetName[-3])


# In[17]:


# [ ] create and assign string variable: first_name
firstName = "Timothy"
# [ ] print the first and last letters of name
print(firstName[0], firstName[-1])


# ## Task 3: Fix the errors

# In[18]:


# [ ] Review, Run, Fix the error using string index
shoe = "tennis"
# print the last letter
print(shoe[-1])


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
