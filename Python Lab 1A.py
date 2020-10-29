#!/usr/bin/env python
# coding: utf-8

# # Lab 1a
# ## Basics Practice: Notebooks, Comments, print(), type(), Addition, Errors and Art
# 
# ### Student will be able to
# - Use Python 3 in Jupyter notebooks
# - Write working code using `print()` and `#` comments  
# - Write working code using `type()` and variables
# - Combine Strings using string addition (+)
# - Add numbers in code (+)
# - Troubleshoot errors
# - Create character art  
# 
# >**Note:** The **[ ]** indicates student has a task to complete.
#   
# >**Reminder:** To run code and save changes: student should upload or clone a copy of notebooks. 
# 
# #### Notebook use
# - [ ] Insert a **code cell** below   
# - [ ] Enter the following Python code, including the comment: 
# ```Python 
# # [ ] print 'Hello!' and remember to save notebook!
# print('Hello!')
# ```
# Then run the code - the output should be:  
# `Hello!`

# In[1]:


# [ ] print 'Hello!' and remember to save notebook!
print('Hello!')


# #### Run the cell below   
# - [ ] Use **Ctrl + Enter**  
# - [ ] Use **Shift + Enter**    

# In[2]:


print('watch for the cat')


# #### Student's Notebook editing
# - [ ] Edit **this** notebook Markdown cell replacing the word "Student's" above with your name
# - [ ] Run the cell to display the formatted text
# - [ ] Run any 'markdown' cells that are in edit mode, so they are easier to read

# #### [ ] Convert \*this\* cell from markdown to a code cell, then run it  
# print('Run as a code cell')
# 

# ##  # Comments
# Create a code comment that identifies this notebook, containing your name and the date.

# In[ ]:


# Python Lab 1A, Nathan, 8/30/19


# #### Use print() to 
# - [ ] print [**your_name**]
# - [ ] print **is using Python!**

# In[3]:


# [ ] print your name
print("Nathan")
# [ ] print "is using Python"
print("is using Python")


# Output above should be:  
# `Your Name  
# is using Python!`  

# #### Use variables in print()
# - [ ] Create a variable **your_name** and assign it a string containing your name
# - [ ] Print **your_name**

# In[5]:


# [ ] create a variable your_name and assign it a string containing your name
your_name = "Nathan"
#[ ] print your_name
print(your_name)


# #### Create more string variables
# - **[ ]** Create variables as directed below
# - **[ ]** Print the variables

# In[8]:


# [ ] create variables and assign values for: favorite_song, shoe_size, lucky_number
favorite_song = "Positive Force"
shoe_size = 12
lucky_number = 22
# [ ] print the value of each variable favorite_song, shoe_size, and lucky_number
print(favorite_song)
print(shoe_size)
print(lucky_number)


# #### Use string addition
# - **[ ]**  Print the above string variables (favorite_song, shoe_size, lucky_number) combined with a description by using **string addition**
# >For example, favorite_song displayed as:  
# `favorite song is happy birthday`

# In[14]:


# [ ] print favorite_song with description
favorite_song = "Positive Force"
print("My favorite song is", favorite_song)
# [ ] print shoe_size with description
shoe_size = 12
print("My shoe size is", shoe_size)
# [ ] print lucky_number with description
lucky_number = 22
print("My lucky number is", lucky_number)


# ##### More string addition
# - **[ ]** Make a single string (sentence) in a variable called favorite_lucky_shoe using **string addition** with favorite_song, shoe_size, lucky_number variables and other strings as needed 
# - **[ ]** Print the value of the favorite_lucky_shoe variable string
# > Sample output:  
# `For singing happy birthday 8.5 times, you will be fined $25`

# In[15]:


# assign favorite_lucky_shoe using
favorite_song = "Positive Force"
shoe_size = 12
lucky_number = 22
favorite_lucky_shoe = str(shoe_size) + " CDs of the song " + favorite_song + "can be bought for $" + str(lucky_number)
print(favorite_lucky_shoe)


