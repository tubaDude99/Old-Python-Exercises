#!/usr/bin/env python
# coding: utf-8

# # Section 4.4
# ## `while()` Boolean Loops
# - While `True`  or forever loops
# - Incrementing in loops
# - **Boolean operators in while loops**
# 
# ### Student will be able to
# - Create forever loops using `while` and `break`
# - Use incrementing variables in a while loop
# - **Control while loops using Boolean operators**

# ## Concept: `while` with Boolean Comparison
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/f540955e-543b-48f0-8201-3513b0beeed9/Unit1_Section7.2-while-boolean-comp.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/f540955e-543b-48f0-8201-3513b0beeed9/Unit1_Section7.2-while-boolean-comp.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### `while`  with Boolean comparison operator
# #### `while x < 5:`
# With increment we use **`break`** when count becomes greater than some number.
# 
# The same result can be achieved by using **`while x < 5:`**.

# ### Examples
#   
# 

# In[2]:


# review and run GREET COUNT
greet_count = 5

# loop while count is greater than 0
while greet_count > 0:
    print(greet_count, "!")
    greet_count -= 1
print("\nIGNITION!")


# ## Task 1: `while` with comparison operator 
# ### Program: Animal Names
# - Use **`while`** to get the user input, animal_name, of 4 animals 
#   - Use a counter, num_animals, in the while loop condition
#   - Append the names to a string variable, all_animals
#   - User can exit early by typing "exit" (check if animal_name is "exit" and break)
# - When the loop finishes, print the names of all_animals
# 
# - Bonus: print "no animals" if animal_name is empty after exiting the loop
# 
# **Tip:** Think about Sequence and variables that need to be initialized before the while loop

# In[8]:


# [ ] Create the Animal Names program, run tests
animals = ""
i = 0
while i < 4:
    animal = input()
    if animal == "exit":
        break
    else:
        animals = animals + animal + " "
    i += 1
print(animals)


# ## Concept: `while` with Boolean String Tests
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/26728191-873d-42ba-b6b5-48b396a8f42f/Unit1_Section7.2-while-boolean-string.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/26728191-873d-42ba-b6b5-48b396a8f42f/Unit1_Section7.2-while-boolean-string.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Using `while` with a Boolean String Tests
# A while loop can be controlled by Boolean strings such as `while name.isalpha() == False:`

# ### Example

# In[9]:


# review and run example that loops until a valid first name format is entered
student_fname = ""
while student_fname.isalpha() == False:
    student_fname = input("enter student\'s first (Letters only, No spaces): ")
print("\n" + student_fname.title(),"has been entered as first name")


# ## Task 2: Using `while` with a Boolean String
# ### Program: Long Number
# #### Create variables
# - **`int_num`** and get user input **string** of only digits  
# - **`long_num`** and initialize it as an empty string  
# 
# #### Create a while loop that runs as long as the input is all digits  
# 
# #### Inside the while loop   
# - Add **`int_num`** to the end of **`long_num`**
# - Get user input for **`int_num`** again (*inside while loop this time*)  
# 
# #### After the loop exits 
# - Print the value of **`long_num`**   

# In[1]:


# [ ] Create the program, run tests
intNum = input("Enter only digits: ")
longNum = ""
while intNum.isdigit():
    longNum = longNum + intNum
    intNum = input("Enter only digits: ")
print(longNum)


# ## Task 3: Fix the Errors
# This loop never runs.
# ### This is a logic error - there is no ErrorMessage, but the code *doesn't work*

# In[3]:


# [ ] review the code, run, fix the Logic error
count = 1

# loop 5 times
while count < 6:
    print(count, "x", count, "=", count*count)
    count +=1
    


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
