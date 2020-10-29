#!/usr/bin/env python
# coding: utf-8

# # Module 1 Required code  
#   
# 
# ## Note: Students of Dev330x on edX
# 
# > ### It is required to submit your required code for Module 1 within the edX course   
# > The completed code must be copied from the cell below and pasted in to the edX required code page at the end of Module 1 in the course "Introduction to Python: Creating Scalable, Robust, Interactive Code" on edX.  
# >  
# > **REQUIREMENTS**  
# > Submit all of the code in working order but you will only be graded on the the 2 functions below:
# - ### name_generator()
#   - **use the following required keywords & functions:** `datetime.today()`, `randint()`, `.strftime()`, `return`
# - ### directory_creator()
#   - **use the following:** Python `os` module

# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Required Code Module 1</B></font>   
# 
# 
# 
# ## Directory creator  
# 
# ### Complete the Required Code in the Jupyter Notebook Required_Code_Mod01 and then paste into edX code submission page   
# 
# This is the same code assignment located as the project at the bottom of 3-1.5_Mod01_Practice.ipynb

# In[ ]:


# [ ] The following program is designed to generate a number of directories.
# The directory names follow the pattern (MM_DD_YY_randnum), where:
#     - MM_DD_YY: is today's date as month/day/year
#     - randnum: is a random integer between 10000 and 50000
# For example, if today is May 12th, 2016, then the following would be valid names: 05_12_16_11050 or 05_12_16_15001
#
# For this task, you should complete the functions:
# 1) `directory_count()`
# 2) `name_generator()`
# 3) `directory_creator(name)`
# 4) `create()`
#
# HINT: You should import all necessary modules

import os

def directory_count():
    """
    Calculate the number of directories to be generated.
    
    I) Get the current minute using appropriate functionality from `datetime`
    II) Take the square root of ..the current minute + 15
    III) Round the square root to an integer
    VI) return the rounded number as the number of directories to be created
    
    args: 
          NONE
    
    returns: 
         `dir_count`: number of directories to be created 
    """
    #TODO

def name_generator():
    """
    Generate a single directory name using the pattern (MM_DD_YY_randnum).
    
    args:
         NONE
    
    returns:
         `dir_name`: string containing a valid directory name
    """
    #TODO

def directory_creator(name):
    """
    Create a single directory called `name` in the current working directory.
    
    args:
         name: directory to be created
    
    returns:
         NONE
    """
    #TODO

def create():
    """
    Generate the necessary directories.
    
    Use `directory_count` to calculate the number of directories, then use `directory_creator` and `name_generator`.

    args:
         NONE
    
    returns:
         NONE
    """
    #TODO

# Change working directory to `parent_dir` or `create`
if("parent_dir" not in os.getcwd()):
    if os.path.exists("./parent_dir"):
        print("Changing working dir to parent_dir")
        os.chdir("parent_dir")
    else:
        os.mkdir(os.getcwd() + "./parent_dir")
        print("Changing working dir to parent_dir")
        os.chdir("parent_dir")
else:
    # so the code can run multiple times 
    # while directory not ending with 'parent_dir' move up the path ..\
    while "parent_dir" not in os.getcwd()[-11:]:
        # move up in dir to find 'parent_dir'
        os.chdir("..")
        print("moved up", os.getcwd())
        
# print the current working directory (should be "parent_dir")
print("The current working directory is:", os.getcwd())

# check for randoms_directory if not present, create new
if os.path.exists(os.getcwd() + "/randoms_directory") != True:
    os.mkdir("randoms_directory")

# change the current working directory to randoms_directory
print("Changing working dir to randoms_directory")
os.chdir("randoms_directory")
# print the current working directory (should be "randoms_dir")
print("The current working directory is:", os.getcwd())

# create directories inside "randoms_directory"
create()
    
# list the content of the current directory
print("Current directory content:", os.listdir())


# --Completed--

import os
from random import randint
from datetime import datetime
from math import sqrt, floor

def directory_count():
    """
    Calculate the number of directories to be generated.
    
    I) Get the current minute using appropriate functionality from `datetime`
    II) Take the square root of ..the current minute + 15
    III) Round the square root to an integer
    VI) return the rounded number as the number of directories to be created
    
    args: 
          NONE
    
    returns: 
         `dir_count`: number of directories to be created 
    """
    now = datetime.today()
    minute = now.minute
    dir_count = floor(sqrt(minute + 15))
    return dir_count

