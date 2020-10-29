#!/usr/bin/env python
# coding: utf-8

# # Section 1.7
# ## Print Formatting
# - input() - gathering user input  
# - **print() formatting**  
# - Quotes inside strings
# - Boolean string tests methods
# - String formatting methods
# - Formatting string input()
# - Boolean `in` keyword 
# 
# -----
# 
# ### Students will be able to
# - Gather, store and use string `input()`  
# - **Format `print()` output**  
# - Test string characteristics
# - Format string output
# - Search for a string in a string

# ## Concept: Comma Print Formatting
# ### print() comma-separated strings 
# Python provides several methods of formatting strings in the **`print()`** function beyond **string addition**.   
#   
# **`print()`** provides using **commas** to combine strings for output.
# By comma-separating strings,  **`print()`** will output each separated by a space by default.
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ac97f001-e639-494e-aa15-e420efb5a7a8/Unit1_Section2-2-Print-Comma_Format.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ac97f001-e639-494e-aa15-e420efb5a7a8/Unit1_Section2-2-Print-Comma_Format.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# #### Comma formatted `print()`
# - **[ ]** Print 3 strings on the same line using commas inside the `print()` function 

# ### Examples

# In[1]:


# review and run code

name = "Collette"

# string addition 
print("Hello " + name + "!")

# comma separation formatting
print("Hello to",name,"who is from the city")


# ## Task 1
# **Print 3 strings on the same line using commas inside the print() function.**

# In[3]:


# [ ] print 3 strings on the same line using commas inside the print() function 
print("Scooby Dooby Doo","Where are you","We've got some work for you now.")


# ## Concept: Using Commas in `print()` with Strings and Numbers
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/46b436d7-31ed-4e9a-a4c9-55f9eaacfb84/Unit1_Section2-2-Print-String_Number.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/46b436d7-31ed-4e9a-a4c9-55f9eaacfb84/Unit1_Section2-2-Print-String_Number.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# - **`print()`** function formatting with comma separation works different than with string addition.
# - **`print()`**  using comma separation can mix numbers (int & float) and strings without a TypeError.
# 
# #### `print()` with numbers and strings together using commas
# - **[ ]** use a **`print()`** function with comma separation to combine 2 numbers and 2 strings

# ### Examples

# In[4]:


# review and run code
print("I will pick you up @",6,"for the party")


# In[5]:


# review and run code
number_errors = 0
print("An Integer of", 14, "combined with strings causes",number_errors,"TypeErrors in comma formatted print!")


# ## Task 2
# **Use a print() function with comma separation to combine 2 numbers and 2 strings**

# In[6]:


# [ ] use a print() function with comma separation to combine 2 numbers and 2 strings
print("number",6,123455,"eogidrosdjioufgn")


# ## Task 3  
# **print() comma separated mixing of strings and variables**  
# By comma-separating strings and/or string variables **`print()`** will output each separated by a space by default.
#   
# **Display text describing an address, made from strings and variables of different types**
# - Initialize variables with input()
#   - street
#   - st_number
# - Display a message about the street and street number using comma separation formatting

# In[8]:


# [ ] get user input for a street name in the variable, street
street = input("Street?")
# [ ] get user input for a street number in the variable, st_number
st_number = input("Number?")
# [ ] display a message about the street and st_number
print("You live at",st_number,street)


# ## Task 4
# **`print()` number, strings, variables from input**
# - [ ] Display text made from combining a variable, a literal string and a number

# In[9]:


# [ ] define a variable with a string or numeric value
newVar = "Variable"
# [ ] display a message combining the variable, 1 or more literal strings and a number
print(newVar,"literal string",24)


# ## Task 5 (Program): How many for the training?
# Create a program that prints out a reservation for a training class. Gather the name of the party, the number attending and the time.
# >**Example** of what input/output might look like:
# ```
# Enter name for contact person for training group: Hiroto Yamaguchi  
# Enter the total number attending the course: 7  
# Enter the training time selected: 3:25 PM  
# ------------------------------  
# Reminder: Training is scheduled at 3:25 PM for the Hiroto Yamaguchi group of 7 attendees.  
# Please arrive 10 minutes early for the first class.  
# ```  
#   
# Design and create your own reminder style.  
# - **[ ]** Get user input for variables.
#   - **owner**: name of person the reservation is for  
#   - **num_people**: how many are attending  
#   - **training_time**: class time
# - **[ ]** Create an integer variable **min_early**: number of minutes early the party should arrive.
# - **[ ]** Using comma separation, print reminder text.
#   - Use all of the variables in the text
#   - Use additional strings as needed
#   - Use multiple print statements to format message on multiple lines (optional)

# In[1]:


# [ ] get input for variables: owner, num_people, training_time  - use descriptive prompt text
owner = input("Who is the owner of the reservation?")
num_people = input("How many people are attending?")
training_time = input("How long will the class be?")
# [ ] create an integer variable min_early and "hard code" the integer value (e.g. - 5, 10 or 15)
min_early = 10
# [ ] print reminder text using all variables & add additional strings -  use comma separated print formatting
print(owner,"and the",num_people,"people accompanying, you should arrive",min_early,"minutes before the",training_time,"class starts.")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
