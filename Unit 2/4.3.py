#!/usr/bin/env python
# coding: utf-8

# # Section 4.3
# ## File .readline() and .strip() Methods
# - File Read, a line at a time with `.readline()`
# - Remove characters using `.strip()`
# 
# ----- 
# 
# ### Student will be able to
# - Use `.readline()` to read data from file, one line at a time
# - Use `.strip()` to remove new line characters and other whitespaces

# ## Concept: Read files a line at a time
# ### .readline()
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/8f41bf3b-05b1-459e-87e9-419168b2bf0d/Unit2_Section4.3a-Readlines-Line_by_Line.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/8f41bf3b-05b1-459e-87e9-419168b2bf0d/Unit2_Section4.3a-Readlines-Line_by_Line.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Use .readline() to read a line in a file as a string
# Each .readline() moves to the next available line in the file.
# ```python
# poem1 = open('poem1.txt', 'r')
# poem_line1 = poem1.readline()
# poem_line2 = poem1.readline()
# poem_line3 = poem1.readline()
# ```

# ### Examples

# In[1]:


# [ ]Run to download file poem1.txt
get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt ')


# In[2]:


# [ ] review and run example
# open address to file
poem1 = open('poem1.txt', 'r')


# In[3]:


# [ ] review and run example
# readline 1, 2, 3
poem_line1 = poem1.readline()
poem_line2 = poem1.readline()
poem_line3 = poem1.readline()


# In[4]:


# [ ] review and run example: print the first 3 .readline() values
print(poem_line1 + poem_line2 + poem_line3)


# In[5]:


# [ ] review and run example printing return value & re-run several times
print(poem1.readline())


# In[6]:


# [ ] review and run example to close file in memory- then run previous cell

poem1.close()


# ## Task 1: Use readline to get rainbow colors
# - Import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow as rainbow.txt  
# - Open rainbow.txt as rainbow_file as read-only  
# - Read the first 3 lines into variables: color1, color2, color3  
# - Close rainbow_file 
# - Print the first 3 colors  

# In[7]:


# [ ] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow as rainbow.txt
get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow -o rainbow.txt')


# In[9]:


# [ ] open rainbow.txt as rainbow_text
rainbow_text = open('rainbow.txt', 'r')


# In[10]:


# [ ] read the first 3 lines into variables: color1, color2, color3
color1 = rainbow_text.readline()
color2 = rainbow_text.readline()
color3 = rainbow_text.readline()


# In[12]:


# [ ] close rainbow.txt
rainbow_text.close()


# In[14]:


# [ ] print the first 3 colors
print(color1 + color2 + color3)


# ## Concept: `.readline()` in a `while` loop
# >```python
# poem_line = poem1.readline()
# while poem_line:
#     print(poem_line.capitalized())
#     poem_line = poem1.readline()
# ```  
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/4662ff60-8839-4fd7-a85d-3aba9ebf8cd3/Unit2_Section4.3b-Readlines-While_Loops.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/4662ff60-8839-4fd7-a85d-3aba9ebf8cd3/Unit2_Section4.3b-Readlines-While_Loops.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### `while .readline()` 
# - while loop continues while the readline() value in poem_line returns text  
#   - A string value evaluates as True in the while loop  
#   - An empty string, '', evaluates **not True** in the while loop 
# - When readline() reaches the end of the file, an empty string is returned  
# 

# ### Examples

# In[15]:


# [ ] review and run example
# open address to file
poem1 = open('poem1.txt', 'r')


# In[16]:


# [ ] review and run example - use a while loop to read each line of a file 
#  remove last character ('\n') and print as upper case
poem_line = poem1.readline()

while poem_line:
    print(poem_line[:-1].upper())
    poem_line = poem1.readline()


# In[17]:


# [ ] review and run example
poem1.close()


# ## Task 2: while .readline() rainbow colors
# Note: Assumes rainbow.txt has been imported in Task 1.
# 
# - Open rainbow.txt as rainbow_file as read-only  
# - Read a color from each line of rainbow_file in a while loop  
#   - Print each color capitalized  
# - Close rainbow_file  

# In[29]:


# [ ] open rainbow.txt as rainbow_text as read-only
rainbow_text = open('rainbow.txt', 'r')


# In[30]:


# [ ] read the color from lines of rainbow_text in a while loop
# [ ] print each color capitalized as the loop runs
rainbow_line = rainbow_text.readline()
while rainbow_line:
    print(rainbow_line)
    rainbow_line = rainbow_text.readline()


# In[31]:


# [ ] close rainbow_text 
rainbow_text.close()


