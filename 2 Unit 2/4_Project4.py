#!/usr/bin/env python
# coding: utf-8

# 
# #  Module 4 Project  
# 
# Course 40461: Introduction to Python, Unit 2
# 
# This is an activity based on the Module 4 Lab, which you may have already completed.
# 
# | **Assignment Requirements** |  
# |:-------------------------------|  
# | **NOTE:** This program requires **`print`** output and code syntax used in Module 4 such as variable assignment, **`input`**, **`while`**, **`open`** keywords,  **`.split()`**, **`.readline()`**, **`.seek()`**, **`.write()`**, **`.close()`** methods.  |  
# 
# ## The Weather
# #### Create a program that:  
# - Imports and opens a file  
# - Appends additional data to a file  
# - Reads from the file to displays each city name and month average high temperature in Celsius  
# 
# **Output:** The output should resemble the following
# ```
# City of Beijing month ave: highest high is 30.9 Celsius
# City of Cairo month ave: highest high is 34.7 Celsius
# City of London month ave: highest high is 23.5 Celsius
# City of Nairobi month ave: highest high is 26.3 Celsius
# City of New York City month ave: highest high is 28.9 Celsius
# City of Sydney month ave: highest high is 26.5 Celsius
# City of Tokyo month ave: highest high is 30.8 Celsius
# City of Rio De Janeiro month ave: highest high is 30.0 Celsius
# ```  
# All of the above text output is generated from the file.
# Only these strings are *hard coded*:  
# - "is"  
# - "of"  
# - "Celsius"  
# 
# 
# 
# ### Import the file into the Jupyter Notebook environment   
# - Use `!curl` to download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv as `mean_temp.txt`  
#   
# 
# ```python
# # [ ] The Weather: import world_mean_team.csv as mean_temp.txt into the Jupyter notebook
# 
# 
# ```  
# 
# #### Add the weather for Rio  
# 1. Open the file in append plus mode (**`'a+'`**)  
# 2. Write a new line for Rio de Janeiro `"\nRio de Janeiro,Brazil,30.0,18.0"`  
# 
# 
# #### Grab the column headings  
# 1. Use .seek() to move the pointer to the beginning of the file  
# 2. Read the first line of text into a variable called: `headings`     
# 3. Convert `headings` to a list using **`.split(',')`** which splits on each comma  
# 
# 
# ```python
# # [ ] The Weather: open file, read/print first line, convert line to list (splitting on comma)
# 
# 
# ```
# 
# #### Read the remaining lines from the file using a while loop
#   1. Assign remaining lines to a **`city_temp`** variable  
#   2. Convert the city_temp to a list using **`.split(',')`** for each **`.readline()`** in the loop  
#   3. Print each city & the highest monthly average temperature   
#   4. Close mean_temps
# 
# >Tips & Hints:   
# - Print **`headings`** to determine indexes to use for the final output (what is in headings[0], [1], [2]..?)  
# - The city_temp data follows the order of the headings (city_temp[0] is described by headings[0]) 
# - The output should look like: **`"month ave: highest high" for Beijing is 30.9 Celsius`**  
# - Convert `city_temp` to lists with `.split(',')`  
# 
# 
# ```python
# # [ ] The Weather: use while loop to print city and highest monthly average temp in celsius
# 
# 
# ```
# 
# 
# 

# In[14]:


# [] create The Weather
get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o meanTemp.txt')
meanTemp = open('meanTemp.txt', 'a+')
meanTemp.write("Rio de Janeiro,Brazil,30.0,18.0\n")
meanTemp.seek(0)
headings = meanTemp.readline().split(',')
cityTemp = meanTemp.readlines()
print('\n' + headings[0] + '\t' + headings[1] + '\t\t' + headings[2] + '\t\t' + headings[3].strip('\n'))
for x in cityTemp:
    x = x.split(',')
    print('The average high in', x[0], 'was', x[2])
    


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
