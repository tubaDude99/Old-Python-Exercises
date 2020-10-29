#!/usr/bin/env python
# coding: utf-8

# # Section 4.1
# ## Files Import, Open, and Read
# - File import in Jupyter Notebooks
# - File `open(`) and `.read()`
# 
# ----- 
# 
# ### Student will be able to
# - Import files in Jupyter Notebooks using the curl command
# - `open()` and `.read()` local files in memory
# - `.read()` a specific number of characters

# ## Concept: Import Files to Jupyter
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/850e52a7-2082-4cb7-926f-54bf2527cee0/Unit2_Section4.1a-Import_Files_to_Jupyter.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/850e52a7-2082-4cb7-926f-54bf2527cee0/Unit2_Section4.1a-Import_Files_to_Jupyter.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### curl imports files to Jupyter session from a web address
# Below is code using curl to import poem1.txt, the code is in a command line interface syntax.
# 
# >#### `!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt`  
# 
# The table explains each element of the  command above.  
# 
# | code | meaning |
# |-----|---|
# | **`!`** | runs command interface supporting **curl** | 
# | **`curl`** | enables **curl** that can download files |  
# | **`https://raw.githubusercontent.com/...`** | is the address for data file to import |  
# | **`-o`** | tells **`curl`** write data to a file |  
# | ** *`poem1.txt`* ** | name **`curl`** will give the file  |
# 

# ### Examples

# In[2]:


# [ ] review and run example
get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt')


# ## Concept: Opening a local file in read mode
# >```python
# poem_file = open('poem1.txt', 'r') 
# ```  
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/07e5f863-e416-4534-a45c-df50d0d3df33/Unit2_Section4.1b-Opening_Files_Read_Mode.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/07e5f863-e416-4534-a45c-df50d0d3df33/Unit2_Section4.1b-Opening_Files_Read_Mode.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Read  mode &nbsp; `'r'`
# | MODE    |  Description  |
# |:-------:|:--------------|
# | **'r'**  | **read only mode** |
# | 'w'  | write - overwrites file with same name |
# | 'r+' | read and write mode |
# | 'a'  | opens for appending to end of file |
# 
# ### `open()` creates an object that can be addressed in python code

# ### Examples

# In[3]:


# [ ]Run to open the file in memory as poem_file
poem_file = open('poem1.txt', 'r')


# In[4]:


# [ ] run and review code to test if open worked 
# should display name='poem1.txt' and no errors
poem_file


# ## Task 1: Import and open a local file in read mode
# 1. **Import a list of cities using curl**  
#   a. Get the list from https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities  
#   b. Name the list cities.txt  
# 2. **Open cities.txt in read mode using a variable = cities_file**  
# 3. **Test that cities_file opened cities.txt with a print statement**  

# In[5]:


# [ ] import cities.txt
get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/cities -o cities.txt')


# In[6]:


# [ ] open cities.txt as cities_file
# [ ] test cities.txt was opened 
cities_file = open('cities.txt', 'r')
cities_file


# ## Concept: Read a file using `.read()`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c37a03df-7d95-4339-8fec-8f199b747a08/Unit2_Section4.1c-Reading_Files.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c37a03df-7d95-4339-8fec-8f199b747a08/Unit2_Section4.1c-Reading_Files.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### reading text
# ```python
# poem_contents = poem_file.read()
# ```
# ### `.read()` loads the content of the file into memory as a string, including formatting such as new line (`\n`)

# ### Examples
# Note: The examples expect that the cells that import and open poem1.txt have been run without a read().
# Run the cells that import and open poem1.txt.

# In[7]:


# [ ] review and run example
poem_contents = poem_file.read()


# In[8]:


# [ ] review and run example
# shows the file as a string with formatting characters such as "\n", output should be non-blank
poem_contents


# In[9]:


# [ ] review and run example
# since .read() loaded the file as a string it can be printed
print(poem_contents)


# ## Task 2: Read a file
# ### Read the file cities.text that was imported in Task 1
# 1. **Import and open cities.txt**  
#   a. Ensure the code was created and run in **Task 1** to import cities.txt  
#   b. Create and run code to re-open cities.txt as cities_file  
# 2. **read() cities_file into a variable called cities**
# 3. Test the read() by displaying the string contained in cities
# 4. Test the read() by printing the cities string

# In[10]:


# [ ] after import and open of cities.txt in task 1
# [ ] read cities_file as cities
# [ ] display the string: cities
cities = cities_file.read()


# In[11]:


# [ ] print the string: cities
print(cities)


