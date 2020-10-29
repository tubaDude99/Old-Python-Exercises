#!/usr/bin/env python
# coding: utf-8

# # Section 1.3
# ##  Type() Function
# - Python 3 in Jupyter notebooks
# - `print()`
# - Comments  
# - **Data types basics**
# - **Variables**  
# - Addition with Strings and Integers
# - Errors  
# - Character art  
# 
# -----
# 
# 
# ### Student will be able to
# - Use Python 3 in Jupyter notebooks
# - Write working code using `print()` and `#` comments  
# - **Write working code using `type()` and variables**
# - Combine Strings using string addition (+)
# - Add numbers in code (+)
# - Troubleshoot errors
# - Create character art

# ## Concept: Using the Python `type()` Function
# **`type()`** returns the data type of Python objects.
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b8fbc662-a42e-4a4a-8cfc-564cb240576e/Unit1_Section1.3-Type.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b8fbc662-a42e-4a4a-8cfc-564cb240576e/Unit1_Section1.3-Type.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# ### `str`, `int`, `float`  
# #### What does using `type()` reveal?
# - **`str`**: when **type()** returns **str** that means it has evaluated a **string** characters (numbers, letters, punctuation...) in quotes 
# - **`int`**: when **type()** returns **int** that means it has evaluated an **Integer** (+/- whole numbers) 
# - **`float`**: when **type()** returns **`float`** that means it has evaluated decimal numbers (e.g. 3.33, 0.01, 9.9999 and 3.0), ...more later in the course

# ### Examples
# - Read and run the code for each sample.

# In[ ]:


# [ ] read and run the code
type("Hello World!")


# In[ ]:


type(501)


# In[ ]:


type(8.33333)


# In[ ]:


student_name = "Colette Browning"
type(student_name)


# ## Task 1 (multi-part): Using `type()`
# - Complete the "identify data types" tasks by assigning  values to the variable&nbsp; **`bucket`** and using **`type()`**.

# In[1]:


# [ ] show the type after assigning bucket = a whole number value such as 16 
bucket = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
type(bucket)


# In[5]:


# [ ] show  the type after assigning bucket = a word in "double quotes"
bucket = "double quotes"
type(bucket)


# In[6]:


# [ ] display the type of 'single quoting' (use single quotes) 
type('single quoting')


# In[7]:


# [ ] display the type of "double quoting" (use double quotes)
type("double quoting")


# In[8]:


# [ ] display the type of "12" (use quotes)
type("12")


# In[9]:


# [ ] display the type of 12 (no quotes)
type(12)


# In[10]:


# [ ] display the type of -12 (no quotes)
type(-12)


# In[11]:


# [ ] display the type of 12.0 (no quotes)
type(12.0)


# In[12]:


# [ ] display the type of 1.55
type(1.55)


# In[15]:


# [ ] find the type of the type(3) statement (no quotes) - just for fun
type(type(3))


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
