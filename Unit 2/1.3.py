#!/usr/bin/env python
# coding: utf-8

# # Section 1.3
# ## Iterating Strings
# - Accessing string characters with index
# - Accessing substrings with index slicing
# - **Iterating through characters of a string**
# - More string methods
# 
# ----- 
# 
# ### Student will be able to
# - Work with string characters
# - Slice strings into substrings
# - **Iterate through string characters**
# - Use string methods

# ## Concept: Iterate a String by Character
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/edd3631b-bceb-45a1-82bb-addf532aba4d/Unit2_Section1.3a-Iterate_a_String.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/edd3631b-bceb-45a1-82bb-addf532aba4d/Unit2_Section1.3a-Iterate_a_String.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### `for letter in word:`
# Python provides powerful sequence iteration features.  Below, **`for letter in word:`** loops through each letter in *word*.
# 
# ```python
# word = "cello"
# 
# for letter in word:
#     print(letter)
# ```  
# 
# The variable **`letter`** is an arbitrary variable name .  Any valid variable name can be used.
# 

# ### Examples

# In[1]:


# [ ] review and run example
word = "cello"

for letter in word:
    print(letter)


# In[2]:


# [ ] review and run example
# note: the variable 'letter' changed to 'item'
word = "trumpet"

for item in word:
    print(item)


# In[3]:


# [ ] review and run example
# note: variable is now 'xyz' 
# using 'xyz', 'item' or 'letter' are all the same result
word = "piano"

for xyz in word:
    print(xyz)


# In[4]:


# [ ] review and run example
# creates a new string (new_name) adding a letter (ltr) each loop
# Q?: how many times will the loop run?
student_name = "Skye"
new_name = ""

for ltr in student_name:
    if ltr.lower() == "y":
        new_name += ltr.upper()
    else:
        new_name += ltr
print(student_name,"to",new_name)


# ## Task 1: Iterate a String
# ### One character at a time

# In[5]:


# [ ] Get user input for first_name
# [ ] iterate through letters in first_name 
#    - print each letter on a new line
fName = input()
for l in fName:
    print(l)


# ## Task 2 (Program): capitalize-io
# - Get user input for first_name
# - Create an empty string variable: new_name
# - Iterate through letters in first_name 
#   - Add each letter in new_name
#   - Capitalize if letter is an "i" or "o" *(hint: if, elif, else)
# - Print new_name

# In[7]:


# [ ] Create capitalize-io
fName = input()
nName = ""
for l in fName:
    if l in "io":
        l = l.upper()
    nName = nName + l
print(nName)


# ## Concept: Iterate Substrings 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/257ed101-c530-406a-ba20-6d437d88e529/Unit2_Section1.3b-Iterate-Substrings.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/257ed101-c530-406a-ba20-6d437d88e529/Unit2_Section1.3b-Iterate-Substrings.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# Combine string slicing and iteration:
# 
# ```python
# student_name = "Skye"
# 
# for letter in student_name[:3]:
#     print(letter)
# ```  
# 
# Iterate backwards using: **`student_name[::-1]`**.

# ### Example

# In[8]:


# [ ] review and run example
student_name = "Skye"

for letter in student_name[:3]:
    print(letter)


# In[9]:


# Iterate BACKWARDS
# [ ] review and run example
student_name = "Skye"

# start at "y" (student_name[2]), iterate backwards
for letter in student_name[2::-1]:
    print(letter)


# ## Task 3: String slicing and iteration

# In[10]:


# [ ] create & print a variable, other_word, made of every other letter in long_word
long_word = "juxtaposition"
oWord = long_word[::2]
print(oWord)


# In[1]:


# Mirror Color
# [ ] get user input, fav_color
# [ ] print fav_color backwards + fav_color
# example: "Red" prints "deRRed"
fColor = input()
print(fColor[::-1] + fColor)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