# ## Concept: Reading a file with `.read(n)` 
# ### Where n = number of characters to read
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/9960a973-339b-40e1-b5b3-1f7db661934e/Unit2_Section4.1d-Reading_Number_of_Characters.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/9960a973-339b-40e1-b5b3-1f7db661934e/Unit2_Section4.1d-Reading_Number_of_Characters.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Each time `poem_file.read(10)` runs, the next 10 characters are read.
# 
# > **Note:** if .read(10) result is = '' &nbsp;(or empty string with no characters), it is likely that the end of the file has been reached. Perform a fresh **.open()** to reset read() to the beginning of the file.

# ### Examples
# Note: The examples expect that the cells that import and open poem1.txt have been run without a read().
# Run the cell at the top of the notebook to ** import poem1.txt**.
# Each line is a different approach to reading and displaying 10 characters of the poem.

# In[12]:


# [ ] review and run example to read poem1.txt 10 characters at a time
poem_file = open('poem1.txt', 'r')
poem_10char = poem_file.read(10)
print(poem_10char)
poem_10char


# In[13]:


# [ ] review and run example, + 10 more characters
# reads and displays without storing in a variable
poem_file.read(10)


# In[14]:


# [ ] review and run example, + 10 more characters
# reads and stores in variable poem_parts
poem_parts = poem_file.read(10)
print(poem_parts)


# In[15]:


# [ ] REPEATEDLY RUN this cell,  + 5 more characters each time run are appended using string addition
# [ ]  consider why no additional text displays after multiple runs
poem_parts += poem_file.read(5)
print(poem_parts)


# ## Task 3: Digits of pi  
# ### Read a set number of digits with .read(n)
# ### Import, open, read, print
# 1. Import digits_of_pi.txt located at https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi  
# 2. Open as **digits_of_pi_text** 
# 3. Read()the first 4 characters of digits_of_pi_text into a variable called pi_digits  
# 4. Print pi_digits  
# 5. Add to pi_digits string with string addition  
#   a. Add next 4 characters from digits_of_pi obtained from read()  
#   b. Run the cell multiple times to get more digits of *pi*  

# In[24]:


# [ ] digits of pi
# 1. import digits_of_pi.txt
get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi -o dPi.txt')


# In[25]:


# [ ] digits of pi
# 2. open as digits_of_pi_text 
# 3. read() 4 char of digits_of_pi_text to pi_digits variable 
# 4. print pi_digits  
dPiTxt = open('dPi.txt', 'r')
piD = dPiTxt.read(4)
print(piD)


# In[35]:


# [ ] digits of pi
# 5. add to pi_digits string with string addition  
#   a. add next 4 characters from digits_of_pi obtained from read()  
#   b. run the cell multiple times to get more digits of *pi*
piD += dPiTxt.read(4)
print(piD)


# ## Concept: .read() returns a string 
# ### These strings can be manipulated just like any other string
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/f7fb0136-24a3-4a0e-aff2-b1abc2f83029/Unit2_Section4.1e-Read_Returns_a_String.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/f7fb0136-24a3-4a0e-aff2-b1abc2f83029/Unit2_Section4.1e-Read_Returns_a_String.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Boolean tests such as:
# - .upper()  
# - .title() 
# - string slices, e.g.- `cities[3:9]`  
# - etc..  
# 
# ### And string methods can be performed such as:
# - .isdigit()  
# - .isalpha()  
# - etc...

# ### Examples
# Note: The examples expect that the cells that import have has been run.
# It may be necessary to run the cell to **import poem1.txt** at the beginning of this notebook.

# In[37]:


# [ ] review and run example
poem_file = open('poem1.txt', 'r')
poem_part = poem_file.read(15).upper()
print(poem_part)


# In[38]:


# [ ] review and run example
poem_part = poem_file.read(6).title()
print(poem_part)


# In[39]:


# [ ] review and run example
poem_part = poem_file.read(6)
print(poem_part)
print(poem_part.isalpha(), "isalpha() because of `\\n`")
poem_part


# In[40]:


# [ ] review and run example
poem_file = open('poem1.txt', 'r')
poem_text = poem_file.read()
print(poem_text[8:26])


# ## Task 4: City Initials
# ### Read the file cities.text that was imported in Task 1
# 1. Ensure the code was created and run in **Task 1** to import cities.txt  
# 2. Create and run code to re-open cities.txt as cities_file  
# 3. **`read()`** cities_file into a variable called cities  
# 4. Iterate through the characters in cities 
#   a. Test if .isupper(), if True append the character to a string variable: initials
#   c. Else if (elif) character is "\n", if True append the "\n" to initials  
# 5. Print initials

# In[43]:


# [ ] complete the task
cities_file = open('cities.txt', 'r')
cities = cities_file.read()
initials = ""
for x in cities:
    if x.isupper():
        initials += x
    elif x == '\n':
        initials += '\n'
print(initials)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
