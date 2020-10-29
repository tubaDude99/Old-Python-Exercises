#!/usr/bin/env python
# coding: utf-8

# # Section 1.8
# ## Quote Display and Boolean
# - input() - gathering user input  
# - print() formatting  
# - **Quotes inside strings** 
# - **Boolean string tests methods**  
# - String formatting methods
# - Formatting string input()
# - Boolean `in` keyword 
# 
# -----
# 
# ### Student will be able to
# - Gather, store and use string `input()`  
# - Format `print()` output  
# - **Test string characteristics**  
# - Format string output
# - Search for a string in a string

# ## Concept: Quotes Inside Strings 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c21bfb29-21f6-4bef-b00e-25d2f7440153/Unit1_Section2-3-Quotes_in_Strings.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c21bfb29-21f6-4bef-b00e-25d2f7440153/Unit1_Section2-3-Quotes_in_Strings.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Single quotes in double quotes
# To display single quotes **`'`** in a string - double quotes can be used as the outer quotes: **`"it's time"`**.
# ### Double quotes in single quotes
# To display double quotes **`"`** in a string- single quotes can be used as the outer quotes: **`'Alton said "Hello"'`**.

# ### Examples

# In[1]:


# review and run the code

# Single quote surrounded by Double
print("It's time to save your code")

# Double quote surrounded by Single
print('I said to the class "sometimes you need to shut down and restart a notebook when cells refuse to run"')


# ## Task 1: Print with quotes
# - **[ ] `print()`** strings that display double and single quotation marks

# In[1]:


# [ ] using a print statement, display the text: Where's the homework?
print("Where's the homework?")


# In[2]:


# [ ] output with double quotes: "Education is what remains after one has forgotten what one has learned in school" - Albert Einstein
print('"Education is what remains after one has forgotten what one has learned in school" - Albert Einstein')


# >**Note:** Quotes in quotes handles only simple cases of displaying quotation marks.  More complex cases are covered later under *escape sequences.*

# ## Concept: Boolean String Tests
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"https://jupyternootbookwams.streaming.mediaservices.windows.net/dfe6e85f-8022-471c-8d92-0b1d61ebffbd/Unit1_Section2-3-Boolean_String_Methods.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"https://jupyternootbookwams.streaming.mediaservices.windows.net/dfe6e85f-8022-471c-8d92-0b1d61ebffbd/Unit1_Section2-3-Boolean_String_Methods.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# Methods:
# - .isalpha()
# - .isalnum()
# - .istitle()
# - .isdigit()
# - .islower()
# - .isupper()
# - .startswith()
# 
# Type **`str`** has methods that return a Boolean (True or False) for different tests on the properties of strings.
# >```Python
# "Hello".isapha()
# ```
# out:[ ] &nbsp; &nbsp; `True`  
#   
# `.isalpha()` returns True if all characters in the string ("Hello") are alphabetical, otherwise returns False.
# 

# ### Examples: Boolean String Tests
# - **[ ] Review and run code in each cell**

# In[3]:


"Python".isalpha()


# In[4]:


"3rd".isalnum()


# In[5]:


"A Cold Stromy Night".istitle()


# In[6]:


"1003".isdigit()


# In[7]:


cm_height = "176"
print("cm height:",cm_height, "is all digits =",cm_height.isdigit())


# In[8]:


print("SAVE".islower())
print("SAVE".isupper())


# In[12]:


"Boolean".startswith("B")


# ## Task 2 (multi-part): Test strings with **`.isalpha()`**

# In[13]:


# [ ] Use .isalpha() on the string "alphabetical"
"alphabetical".isalpha()


# In[16]:


# [ ] Use .isalpha() on the string: "Are spaces and punctuation Alphabetical?"
"Are spaces and punctuation Alphabetical?".isalpha()


# In[17]:


# [ ] initailize variable alpha_test with input
alpha_test = input("?")
# [ ] use .isalpha() on string variable alpha_test
alpha_test.isalpha()


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
