#!/usr/bin/env python
# coding: utf-8

# # Section 1.4
# ##  Addition and Errors
# - Python 3 in Jupyter notebooks
# - `print()`
# - Comments  
# - Data types basics
# - Variables  
# - **Addition with Strings and Integers**
# - **Errors**  
# - Character art  
# 
# -----
# 
# ### Student will be able to
# - Use Python 3 in Jupyter notebooks
# - Write working code using `print()` and `#` comments  
# - Write working code using `type()` and variables
# - Combine Strings using string addition (+)
# - **Add numbers in code (+)**  
# - **Troubleshoot errors**  
# - Create character art

# ## Concept: Addition of Numbers and Strings  
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/a8befa5f-b4a5-4081-87c0-8846be85c719/Unit1_Section1.4-Addition.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/a8befa5f-b4a5-4081-87c0-8846be85c719/Unit1_Section1.4-Addition.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# ### Numeric addition
# **Numeric addition:** Single line *math equations*, run in a code cell, will output a sum. 
# ```Python
# # Adding a pair of single digit Integers
# 3 + 5  
# ```  
# ### String addition
# **String addition:** Single line *equations*, run in a code cell, will output a single concatenated string.  
# > **Tip:** all strings must be in quotes  
#     
# ```Python
# # Adding a pair of strings
# "I wear " + "a hat"  
# ```  
# We can also **add variables** as long as we add strings to strings and numbers to numbers.

# ### Examples: String and Number Addition

# In[1]:


# [ ] Review and run code for adding a pair of 2 digit Integers
23 + 18


# In[2]:


# [ ] Review and run code for adding 2 strings
"my name is " + "Alyssa"  


# In[3]:


# [ ] Review and run code for adding a variable string and a literal string
shoe_color = "brown"
"my shoe color is " + shoe_color


# ## Task 1 (multi-part): String and Number Addition

# In[4]:


# [ ] add 3 integer numbers
1 + 2 + 123456789


# In[5]:


# [ ] add a float number and an integer number
1.23 + 123


# In[6]:


# [ ] Add the string "This notebook belongs to " and a string with your first name
"This notebook belongs to " + "Nathan."


# In[7]:


# [ ] Create variables sm_number and big_number and assign numbers then add the numbers
sm_number = 0.054
big_number = 908070605040302010
sm_number + big_number


# In[8]:


# [ ] assign a string value to the variable first_name and add to the string ", remember to save the notebook frequently"
first_name = "Timothy"
first_name + ", remember to save the notebook frequently"


# ## Concept: Use Addition in Variable Assignments  
# It is common to store the results of addition in a variable.  
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/48aefdf7-8f2f-4080-97e9-c25477f71248/Unit1_Section1.4-Assignment.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/48aefdf7-8f2f-4080-97e9-c25477f71248/Unit1_Section1.4-Assignment.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# ### Use addition in `print ()`   
# Use **`print()`** to show the results of multiple lines of output.  
#  

# ### Examples: Addition in variable assignments and in `print()`

# In[9]:


# [ ] review & run code for assigning variables & using addition
add_two = 34 + 16
first_name = "Alton"
greeting = "Happy Birthday " + first_name

print(add_two)
print(greeting)


# In[10]:


#  [ ] review & run code for Integer addition in variables and in a print function
int_sum = 6 + 7
print(int_sum)
print(11 + 15)
print()


# In[11]:


# string addition in variables and in print()function
hat_msg = "I do not wear " + "a hat"  
print(hat_msg)
print("at " + "dinner")


# ## Task 2 (multi-part): Create integer addition and string addition output

# In[14]:


# [ ] perform string addition in the variable named new_msg (add a string to "my favorite food is ")
new_msg = "My favorite food is" + " edible subtance"
print(new_msg)


# In[15]:


# [ ] perform Integer addition in the variable named new_msg (add 2 or more Integers)
new_sum =   0 + 1 + 1
print(new_sum)



# In[ ]:


# [ ] create and print a new string variable, new_msg_2, that concatenates new_msg + a literal string
new_msg_2 = new_msg + "literal string"
print(new_msg_2)


