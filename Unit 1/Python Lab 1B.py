#!/usr/bin/env python
# coding: utf-8

# # Lab 1b
# ## Strings Practice: Input, Testing, and Formatting
# 
# -----
# 
# ### Student will be able to
# - Gather, store and use string `input()`  
# - Format `print()` output  
# - Test string characteristics  
# - Format string output  
# - Search for a string in a string  

# ## input()
# Getting input from users

# In[2]:


# [ ] get user input for a variable named remind_me
remind_me = input("What shall I remind thee of?")

# [ ] print the value of the variable remind_me
print(remind_me)


# In[3]:


# use string addition to print "remember: " before the remind_me input string
print("remember: " + remind_me)


# ### Program: Meeting Details
# #### [ ] Get user **input** for meeting subject and time
# `What is the meeting subject?: plan for graduation`  
# `What is the meeting time?: 3:00 PM on Monday`  
# 
# #### [ ] Print **output** with descriptive labels  
# `Meeting Subject: plan for graduation`  
# `Meeting Time:    3:00 PM on Monday`

# In[4]:


# [ ] get user input for 2 variables: meeting_subject and meeting_time
meeting_subject = input("What is the meeting subject?: ")
meeting_time = input("What is the meeting time?: ")
# [ ] use string addition to print meeting subject and time with labels
print("There will be a meeting on " + meeting_subject + " at " + meeting_time)


# ## print() formatting 
# ### Combining multiple strings separated by commas in the print() function

# In[5]:


# [ ] print the combined strings "Wednesday is" and "in the middle of the week" 
print("Wednesday is","in the middle of the week")


# In[6]:


# [ ] print combined string "Remember to" and the string variable remind_me from input above
print("Remember to", remind_me)


# In[7]:


# [ ] Combine 3 variables from above with multiple strings
print("String", remind_me, "Second string", meeting_time, meeting_subject, "last string")


# ### print() quotation marks

# In[8]:


# [ ] print a string sentence that will display an Apostrophe (')
print("It's time for Veggie Tales!")


# In[9]:


# [ ] print a string sentence that will display an Apostrophe (')
print("Timothy's computer is very slow")


# ## Boolean string tests

# ### Vehicle tests  
# #### Get user input for a variable named vehicle  
# Print the following test results:
# - Check True or False if vehicle is All alphabetical characters using .isalpha()  
# - Check True or False if vehicle is only All alphabetical & numeric characters  
# - Check True or False if vehicle is Capitalized (first letter only)  
# - Check True or False if vehicle is All lowercase  
# - **Bonus:** Print description for each test (e.g.- `"All Alpha: True"`)

# In[10]:


# [ ] complete vehicle tests 
print("vehicle".isalpha())
print("vehicle".isalnum())
print("vehicle".istitle())
print("vehicle".islower())


# In[11]:


# [ ] print True or False if color starts with "b" 
print("color".startswith("b"))


# In[ ]:





# ## String formatting

# In[13]:


# [ ] print the string variable capital_this Capitalizing only the first letter
capitalize_this = "the TIME is Noon."
print(capitalize_this.capitalize())


# In[15]:


# print the string variable swap_this in swapped case
swap_this = "wHO writes LIKE tHIS?"
print(swap_this.swapcase())


# In[16]:


# print the string variable whisper_this in all lowercase
whisper_this = "Can you hear me?"
print(whisper_this.lower())


# In[17]:


# print the string variable yell_this in all UPPERCASE
yell_this = "Can you hear me Now!?"
print(yell_this.upper())


# In[18]:


#format input using .upper(), .lower(), .swapcase, .capitalize()
format_input = input('enter a string to reformat: ')
print(format_input.upper())
print(format_input.lower())
print(format_input.swapcase())
print(format_input.capitalize())


# ### input() formatting

# In[19]:


# [ ] get user input for a variable named color
# [ ] modify color to be all lowercase and print
color = input("Color? ")
print(color.lower())