def name_generator():
    """
    Generate a single directory name using the pattern (MM_DD_YY_randnum).
    
    args:
         NONE
    
    returns:
         `dir_name`: string containing a valid directory name
    """
    now = datetime.today()
    rand_num = randint(10000, 50000)
    formatted_date = now.strftime("%m_%d_%y")
    dir_name = formatted_date + "_" + str(rand_num)
    return dir_name

def directory_creator(name):
    """
    Create a single directory called `name` in the current working directory.
    
    args:
         name: directory to be created
    
    returns:
         NONE
    """
    os.mkdir(name)

def create():
    """
    Generate the necessary directories.
    
    Use `directory_count` to calculate the number of directories, then use `directory_creator` and `name_generator`.

    args:
         NONE
    
    returns:
         NONE
    """
    dir_count = directory_count()
    print("Creating", dir_count, "directories")
    for i in range(dir_count):
        directory_creator(name_generator())

# Change working directory to `parent_dir` or `create`
if("parent_dir" not in os.getcwd()):
    if os.path.exists("./parent_dir"):
        print("Changing working dir to parent_dir")
        os.chdir("parent_dir")
    else:
        os.mkdir(os.getcwd() + "./parent_dir")
        print("Changing working dir to parent_dir")
        os.chdir("parent_dir")
else:
    # so the code can run multiple times 
    # while directory not ending with 'parent_dir' move up the path ..\
    while "parent_dir" not in os.getcwd()[-11:]:
        # move up in dir to find 'parent_dir'
        os.chdir("..")
        print("moved up", os.getcwd())
        
# print the current working directory (should be "parent_dir")
print("The current working directory is:", os.getcwd())

# check for randoms_directory if not present, create new
if os.path.exists(os.getcwd() + "/randoms_directory") != True:
    os.mkdir("randoms_directory")

# change the current working directory to randoms_directory
print("Changing working dir to randoms_directory")
os.chdir("randoms_directory")
# print the current working directory (should be "randoms_dir")
print("The current working directory is:", os.getcwd())

# create directories inside "randoms_directory"
create()
    
# list the content of the current directory
print("Current directory content:", os.listdir())


# ### Test your code for the graded functions name_generator() & directory_creator()  
# Help ensure that required name_generator() & directory_creator() functions will earn credit when submitted to edX by running the code below after the functions have been loaded in this notebook.
# 
# Be sure to meet the following **requirements** for name_generator() & directory_creator() functions before submission to edX:  
# > 
# - ### name_generator()
#   - **use the following required keywords & functions:** `datetime.today()`, `randint()`, `.strftime()`, `return`
# - ### directory_creator()
#   - **use the following Python module:** `os` 

# In[ ]:


# Test your code for the graded functions name_generator() & directory_creator()
import os
import shutil

# make sure directory structure is in place
os.chdir("/home/nbuser/library")

if os.path.exists(os.getcwd() + "/parent_dir") != True:
    os.mkdir("parent_dir")
os.chdir("parent_dir")
    
    
if os.path.exists(os.getcwd() + "/randoms_directory") != True:
    os.mkdir("randoms_directory")
os.chdir("randoms_directory")
    
if os.path.exists(os.getcwd() + "/test_required") == True:
    # delete the test_required directory
    shutil.rmtree("/home/nbuser/library/parent_dir/randoms_directory/test_required")
# create and move to Test_required
os.mkdir("test_required")
os.chdir("test_required")

# print the current working directory (should be "parent_dir")
print("The current working directory is:", os.getcwd())
print("\nThe created directories should be named MM_DD_YY_randnum - such as '03_22_19_17040'")

# TEST*** test name_generator & directory_creator() by creating 3 directories ***TEST
for i in range(3):
    dir_name = name_generator()
    print("creating directory", dir_name)
    directory_creator(dir_name)


# list the content of the current directory
print("Current directory content:", os.listdir())

# Check if TEST created 3 directories
num_dir = len(os.listdir())

if num_dir == 3:
    print("\nPASS: Contains 3 directories as expected. Be sure name_generator() & directory_creator() contain required keywords and functions.")  
    print("Copy code cell above into edX required code submission.")
else:
    print("\nFAIL: Should contain 3 directories, contains", num_dir )


# In[ ]:




