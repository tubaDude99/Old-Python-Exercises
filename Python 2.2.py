#!/usr/bin/env python
# coding: utf-8

# # Section 2.2
# ## Function Return and Multi-Parameters
# - Creating a simple function with a parameter
# - **Exploring functions with `return` values**  
# - **Creating functions with multiple parameters**  
# - Sequence in Python  
# 
# -----
# 
# ### Student will be able to
# - Create functions with a parameter  
# - **Create functions with a `return` value**
# - **Create functions with multiple parameters**
# - Use knowledge of sequence in coding tasks 
# - Use coding best practices 

# ## Concept: Functions with Return Values
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/db990568-d940-4ede-a063-7e40ed25c978/Unit1_Section3.2-function-return.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/db990568-d940-4ede-a063-7e40ed25c978/Unit1_Section3.2-function-return.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# - **`type()`** returns an object type.
# -  **`type()`** can be called with a float the return value can be stored in a variable.
# ```python
# object_type = type(2.33)
# ```  
# 
# ## Creating a function with a return value  
# - **`return`** keyword in a function *returns* a value after *exiting* the function.  
# 
# ```python
# def msg_double(phrase):
#       double = phrase + " " + phrase
#       return double
# ```  
# 

# ### Example 
#   
# Review and run the code.

# In[1]:


# Message double returns the string Argument doubled
def msg_double(phrase):
      double = phrase + " " + phrase
      return double

# save return value in variable
msg_2x = msg_double("let's go")
print(msg_2x)


# In[2]:


# example of functions with return values used in functions
def msg_double(phrase):
      double = phrase + " " + phrase
      return double

# prints the returned object
print(msg_double("Save Now!"))

# echo the type of the returned object
type(msg_double("Save Now!"))


# ## Task 1: A function that adds the "Doctor" title to a name
# - Define function `make_doctor()`&nbsp; that takes a parameter `name`
# - Get user **input** for variable **`full_name`**
# - Call the function using `full_name` &nbsp; as argument
# - Print the return value

# In[5]:


# create and call make_doctor() with full_name argument from user input - then print the return value
def make_doctor(full_name):
    return("Dr. "+full_name)
print(make_doctor("Richard Williams"))


# ## Concept: Functions with Multiple Parameters
# Functions can have multiple parameters separated by commas.
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/d82c3856-61ff-4fa3-9a20-df8f6ea4dd7a/Unit1_Section3.2-MultiParam_Function.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/d82c3856-61ff-4fa3-9a20-df8f6ea4dd7a/Unit1_Section3.2-MultiParam_Function.vtt","srclang":"en","kind":"subtitles","label":"english"}])

# ### Example
#   
# Review and run the code.

# In[6]:


def make_schedule(period1, period2):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title())
    return schedule

student_schedule = make_schedule("mathematics", "history")
print("SCHEDULE:", student_schedule)


# ## Task 2: Define `make_schedule()` and add a 3rd period 
# - Start with the above example code
# - Add a parameter period_3
# - Update function code to add period_3 to the schedule
# - Call **`student_schedule()`** with an additional argument such as 'science'
# - Print the schedule

# In[8]:


# [ ] add a 3rd period parameter to make_schedule
# [ ] Optional - print a schedule for 6 classes (Tip: perhaps let the function make this easy)
def make_schedule(period1, period2, period3):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title() + ", [3rd] " + period3.title())
    return schedule
make_schedule("math","english","economics")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
