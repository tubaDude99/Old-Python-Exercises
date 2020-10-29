#!/usr/bin/env python
# coding: utf-8

# # Section 1.2
# ## Index Slicing
# - Accessing string characters with index
# - **Accessing substrings with index slicing**
# - Iterating through characters of a string
# - More string methods
# 
# ----- 
# 
# ### Student will be able to
# - Work with string characters
# - **Slice strings into substrings**
# - Iterate through string characters
# - Use string methods

# ## Concept: Accessing Substrings 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/251ad8c1-588b-47de-8638-a5bcd0f29800/Unit2_Section1.2a-Index_Slicing-Substrings.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/251ad8c1-588b-47de-8638-a5bcd0f29800/Unit2_Section1.2a-Index_Slicing-Substrings.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Index Slicing [start:stop]
# String slicing returns a string section by addressing the start and stop indexes
# 
# ```python
# # assign string to student_name
# student_name = "Colette"
# # addressing the 3rd, 4th and 5th characters
# student_name[2:5]
# ```
# The slice starts at index 2 and ends at index 5 (but does not include index 5)

# ### Examples

# In[1]:


# [ ] review and run example
# assign string to student_name
student_name = "Colette"

# addressing the 3rd, 4th and 5th characters using a slice
print("slice student_name[2:5]:",student_name[2:5])


# In[2]:


# [ ] review and run example
# assign string to student_name
student_name = "Colette"

# addressing the 3rd, 4th and 5th characters individually
print("index 2, 3 & 4 of student_name:", student_name[2] + student_name[3] + student_name[4])


# In[3]:


# [ ] review and run example
long_word = 'Acknowledgement'
print(long_word[2:11])
print(long_word[2:11], "is the 3rd char through the 11th char")
print(long_word[2:11], "is the index 2, \"" + long_word[2] + "\",", "through index 10, \"" + long_word[10] + "\"")


# ## Task 1: Slice a string
# ### Start & stop index

# In[6]:


# [ ] slice long_word to print "act" and to print "tic"
long_word = "characteristics"
print(long_word[4:7])
print(long_word[-4:-1])


# In[7]:


# [ ] slice long_word to print "sequence"
long_word = "Consequences"
print(long_word[3:-1])


# ## Concept: Accessing Substring Beginnings 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/368b352f-6061-488c-80a4-d75e455f4416/Unit2_Section1.2b-Index_Slicing_Beginnings.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/368b352f-6061-488c-80a4-d75e455f4416/Unit2_Section1.2b-Index_Slicing_Beginnings.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Index Slicing [:stop]
# String slicing returns a string section from index 0 by addressing only the stop index
# 
# ```python
# student_name = "Colette"
# # addressing the 1st, 2nd & 3rd characters
# student_name[:3]
# ```
# **default start for a slice is index 0**

# ### Example

# In[8]:


# [ ] review and run example
student_name = "Colette"
# addressing the 1st, 2nd & 3rd characters
print(student_name[:3])


# ## Task 2

# In[13]:


# [ ] print the first half of the long_word
long_word = "Consequences"
print(long_word[:6])
# [ ] print a message that there is "No Parking" on index 0 or index 4 streets
print("There is no parking on %s or %s streets." %(long_word[0],long_word[4]))


# ## Concept: Accessing Substring Endings 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/29beb75a-aee7-43df-9569-e9ad22cffac4/Unit2_Section1.2c-Index_Slicing_Endings.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/29beb75a-aee7-43df-9569-e9ad22cffac4/Unit2_Section1.2c-Index_Slicing_Endings.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Index Slicing [start:]
# String slicing returns a string section including by addressing only the start index
# 
# ```python
# student_name = "Colette"
# # addressing the 4th, 5th and 6th characters
# student_name[3:]
# ```
# **default end index returns up to and including the last string character**

# ### Example

# In[11]:


# [ ] review and run example
student_name = "Colette"
#  4th, 5th, 6th and 7th characters
student_name[3:]


# ## Task 3

# In[14]:


# [ ] print the second half of the long_word
long_word = "Consequences"
print(long_word[6:])
# [ ] print a message that there is "No Parking" on index 0 or index 4 streets
print("There is no parking on %s or %s streets." %(long_word[0],long_word[4]))


# ## Concept: Accessing Substrings by Step Size
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/62c65917-4979-4d26-9a05-09e1ed02cc51/Unit2_Section1.2d-Index_Slicing-Step_Sizes.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/62c65917-4979-4d26-9a05-09e1ed02cc51/Unit2_Section1.2d-Index_Slicing-Step_Sizes.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Index Slicing [:], [::2]
# - **[:]** returns the entire string
# - **[::2]** returns the first char and then steps to every other char in the string
# - **[1::3]** returns the second char and then steps to every third char in the string  
# 
# the number **2**, in the print statement below, represents the **step** 
# 
# ```python
# print(long_word[::2])
# ```

# ### Examples

# In[16]:


# [ ] review and run example
student_name = "Colette"
# return all
print(student_name[:])


# In[17]:


# [ ] review and run example
student_name = "Colette"
# return every other
print(student_name[::2])


# In[18]:


# [ ] review and run example
student_name = "Colette"
# return every third, starting at 2nd character
print(student_name[1::2])


# In[19]:


# [ ] review and run example
long_word = "Consequences"
# starting at 2nd char (index 1) to 9th character, return every other character
print(long_word[1:9:2])


# ## Task 4

# In[21]:


# [ ] print the 1st and every 3rd letter of long_word
long_word = "Acknowledgement"
print(long_word[0::3])


# In[23]:


# [ ] print every other character of long_word starting at the 3rd character
long_word = "Acknowledgement"
print(long_word[2::2])


# ## Concept: Accessing Substrings Continued  
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/2e59f526-fadb-434e-822e-afe3732f75df/Unit2_Section1.2e-Index_Slicing-Reverse.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/2e59f526-fadb-434e-822e-afe3732f75df/Unit2_Section1.2e-Index_Slicing-Reverse.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Stepping backwards 
# 
# ```python
# print(long_word[::-1])
# ```  
# 
# Use **[::-1]** to reverse a string.

# ### Example

# In[24]:


# [ ] review and run example of stepping backwards using [::-1]
long_word = "characteristics"
# make the step increment -1 to step backwards
print(long_word[::-1])


# In[25]:


# [ ] review and run example of stepping backwards using [6::-1]
long_word = "characteristics"
# start at the 7th letter backwards to start
print(long_word[6::-1])


# ## Task 5: Use slicing

# In[26]:


# [ ] reverse long_word
long_word = "stressed"
print(long_word[::-1])


# In[28]:


# [ ] print the first 5 letters of long_word in reverse
long_word = "characteristics"
print(long_word[5::-1])


# ## Task 6: Use slicing

# In[36]:


# [ ] print the first 4 letters of long_word
# [ ] print the first 4 letters of long_word in reverse
# [ ] print the last 4 letters of long_word in reverse
# [ ] print the letters spanning indexes 3 to 6 of long_word in Reverse
long_word = "timeline"
print(long_word[:4])
print(long_word[3::-1])
print(long_word[:-5:-1])
print(long_word[6:2:-1])


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
