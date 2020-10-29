#!/usr/bin/env python
# coding: utf-8

# # Section 3.2
# ## Conditionals: Comparison Operators
# - **`if`, `else`, `pass`**  
#   - Conditionals using Boolean string methods
#   - **Comparison operators**
#   - String comparisons
# 
# ----- 
# 
# ### Student will be able to
# - **Control code flow with `if`... `else` conditional logic**  
#   - Using Boolean string methods (`.isupper(), .isalpha(), startswith()...`)  
#   - **Using comparison (`>, <, >=, <=, ==, !=`)**  
#   - Using strings in comparisons  

# ## Concept: Comparison Operators 
#  - **`>`**
#  - **`<`**
#  - **`>=`**, **`<=`**
#  - **`==`**
#  - Assign **`=`** vs compare **`==`**
#  - **`!=`** 
#  
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/cf192500-3879-4228-bd50-70dd3f38d831/Unit1_Section4.2-comparison-operators.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/cf192500-3879-4228-bd50-70dd3f38d831/Unit1_Section4.2-comparison-operators.vtt","srclang":"en","kind":"subtitles","label":"english"}])

# ### Examples

# In[1]:


# [ ] review and run code to see if 3 greater than 5
3 > 5


# In[2]:


# [ ] review and run code to see if 3 less than or equal to 5
3 <= 5


# In[3]:


# [ ] review and run code 

# assign x equal to 3
x = 3

# test if x is equal to
x == 9


# In[4]:


# [ ] review and run code 
x = 3
print("x not equal 9 is", x != 9)
print("x equal 3 is", x == 3)


# ## Task 1: Comparison operators

# In[5]:


X = 9 + 4
# [ ] create a test to print() True or False for x is equal to 13
print(X == 13)


# In[6]:


# [ ] create a test to print True or False for 3 + 3 is greater than 2 + 4
print(3+3 > 2+4)


# ## Concept:  Comparison Operators in Conditionals
# ### Conditionals: Comparison operators with `if`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/15e3b015-e83b-4ab8-8375-b11e52a348ea/Unit1_Section4.2-conditional-if.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/15e3b015-e83b-4ab8-8375-b11e52a348ea/Unit1_Section4.2-conditional-if.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# Comparison operators evaluate to Boolean **`True`** and **`False`** to direct the flow of **`if`** conditionals.

# ### Examples

# In[7]:


# review code and run cell
x = 21
if x > 25:
    print("x is already bigger than 25")
else:
    print("x was", x)
    x = 25
    print("now x is", x)


# In[8]:


# review code and run cell
x = 18
if x + 18 == x + x:
    print("Pass: x + 18 is equal to", x + x)
else:
    print("Fail: x + 18 is not equal to", x + x)


# In[9]:


# review code and run cell. "!" means "not"
x = 18
test_value = 18
if x != test_value:
    print('x is not', test_value)
else:
    print('x is', test_value)


# In[10]:


# review code and run cell
# DON'T ASSIGN (x = 2) when you mean to COMPARE (x == 2)
x = 2

if x = 2:
    print('"==" tests for, is equal to')
else:
    pass


# ## Task 2: Evaluating a comparison operator in `if`

# In[11]:


# [ ] create an if/else statement that tests if y is greater than or equal x + x 
# [ ] print output: "y greater than or equal x + x is" True/False ...or a similar output
x = 3
y = x + 8
if y >= x+x:
    print("y greater than or equal x + x is", y >= x+x)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