# ### print() art

# #### Use `print()` and the asterisk **\*** to create the following shapes:
# - [ ] Diagonal line  
# - [ ] Rectangle  
# - [ ] Smiley face

# In[21]:


# [ ] print a diagonal using "*"
print("*")
print("  *")
print("    *")
print("      *")
print("        *")
print("          *")
# [ ] rectangle using "*"
print()
print()
print("************")
print("*          *")
print("*          *")
print("*          *")
print("************")
# [ ] smiley using "*"
print()
print()
print("  *   *")
print()
print("*   *   *")
print(" *     *")
print("  *****")


# ### Using `type()`
# #### Calculate the *type* using `type()`

# In[24]:


# [ ] display the type of 'your name' (use single quotes)
type('your name')


# In[26]:


# [ ] display the type of "save your notebook!" (use double quotes)
type("save your notebook")


# In[27]:


# [ ] display the type of "25" (use quotes)
type("25")


# In[28]:


# [ ] display the type of "save your notebook " + 'your name'
type("save your notebook" + 'your name')


# In[29]:


# [ ] display the type of 25 (no quotes)
type(25)


# In[30]:


# [ ] display the type of 25 + 10 
type(25 + 10)


# In[31]:


# [ ] display the type of 1.55
type(1.55)


# In[32]:


# [ ] display the type of 1.55 + 25
type(1.55 + 25)


# #### Find the type of variables
# - **[ ]** Run the cell below to make the variables available to be used in other code
# - **[ ]** Display the data type as directed in the cells that follow

# In[2]:


# assignments ***RUN THIS CELL*** before starting the section



# In[3]:


# [ ] display the current type of the variable student_name
type(student_name)


# In[5]:


# [ ] display the type of student_age
type(student_age)


# In[6]:


# [ ] display the type of student_grade
type(student_grade)


# In[7]:


# [ ] display the type of student_age + student_grade
type(student_age + student_grade)


# In[8]:


# [ ] display the current type of student_id
type(student_id)


# In[9]:


# assign new value to student_id 
student_id = 4

# [ ] display the current of student_id
type(student_id)


# #### Number integer addition
# 
# - **[ ]** Create variables (x, y, z) with integer values

# In[10]:


# [ ] create integer variables (x, y, z) and assign them 1-3 digit integers (no decimals - no quotes)
x = 154
y = 25
z = 429


# - **[ ]** Insert a **code cell** below
# - **[ ]** Create an integer variable named **xyz_sum** equal to the sum of x, y, and z
# - **[ ]** Print the value of **xyz_sum** 

# In[11]:


xyz_sum = x+y+z
print(xyz_sum)


# ### Errors
# - **[ ]** Troubleshoot and fix the errors below

# In[14]:


# [ ] fix the error 

print("Hello World!")    



# In[ ]:


# [ ] fix the error 
print("strings have quotes and variables have names")


# In[16]:


# [ ] fix the error 
print("I have $" + "5")


# In[18]:


# [ ] fix the error 
print('always save the notebook')
      


# ## ASCII art
# - **[ ]** Display first name or initials as ASCII Art
# - **[ ]** Challenge: insert an additional code cell to make an ASCII picture

# In[24]:


# [ ] ASCII ART
print("|\   |")
print("| \  |")
print("|  \ |")
print("|   \|")


# In[29]:


# [ ] ASCII ART
print(" ____")
print("|    )")
print("|____/")
print("|    )")
print("|____/")


# In[1]:


print("____                  ____                  ____")
print("\_  \___             /    \             ___/  _/")
print(" \____  \___________| *  * |___________/  ____/ ")
print("  \_  \____________ |  \/  | ____________/  _/  ")
print("   \___             |      |             ___/   ")
print("    \_ \___________ |      | ___________/ _/    ")
print("     \______________/\____/\______________/     ")
print("                      /  \                      ")
print("                     /|\/|\                     ")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
