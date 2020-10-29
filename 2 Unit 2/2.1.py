#!/usr/bin/env python
# coding: utf-8

# # Section 2.1
# ## List Sequences
# - **List Creation**
# - **List Access**
# - List Append
# - List Insert
# - List Delete
# 
# ----- 
# 
# ### Student will be able to
# - **Create lists**
# - **Access items in a list**
# - Add items to the end of a list
# - Modify and insert items into a list
# - Delete items from a list

# ## Concept: Creating Lists
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/933c4e57-93ae-4660-8725-6eff3987dd1c/Unit2_Section2.1a-Creating_Lists.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/933c4e57-93ae-4660-8725-6eff3987dd1c/Unit2_Section2.1a-Creating_Lists.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# A simple lists contains **comma separated** objects enclosed in **square brackets**.
# ```python
# empty_list = [ ]
# sample_list = [1, 1, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5]
# ```
# 
# List object types are not restricted so a mix of object types can be in single list
# ```python
# mixed_list = [1, 1, "one", "two", 2.0, sample_list, "Hello World"]
# ```

# ### Examples

# In[1]:


# [ ] review and run example
# define list of strings
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]

# display type information
print("ft_bones: ", type(ft_bones))

# print the list
print(ft_bones)


# In[2]:


# [ ] review and run example
# define list of integers
age_survey = [12, 14, 12, 29, 12, 14, 12, 12, 13, 12, 14, 13, 13, 46, 13, 12, 12, 13, 13, 12, 12]

# display type information
print("age_survey: ", type(age_survey))

# print the list
print(age_survey)


# In[3]:


# [ ] review and run example
# define list of mixed data type
mixed_list = [1, 34, 0.999, "dog", "cat", ft_bones, age_survey]

# display type information
print("mixed_list: ", type(mixed_list))

# print the list
print(mixed_list)


# ## Task 1: Create Lists

# In[4]:


# [ ] create team_names list and populate with 3-5 team name strings
team_names = ["Timothy","Jacob","Nathan","Priya"]
# [ ] print the list
print(team_names)


# In[5]:


# [ ] Create a list mix_list with numbers and strings with 4-6 items
mixList = [3.141,"Timothy",True,"Williams"]
# [ ] print the list
print(mixList)


# ## Concept: List Access 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/efc23682-3b15-4c73-afe0-77067fac2769/Unit2_Section2.1b-Accessing_Lists.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/efc23682-3b15-4c73-afe0-77067fac2769/Unit2_Section2.1b-Accessing_Lists.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Counting like a computer
# #### To access a list we need to count like a computer, and that means starting with zero (0)
# Lists give an **index** number to each list item.
# 
# - first element in a list is index 0
# - second element in a list is index 1
# 
# To access the first item in a list use the list name, followed by square brackets containing the index number.
# ```python
# age_survey[0]
# ```
# 

# ### Examples
# 
# |run previous examples before running the examples below|
# |-----------------------------------------------------------|
# 

# In[6]:


# [ ] review and run example
print(ft_bones[0], "is the 1st bone on the list")
print(ft_bones[2], "is the 3rd bone on the list")
print(ft_bones[-1], "is the last bone on the list")


# In[7]:


# [ ] review and run example
print(ft_bones[1], "is connected to the",ft_bones[3])


# In[8]:


# [ ] review and run example
three_ages_sum = age_survey[0] + age_survey[1] + age_survey[2]
print("The first three ages total", three_ages_sum)


# ## Task 2

# In[9]:


# [ ] Create a list, streets, that lists the name of 5 street name strings
streets = ["Severn", "Old Jenks", "Highview","Pinedale","Versaille"]
# [ ] print a message that there is "No Parking" on index 0 or index 4 streets
print("There is no parking on " + streets[0] + " or " + streets[4])


# In[11]:


# [ ] Create a list, num_2_add, made of 5 different numbers between 0 - 25
n2add = [1,3,6,9,24,16]
# [ ] print the sum of the numbers
print(n2add[0]+n2add[1]+n2add[2]+n2add[3]+n2add[4])


# ## Task 3: Fix the errors

# In[12]:


# [ ] Review & Run, but ***Do Not Edit*** this code cell
# [ ] Fix the error by only editing and running the block below

print(" Total of checks 3 & 4 = $", pay_checks[2] + pay_checks[3])


# In[14]:


# [ ] Fix the error above by creating and running code in this cell
pay_checks = [0,0,0,0]
print(" Total of checks 3 & 4 = $", pay_checks[2] + pay_checks[3])


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
