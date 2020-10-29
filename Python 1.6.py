#!/usr/bin/env python
# coding: utf-8

# # Section 1.6
# ## Input
# - **input() - gathering user input**  
# - print() formatting 
# - Quotes inside strings
# - Boolean string tests methods
# - String formatting methods
# - Formatting string input()
# - Boolean `in` keyword 
# 
# -----
# 
# ### Student will be able to
# - **Gather, store and use string `input()`**  
# - Format `print()` output
# - Test string characteristics
# - Format string output
# - Search for a string in a string

# ## Concept: Get Information from Users with `input()`  
# The **`input()`** function prompts the user to supply data returning that data as a string.
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7a8881cb-0bdd-493c-b1a1-9849a95d05e6/Unit1_Section2-1-input-basic.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7a8881cb-0bdd-493c-b1a1-9849a95d05e6/Unit1_Section2-1-input-basic.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 

# ### Examples

# In[ ]:


# review and run code - enter a small integer in the text box
print("enter a small int: ")
small_int = input()
print("small int: ")
print(small_int)


# ## Task 1: Storing input in a variable
# - **[ ]** Create code to store input in student_name variable  
# An input box should when run:
# - **[ ]** type a name in the input box and press **Enter**
# - **[ ]** determine the **`type()`** of **student_name**

# In[2]:


# [ ] get input for the variable student_name
student_name = input("What is your name?")
# [ ] determine the type of student_name
type(student_name)


# ### Task 1 continued...
# > **Note**: **`input()`** returns a string (type = str) regardless of entry
# - If a string is entered **`input()`** returns a string
# - If a number is entered **`input()`** returns a string  
#   
# - **[ ]** Determine the **`type()`**  of input below by entering
#   - A name
#   - An integer (whole number no decimal)
#   - A float number with a decimal point

# In[5]:


# [ ] run cell several times, entering a name, an integer number, and a float number after adding code below
print("enter a name or number")
test_input = input()
# [ ] insert code below to check the type of test_input
type(test_input)


# ## Concept: User Prompts using `input()`
# 
# The **`input()`** function has an optional string argument which displays the string intended to inform a user what to enter  
# **`input()`** works similar to **`print()`**&nbsp;in the way it displays arguments as output.
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c607aa57-b18b-4f29-a317-7b13db66d8e8/Unit1_Section2-1-input-prompt.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c607aa57-b18b-4f29-a317-7b13db66d8e8/Unit1_Section2-1-input-prompt.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 

# ### Examples

# In[ ]:


student_name = input("enter the student name: ")  
print("Hi " + student_name)


# ## Task 2: Prompting the user for input
# - **[ ]** create a variable named **city** to store input, add a prompt for the name of a city
# - **[ ]** print "the city name is " followed by the value stored in **city**

# In[6]:


# [ ] get user input for a city name in the variable named city
city = input("What is the name of the city? ")
# [ ] print the city name
print(city)


# ### Task 2 continued 
# ## Multiple prompts for user input
# Often programs need information on multiple items.
# - **[ ]** create variables to store input: **name**, **age**, **get_mail**
# - **[ ]** create prompts for name, age and yes/no to being on an email list
# - **[ ]** print description + input values   
# 
# >Example print output:  
# `name = Alton`  
# `age =  17`  
# `wants email = yes`  
#   
# **Tip:** With multiple input statements, after each prompt, **click 'in' the input box** to continue entering input. 

# In[7]:


# [ ]create variables to store input: name, age, get_mail with prompts
# for name, age and yes/no to being on an email list
name = input("Name?")
age = input("Age?")
get_mail = input("Mail? Yes/No")
# [ ] print a description + variable value for each variable
print("Name:")
print(name)
print("Age:")
print(age)
print("On Mailing List?")
print(get_mail)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
