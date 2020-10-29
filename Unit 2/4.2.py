#!/usr/bin/env python
# coding: utf-8

# # Section 4.2
# ## File .readlines() and .close() Methods
# - File Read as a list with `.readlines()`
# - File Closing to free resources with `.close()`
# 
# ----- 
# 
# ### Student will be able to
# - Use `.readlines()` to read text from files as a list of lines
# - Use `.close` to free system resources

# ## Concept: `.readlines()`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/0cd43d02-5eac-40b5-ba2d-97f078415ddd/Unit2_Section4.2a-Readlines-Open_Text_as_List.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/0cd43d02-5eac-40b5-ba2d-97f078415ddd/Unit2_Section4.2a-Readlines-Open_Text_as_List.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# ### File read as a list with .readlines() 
# Converts the lines of a file into a **list** of strings.
# 
# ```python
# poem_lines = poem1.readlines()
# ```

# ### Examples

# In[2]:


# [ ] Run to download file to notebook
get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt')


# In[3]:


# [ ] review and run example
# open address to file
poem1 = open('poem1.txt', 'r')

# readlines and print as a list
poem_lines = poem1.readlines()
poem_lines


# In[4]:


# [ ] review and run example
for line in poem_lines:
    print(line)


# ## Task 1: `.readlines()` 
# ### Open the cities file as a list
# 1. **Import a list of cities using curl**  
#   a. Git the list from https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities  
#   b. Name the list cities.txt  
# 2. **Open cities.txt in read mode using a variable: cities_file**  
# 3. **Read cities_file as a list variable: cities_lines using `.readlines()`**
# 4. **Print each line of cities_lines by iterating the list**

# In[5]:


# [ ] import cities

get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt')


# In[6]:


# [ ] open cities.txt as cities_file and read the file as a list: cities_lines
cities_file = open('cities.txt', 'r')
cities_lines = cities_file.readlines()


# In[7]:


# [ ] use list iteration to print each city in cities_lines list
for x in cities_lines:
    print(x)


# ## Concept: Working with lists from .readlines()
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ed9b1523-6d69-462c-b18c-01e5423c1e52/Unit2_Section4.2b-Readlines-Remove_Characters.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ed9b1523-6d69-462c-b18c-01e5423c1e52/Unit2_Section4.2b-Readlines-Remove_Characters.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ###  Remove newline characters from lists created using .readlines()
# ```python
# for line in poem_lines:
#     poem_lines[count] = line[:-1]
#     count += 1
# ```
# **`line[:-1]`** sets the end point at the last character of the string, the result is the **`'\n'`** (newline) character is omitted.
# 
# | list item | list item contents | 
# |-----|-----|
# | poem_lines[0] | 'Loops I repeat\n' |  
# | poem_lines[1] | 'loops\n' |  
# | poem_lines[2] | 'loops\n' | 
# | poem_lines[3] | 'I repeat\n' | 
# |... | ... | 

# ### Examples
# Note: The examples assume that poem1.txt was imported in the first example above.

# In[8]:


# [ ] review and run examples
# [ ] re-open file and read file as a list of strings
poem1 = open('poem1.txt', 'r')
poem_lines = poem1.readlines()
print(poem_lines)


# In[9]:


# [ ] print each list item 
for line in poem_lines:
    print(line)


# In[10]:


# [ ] remove the last character of each list item, which is "\n"
count = 0

for line in poem_lines:
    poem_lines[count] = line[:-1]
    count += 1

print(poem_lines)


# In[11]:


# [ ] print each list item 
for line in poem_lines:
    print(line)


# ## Task 2: Remove newline characters from cities lists created using .readlines()
# - This task assumes that cites.txt has been imported in Task 1 above
# - In Task 1, the cities were printed with a blank line between each city - this task removes the blank lines
# 

# In[25]:


# [ ] re-open file and read file as a list of strings 
# [ ] open cities.txt as cities_file and read the file as a list: cities_lines
cities_file = open('cities.txt', 'r')
cities_lines = cities_file.readlines()


# In[26]:


# [ ] remove the last character, "\n", of each cities_lines list item 
for x in range(len(cities_lines)):
    cities_lines[x] = cities_lines[x][0:-1]


# In[27]:


# [ ] print each list item in cities_lines
for line in cities_lines:
    print(line)


# ## Concept: `.close()`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/50a925e8-25e2-4bfa-936b-e2d181af36f0/Unit2_Section4.2c-File_Close_Method.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/50a925e8-25e2-4bfa-936b-e2d181af36f0/Unit2_Section4.2c-File_Close_Method.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### File .close() method frees resources 
# The file.close() method removes the reference created by the file open() function. 
# 
# ```python  
# poem1.close()
# ```  

# ### Examples  
# Note: The examples assume that poem1.txt was imported in the first example above.

# In[29]:


# [ ] review and run example: open and readlines of poem1.txt
poem1 = open('poem1.txt', 'r')


# In[30]:


# [ ] review and run example: readlines breaks if file is no longer open

poem_lines = poem1.readlines()
print(poem_lines)


# In[31]:


# [ ] review and run example: Close poem1
poem1.close()


# ## Task 3: File .close() 
# Write each item in its own cell.
# - Open cities.txt as cities_file  
# - Read the lines as cities_lines
# - Print the cities that **start with the letter "D" or greater**  
# - Close cities_file
# - Test that file is closed

# In[1]:


# [ ] open cities.txt as cities_file
cities_file = open('cities.txt', 'r')


# In[2]:


# [ ] read the lines as cities_lines
cities_lines = cities_file.readlines()


# In[3]:


# [ ] print the cities that start with the letter "D" or greater
for x in cities_lines:
    if x >= 'D':
        print(x)


# In[4]:


# [ ] close cities_file
cities_file.close()


# In[7]:


# [ ] test that file is closed
cities_file.closed


# ## Task 4: readlines() poem2  
# Write each item in its own cell.
# - Import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2.txt as poem2.txt  
# - Open poem2.txt as poem2_file in read mode
# - Create a list of strings, called poem2_lines, from each line of poem2_text (use **.readlines()**)  
# - Remove the newline character for each list item in poem2_lines  
# - Print the poem2 lines in reverse order  

# In[52]:


# [ ] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2.txt as poem2.txt
get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2.txt -o poem2.txt')


# In[53]:


# [ ] open poem2.txt as poem2_text in read mode
poem2_text = open('poem2.txt', 'r')


# In[54]:


# [ ] create a list of strings, called poem2_lines, from each line of poem2_text
poem2_lines = poem2_text.readlines()


# In[55]:


# [ ] remove the newline character for each list item in poem2_lines
for x in range(len(poem2_lines)):
    poem2_lines[x] = poem2_lines[x][0:-1]


# In[56]:


# [ ] print the poem2 lines in reverse order
poem2_lines.reverse()
print(poem2_lines)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