# ## Concept: Errors!
# Encountering and troubleshooting errors are fundamental parts of computer programming.
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7ab2739a-95e6-4399-9b84-19ac5698bbea/Unit1_Section1.4-TypeError.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7ab2739a-95e6-4399-9b84-19ac5698bbea/Unit1_Section1.4-TypeError.vtt","srclang":"en","kind":"subtitles","label":"english"}])

# ### Examples

# In[ ]:


# [ ] Review & run code
print("my number is " + "123") #string, represents a text character
print("my number is " + 123) #number, with numeric value 


# #### TypeError
# The line&nbsp; **`print("my number is " + 123)`** causes the **`TypeError`** message to appear.  
# >`TypeError: Can't convert 'int' object to str implicitly`  
# 
# When adding to the string&nbsp; `"my number is "`&nbsp; the compiler is experiencing another string, but finds a number ***`123`**.  
# 
# Python cannot convert the Integer &nbsp; `123`&nbsp; to a string without explicit instruction (in code). 
#   
# In other words, Python only allows combining *like types*.
# - **`str`** + **`str`**
# - **`int`** + **`int`**
# 

# 
# ## Task 3: Fix `TypeError` 
# - Review the code in the cells below and then run the code
# - Fix any errors and run until the code no longer shows errors

# In[2]:


# [ ] Review and run the code - then fix any Errors
total_cost = 3 + 45
print(total_cost)


# In[4]:


# [ ] Review and run the code - then fix any Errors
school_num = "123"
print("the street number of Central School is " + school_num)


# In[5]:


# [ ] Read and run the code - write a hypothesis for what you observe adding float + int
#  [ ] HYPOTHESIS: It will return float, int, 6.3

print(type(3.3))
print(type(3))
print(3.3 + 3)


# ## Concept: More Errors
# ### SyntaxError & NameError
# - **SyntaxError** - breaks code formatting rules of Python
# - **NameError** - object is not defined (can't be found)  
# 
# Python has a specific grammar that it follows that is referred to as **syntax**.  
# The print function syntax rules for output of a single string include: 
# - Parentheses **` ( ) `** containing a **string** follow **`print`** (SyntaxError)
# - Strings have **matching quotation marks** (SyntaxError)
# - `print` is lowercase and correctly spelled (NameError)
# 
# Failure to follow any of these rules results in a `SyntaxError` or `NameError` when the code is run.  

# ## SyntaxError
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/1a1cd6c0-793f-4bcb-a0a0-c9f95a302142/Unit1_Section1.4-SyntaxNameErrors.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/1a1cd6c0-793f-4bcb-a0a0-c9f95a302142/Unit1_Section1.4-SyntaxNameErrors.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# - Improperly formatted string (quotes don't match) that results in a SyntaxError

# ### Examples

# In[6]:


# [ ] Review and run the code for properly and improperly formatted print statement
print("Hi!")
## improper format - non matching quotes
print('I like the morning") 


# - Note the misspelling below, "`prin`", results in a NameError

# In[7]:


# [ ] Review and run the code 
prin('hi')


# - EOF = "end of file" found in code below
# - Python went to the end of the file looking for, but not finding, a closing parenthesis 

# In[8]:


# [ ] Review and run the code missing the closing parenthesis  
print("where are my socks?" 


# - In the code below: a parenthesis inside quotations will be seen a part of a string and not as a parenthesis

# In[9]:


# { ] Review and run the code 
print("my socks are in the wrong bin)" 


# ## Task 4: Fix Errors

# >**Tip**: explaining errors to a partner often reveals a solution (works even if explaining error to a pencil). 

# In[ ]:


# [ ] Repair the syntax error 
print("my socks do not match") 


# In[ ]:


# [ ] Repair the NameError  
print("my socks match now") 


# In[ ]:


# [ ] Repair the syntax error 
print("Save the notebook frequently")


# In[ ]:


# [ ] Repair the NameError 
student_name = "Alton"
print(student_name)


# In[11]:


# [ ] Repair the TypeError
total = "3"
print(total + " students are signed up for tutoring")


# A parenthesis inside quotations will be seen a part of a string and not as a parenthesis.

# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