# ## Concept: `.readline()`  with `.strip()`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/809d6b2c-1be9-4bea-8702-9eb328b9f551/Unit2_Section4.3c-Remove_Whitespace.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/809d6b2c-1be9-4bea-8702-9eb328b9f551/Unit2_Section4.3c-Remove_Whitespace.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### .strip() whitespace
# ```python
# poem_line = poem1.readline().strip()
# ```
# **.strip()** removes leading and trailing whitespace, including the '\n' formatting character.

# ### Examples

# In[24]:


# [ ] review and run example
# open address to file
poem1 = open('poem1.txt', 'r')


# In[25]:


# [ ] review and run example - readline while loop without removing '\n'
poem_line = poem1.readline()

while poem_line:
    print(poem_line)
    poem_line = poem1.readline()

poem1.close()


# ### Now with `.strip()` to remove leading and trailing whitespace characters

# In[26]:


# [ ] review and run example - readline with .strip() to remove '\n'
poem1 = open('poem1.txt', 'r')
poem_line = poem1.readline().strip()

while poem_line:
    print(poem_line)
    poem_line = poem1.readline().strip()
    
poem1.close()


# ## Task 3: `.readline()`  with `.strip()` rainbow colors
# Note: Assumes rainbow.txt has been imported in Task 1.
# 
# - Open rainbow.txt as rainbow_file as read-only  
# - Read a color from each line of rainbow_file in a while loop  
#   - Use .strip to remove the whitespace  
#   - Print each color upper case  
# - Close rainbow_file 

# In[32]:


# [ ] open rainbow.txt as rainbow_text as read-only  
rainbow_text = open('rainbow.txt', 'r')


# In[33]:


# [ ] read a color from each line of rainbow_text in a while loop  
# use .strip to remove the whitespace '\n' character 
# print each color upper case 
rainbow_line = rainbow_text.readline().strip()
while rainbow_line:
    print(rainbow_line)
    rainbow_line = rainbow_text.readline().strip()


# ## Concept: `.strip()` with arguments
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/98672edd-b2c5-4478-aaec-42154a5b97c8/Unit2_Section4.3d-Strip_Arguments.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/98672edd-b2c5-4478-aaec-42154a5b97c8/Unit2_Section4.3d-Strip_Arguments.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### .strip() arguments
# ```python
# color = rainbow_messy.readline().strip('*\n*')
# ```
# **`.strip('*\n')`** removes leading and training **`*`** and **\n**.

# ### Examples

# In[34]:


# [ ] review and run example: import rainbow_messy.txt
get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow_messy -o rainbow_messy.txt')


# In[35]:


# [ ] review and run example: open file read only
rainbow_messy = open('rainbow_messy.txt', 'r')


# In[36]:


# [ ] review and run example: .readline() without .strip()

color = rainbow_messy.readline()

while color:
    print(color)
    color = rainbow_messy.readline()


# In[37]:


# [ ] review and run example: strip "*" and newline ('\n')
rainbow_messy = open('rainbow_messy.txt', 'r')

color = rainbow_messy.readline().strip('*\n')

while color:
    print(color)
    color = rainbow_messy.readline().strip('*\n')

rainbow_messy.close()


# ## Task 4: `.strip()` with arguments
# 
# - Run import of cities_messy.txt below at least once this notebook session
# - Run open cities_messy.txt below before each test of the while loop cell
# - Edit while loop to strip the colon ':' , newline and spaces
# - Close cities_messy

# In[44]:


# [ ] import the file
get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities_messy -o cities_messy.txt')


# In[45]:


# [ ] run to read the file into memory
cities_messy = open('cities_messy.txt', 'r')


# In[46]:


# [ ] edit the code to remove leading or trailing colon, newline and space characters
line = cities_messy.readline().strip(": \n")

while line:
    print(line)
    line = cities_messy.readline().strip(": \n")


# ## Task 5: `.strip()` parentheses from poem2_messy
# 
# - Import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2_messy as poem2_messy.txt  
# - Open poem2_messy.txt as poem2_messy in read mode  
# - Edit while loop to strip the leading and trailing parentheses & print the poem without blank lines  
# - Close poem2_messy

# In[47]:


# [ ] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2_messy as poem2_messy.txt  
get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2_messy -o poem2_messy.txt')


# In[48]:


# [ ] open poem2_messy.txt as poem2_messy in read mode
poem2_messy = open('poem2_messy.txt', 'r')


# In[49]:


# [ ] edit while loop to strip the leading and trailing parenthesis, and newlines
# [ ] print the poem 
line = poem2_messy.readline().strip('()\n')

while line:
    print(line)
    line = poem2_messy.readline().strip('()\n')


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
