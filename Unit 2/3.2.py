#!/usr/bin/env python
# coding: utf-8

# # Section 3.2
# # Range Iteration
# - for in: `for` loop using `in`
# - **for range: `for range(start,stop,step)`**
# - More list methods: `.extend()`, `+, .reverse(), .sort()` 
# - Strings to lists,`.split()`, and list to strings, `.join()` 
# ----- 
# 
# ### Student will be able to
# - Iterate through lists using `for` with `in`
# - **Use `for range()` in looping operations**
# - Use list methods `.extend()`, `+, .reverse(), .sort()` 
# - Convert between lists and strings using `.split()` and `.join()` 

# ## Concept: `range(stop)`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/bda2424d-4f25-4c0a-a77a-06384f3da8f2/Unit2_Section3.2a_range_stop.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/bda2424d-4f25-4c0a-a77a-06384f3da8f2/Unit2_Section3.2a_range_stop.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### The range(*stop*) function creates a sequence  
# Using 1 argument with range(*stop*):
# - Default start: 0
# - stop: stopping integer, does not process stop number
# ```python
# for count in range(10):
#   print(count)
# ```
# ### Same as
# ```python
# for count in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#   print(count)
# ```
# 

# ### Examples: Range runs from `0` through the integer before `stop`

# In[10]:


# [ ] review and run example
for count in range(10):
    print(count)


# In[11]:


# review and run example
digits = range(10)
print("digits =", list(digits), "\n")

for count in digits:
    print(count)


# In[12]:


# [ ] review and run example
sub_total = 0
for item in range(10):
    sub_total += item
    print("sub_total:", sub_total)
print("Total =", sub_total)


# In[13]:


# [ ] review and run example
# print the first half of a spelling list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

# find length of 1st half of list (must be int)
half_1 = int(len(spell_list)/2)

for word in range(half_1):
    print(spell_list[word])


# ## Task 1: `range(stop)`

# In[14]:


# [ ] for x = 6, use range(x) to print the numbers 1 through 6
x = 6
for i in range(x):
    print(i)


# In[15]:


# [ ] using range(x) multiply the numbers 1 through 7
# 1x2x3x4x5x6x7 = 5040
x = 1
for i in range(1,8):
    x = x * i
print(x)


# Use **`range(stop)`** to print the second half of spell_list below

# In[16]:


# [ ] print the second half of a spelling list using a range(stop) loop to iterate the list
spell_list = ["Wednesday", "Tuesday", "February", "November", "Annual", "Calendar", "Solstice"]
for x in range(int(len(spell_list)/-2),0):
    print(spell_list[x])


# ## Concept: `range(start,stop)`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/95d6c75a-ed37-4f50-9049-2a2c225f9499/Unit2_Section3.2b_range_start_stop.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/95d6c75a-ed37-4f50-9049-2a2c225f9499/Unit2_Section3.2b_range_start_stop.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### The range(*start,stop*) function creates a sequence
# Using 2 arguments with range(*start,stop*):
# - start: starting integer value of a range loop
# - stop: stopping integer (second argument), does not process stop number 
# ```python
# for count in range(5,10):
#   print(count)
# ```
# 

# ### Examples: Range runs from `start` integer through the integer before `stop`

# In[17]:


# [ ] review and run example
for count in range(5,10):
    print(count)


# In[18]:


# [ ] review and run example
sub_total = 0
temp = 0
for item in range(5, 11):
    temp = sub_total
    sub_total += item
    print("sub_total:", temp, "+", item, "=",sub_total)
print("Total =", sub_total)


# In[19]:


# [ ] review and run example

spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

# find length list 
spell_len = len(spell_list)
# find lenght of 1st half (aka - start of 2nd half)
half_1 = int(spell_len/2)

# print 2nd half list
for word in range(half_1,spell_len):
    print(spell_list[word])


# ## Task 2: `range(start,stop)`

# In[20]:


# [ ] using range(start,stop), .append() the numbers 5 to 15 to the list: five_fifteen
# [ ] print list five_fifteen
fFt =[]
for x in range(5,16):
    fFt.append(x)
print(fFt)


# In[21]:


# [ ] using range(start,stop) - print the 3rd, 4th and 5th words in spell_list
# output should include "February", "November", "Annual"
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
for x in range(3,6):
    print(spell_list[x])


# In[22]:


# [ ] using code find the index of "Annual" in spell_list
# [ ] using range, print the spell_list including "Annual" to end of list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
print(spell_list[spell_list.index("Annual"):])


# ## Concept: `range(start,stop,step)`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/4299f0e2-3dc2-4298-aff1-e2a0b013de6a/Unit2_Section3.2c_range_start_stop_step.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/4299f0e2-3dc2-4298-aff1-e2a0b013de6a/Unit2_Section3.2c_range_start_stop_step.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### The range(*start,stop,step*) function creates a sequence
# Using 3 arguments with range(*start,stop,step*):
# - start: starting integer value of a range loop
# - stop: stopping integer (second argument), does not process stop number 
# - step: skip value for each loop
# ```python
# for count in range(10,101,10):
#   print(count)
# ```
# 

# ### Examples: Range runs from `start` integer, skipping by `step`, through the largest `step` integer before reaching `stop`

# In[23]:


# [ ] review and run example
for count in range(25,101,25):
    print(count)


# In[24]:


# [ ] review and run example
sub_total = 0
temp = 0
for item in range(25,46,5):
    temp = sub_total
    sub_total += item
    print("sub_total:", temp, "+", item, "=",sub_total)
print("Total =", sub_total)


# In[25]:


# [ ] review and run example printing the 1st and then every other word in spell_list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

for index in range(0,len(spell_list),2):
    print(spell_list[index])


# In[26]:


# [ ] review and run example casting range to list
odd_list = list(range(1,20,2))
print(odd_list)


# ## Task 3: `range(start,stop,step)`

# In[28]:


# [ ] print numbers 10 to 20 by 2's using range
for x in range(10,21,2):
    print(x)


# In[32]:


# [ ] print numbers 20 to 10 using range (need to countdown)
# Hint: start at 20
for x in range(20,9,-1):
    print(x)


# In[33]:


# [ ] print first and every third word in spell_list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
print(spell_list[::3])


# ## Task 4 (program): List of letters 
# - Input a word string (**word**)
# - Find the string length of word 
# - **use range()** to iterate through each letter in word (can use to range loops)
# - Save odd and even letters from the word as lists
#   - **odd_letters**: starting at index 0,2,...
#   - **even_letters**: starting at index 1,3,...
# - Print odd and even lists

# In[2]:


# [ ] complete List of letters program- test with the word "complexity"
word = input()
print(len(word))
odd = []
evn = []
for x in range(len(word)):
    if x%2 == 0:
        odd.append(word[x])
    else:
        evn.append(word[x])
print(odd)
print(evn)


# ## Task 5: Fix the error
# 

# In[4]:


# [ ] fix the error printing odd numbers 1 - 9
for num in range(1,10,2):
    print(num)



# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