# In[20]:


# [ ] get user input using variable remind_me and format to all **lowercase** and print
# [ ] test using input with mixed upper and lower cases
remind_me = input("what shall remind ")
print(remind_me.lower())


# In[ ]:


# [] get user input for the variable yell_this and format as a "YELL" to ALL CAPS
yell_this = input("Yell? ").upper()


# In[ ]:





# ## "in" keyword
# ### Boolean: short_str in long_str

# In[21]:


# [ ] get user input for the name of some animals in the variable animals_input
animals_input = input("Animals? ")
# [ ] print true or false if 'cat' is in the string variable animals_input
print('cat' in animals_input)


# In[24]:


# [ ] get user input for color
color = input("What color? ")
# [ ] print True or False for starts with "b"
print(color.startswith("b"))
# [ ] print color variable value exactly as input 
#     test with input: "Blue", "BLUE", "bLUE"
print(color)


# ## Program: Guess what I'm reading
# ### short_str in long_str
# 
# 1. **[ ]** get user **`input`** for a single word describing something that can be read 
#  save in a variable called **can_read**  
#  e.g. - "website", "newspaper", "blog", "textbook"  
#  &nbsp;  
# 2. **[ ]** get user **`input`** for 3 things can be read  
#  save in a variable called **can_read_things**  
# &nbsp;  
# 
# 3. **[ ]** print **`true`** if the **can_read** string is found  
#  **in** the **can_read_things** string variable
#   
# *Example of program input and output*  
# [![01 02 practice Allergy-input](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/guess_reading.gif) ](https://1drv.ms/i/s!Am_KPRosgtaij7A_G6RtDlWZeYA3ZA)
# 

# In[26]:


# project: "guess what I'm reading"
# 1[ ] get 1 word input for can_read variable
can_read = input("What can be read? ")
# 2[ ] get 3 things input for can_read_things variable
can_read_things = input("What can be read? ")
# 3[ ] print True if can_read is in can_read_things
print(can_read in can_read_things)
# [] challenge: format the output to read "item found = True" (or false)
# hint: look print formatting exercises
print("item found =", can_read in can_read_things)


# ## Program: Allergy Check
# 
# 1. **[ ]** get user **`input`** for categories of food eaten in the last 24 hours  
#  save in a variable called **input_test**  
#  *Example input*
#  [![01 02 practice Allergy-input](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/eaten_input.gif) ](https://1drv.ms/i/s!Am_KPRosgtaij65qzFD5CGvv95-ijg)
# &nbsp;  
# 2. **[ ]** Print **`True`** if "dairy" is in the **input_test** string.  
# **[ ]** Test the code so far.  
# &nbsp;
# 3. **[ ]** Modify the print statement to output similar to below.  
# *Example output*
# [![01 02 Allergy output](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/eaten_output.gif) ](https://1drv.ms/i/s!Am_KPRosgtaij65rET-wmlpCdMX7CQ)  
# Test the code so far trying input including and without the string "dairy".  
# &nbsp;  
# 
# 4. **[ ]** Repeat the process checking the input for "nuts", **challenge** add "Seafood" and "chocolate".  
# **[ ]** Test your code  
# &nbsp;  
#   
# 5. **[ ] Challenge:** Make your code work for input regardless of case, e.g. - print **`True`** for "Nuts", "NuTs", "NUTS" or "nuts".  
# 

# In[28]:


# Allergy check 
# 1[ ] get input for test
input_test = input("enter some things eaten in the last 24 hrs: ").lower()
# 2/3[ ] print True if "dairy" is in the input or False if not
print("dairy".lower() in input_test)
# 4[ ] Check if "nuts" are in the input
print("nuts".lower() in input_test)
# 4+[ ] Challenge: Check if "seafood" is in the input
print("Seafood".lower() in input_test)
# 4+[ ] Challenge: Check if "chocolate" is in the input
print("chocolate".lower() in input_test)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
