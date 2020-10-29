#!/usr/bin/env python
# coding: utf-8

# # Section 1.4: File System
# * sys.platform
# * os: os.getcwd, os.chdir, os.listdir, os.mkdir, os.rmdir, os.rename
# * os.path: os.path.abspath, os.path.exists, os.path.isfile, os.path.isdir
# 
# ### Students will be able to:
# * Identify the platform running a Python script ('Linux', 'win32', 'Darwin')
# * Get the current working directory
# * Change the current working directory
# * List the content of the current working directory
# * Create a new directory
# * Remove a directory
# * Rename files and directories
# * Recognize the difference between relative and absolute paths
# * Test whether a path exists
# * Test whether a specific file or directory exists
# 

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Platform Identification
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/0ff85a85-7e41-4b56-9f8d-d9011225d54c/DEV330x-1_4a_platform.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/9d4fe926-4a98-4c1a-9dc4-77d66c648d86/DEV330x-1_4a_platform.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# In recent years, when you reach the download page of a website, you are directed to download a file that matches your operating system. For example, when using a Windows computer, download links direct you to .exe files; similarly, when using a Mac, you download links direct you to .dmg files. This code awareness makes the user experience more pleasant.
# 
# Python scripts can run on different platforms, including Windows, Mac, and Linux. The `sys` module provides access to several system variables, including the platform. If you know the platform your Python code is running on, you may be able to change the behavior of your application to accommodate that platform.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Identifying the platform

# In[1]:


import sys

print(sys.platform)


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Directory Operations
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/f27ecdae-1e25-49cd-9a86-8de1e9bb79b8/DEV330x-1_4b_directory_operation.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b1eac977-5006-4373-9466-223a5a4f42da/DEV330x-1_4b_directory_operations_modified.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# Most operating systems organize files in hierarchical structures. For example, directories (also known as folders) may contain other directories and files. The Python `os` module contains some useful functions to navigate and manipulate files and directories. In the following sections, you will see how to perform some basic directory operations.
# 
# #### Finding and changing the current working directory
# When navigating the hierarchical file system, you will always be located in a directory. The directory you're in is referred to as the "current working directory", or "cwd" for short. Python's `os.getcwd()` nethod returns a string containing the current working directory path.
# 
# The working directory can be changed in Python using `os.chdir(path)`, which changes the cwd into `path`, which is a string variable containing a path to the new working directory.
# 
# NOTE: When changing a working directory, you can specify `..` as your path. This effectively changes the working directory one level up into the parent directory.
# 
# #### Listing the content of a directory
# You might need to access or read the content of a directory. The `os.listdir()` method returns a list of the files and directories in the current working directory.
# 
# #### Creating and removing directories
# In Python, a new directory can be created manually using `os.mkdir(path)`, where `path` is the path and name of the new directory. Similarly, a directory can be removed using `os.rmdir(path)`, where `path` is the name of the directory to be deleted. Note that `rmdir` can delete only empty directories; if the directory specified by path is not empty, an error will be raised.
# 
# #### Renaming files and directories
# Many tasks can be automated by Python. For example, if you want to rename a large number of files to match a predefined pattern, you can use Python's `os.rename(src, dst)` method, in which `src` is a string containing the path of a source file or directory, and `dst` is a string containing the new (destination) path and/or name.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 

# ### Directory structure
# The examples in this lesson traverse through the following directory structure. 
# 
# parent_dir
#     
#     |__  child1_dir
#     |    |
#     |    |_ leaf1.txt
#     |
#     |__ child2_dir
#     |    |
#     |    |_ leaf2.txt
#     |
#     |__ parent_leaf.txt
#     |
#     |__ text_file.txt
# 
# #### Directories
# The directories in this structure are parent_dir, child1_dir, and child2_dir.
# 
# #### Files
# The files in this structure are leaf1.txt, leaf2.txt, parent_leaf.txt, and text_file.txt.

# ### Working directory
# In this example, you will change the current working directory to parent_dir, then to child1_dir, then back to parent_dir. You will also see a printout of the current working directory at every step.

# In[1]:


import os

# Change the current working directory to parent dir
os.chdir('..')
print('Changed working dir to parent: ', os.getcwd())

# Change the current working directory to child1 dir
os.chdir('child1_dir')
print('Changed working dir to child1: ', os.getcwd())

# Change the current working directory back to the parent dir
os.chdir('..')
print('Changed working dir back to parent: ', os.getcwd())


# ### Directory content
# In this example, you will list the content of the current working directory (parent_dir).

# In[8]:


import os

# Print the current working directory (should be "parent_dir")
print('The current working directory is:', os.getcwd())

# List the content of the directory (both files and other directories)
print('Current directory content: ', os.listdir())


# ### Creating and removing directories
# In this example, you will create and remove directories.

# In[6]:


import os

# Print the current working directory (should be "parent_dir")
print('The current working directory is:', os.getcwd())

# Create a new directory 
os.mkdir('new_child')
print('Created new_child dir')

# List the content of the directory
print('Current directory content: ', os.listdir())

# Remove the new child directory
os.rmdir('new_child')
print('Removed new_child dir')

# List the content of the directory
print('Current directory content: ', os.listdir())


# ### Renaming directories
# In this example, you will create a new directory, and then change its name.

# In[9]:


import os

# Print the current working directory (should be "parent_dir")
print('The current working directory is:', os.getcwd())

# Create a new directory 
os.mkdir('new_child')
print('Created new_child dir')

# List the content of the directory
print('Current directory content:', os.listdir())

# Rename new_child as old_child
os.rename('new_child', 'old_child')
print('Renamed new_child as old_child')
# List the content of the dir
print('Current directory content: ', os.listdir())

# Remove the old_child dir
os.rmdir('old_child')
print('Removed old_child dir')
print('Current directory content: ', os.listdir())


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Directory Operations
# 

# In[13]:


# [ ] Write a program to:
# 1) Prompt the user for a directory name
# 2) Create the directory
# 3) Verify the directory was created by listing the content of the current working directory
# 4) Remove the created directory
# 5) Verify the directory was removed by listing the content of the current working directory
import os
n = input()
os.mkdir(n)
print(os.listdir())
os.rmdir(n)
print(os.listdir())

# --Completed--
import os

# 1) Prompt the user for a directory name
dir_name = input("Enter a directory name: ")

# 2) Create the directory
print("Making", dir_name)
os.mkdir(dir_name)

# 3) Verify the directory was created by listing the content of the current working directory
print("Current directory content:", os.listdir())

# 4) Remove the created directory
print("Removing", dir_name)
os.rmdir(dir_name)

# 5) Verify the directory was removed by listing the content of the current working directory
print("Current directory content:", os.listdir())


# In[14]:


# [ ] Write a program to:
# 1) Create a directory called "my_dir"
# 2) Change the current working directory to "my_dir"
# 3) Verify you are in the correct directory by displaying the current working directory
# 4) Change the working directory back to the parent directory
# 5) Verify you are in the correct directory by displaying the current working directory
# 6) Rename "my_dir" to "your_dir"
# 7) Verify the directory was renamed by listing the content of the current working directory
# 8) Remove "your_dir"
# 9) Verify the directory was removed by listing the content of the current working directory
import os
os.mkdir('my_dir')
os.chdir('my_dir')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.rename('my_dir','your_dir')
print(os.listdir())
os.rmdir('your_dir')
print(os.listdir())
# --Completed--
import os

# 1) Create a directory called "my_dir"
print('Making "my_dir"')
os.mkdir("my_dir")

# 2) Change the current working directory to "my_dir"
print("Changing working directory")
os.chdir("my_dir")

# 3) Verify you are in the correct directory by displaying the current working directory
print("Current working directory:", os.getcwd())

# 4) Change the working directory back to the parent directory
print("Changing working directory")
os.chdir("..")

# 5) Verify you are in the correct directory by displaying the current working directory
print("Current working directory:", os.getcwd())

# 6) Rename "my_dir" to "your_dir"
print('Renaming "my_dir" to "your_dir"')
os.rename("my_dir", "your_dir")

# 7) Verify the directory was renamed by listing the content of the current working directory
print("Current directory content:", os.listdir())

# 8) Remove "your_dir"
print('Remove "your_dir"')
os.rmdir("your_dir")

# 9) Verify the directory was removed by listing the content of the current working directory
print("Current directory content:", os.listdir())


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Path Operations
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/a37e2766-ff8d-4588-89de-ca68296ed072/DEV330x-1_4c_path_operations.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/116a8c79-e90e-456c-abe9-eedcd5a9f44e/DEV330x-1_4c_path_operations.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# #### Relative and absolute paths
# A file or directory has a name and a path, which is just a roadmap to its specific location in the file system. Most operating systems, support two types of paths:
# * Relative paths: path to a file or directory from a specific location (or current working directory)
# * Absolute paths: path to a file or directory from a root. In UNIX flavors, a root is "/"; whereas, on Windows machines a root is "C:\"
# 
# For example, consider the UNIX directory structure we have been manipulating:
# 
#     /
#     |
#     |__ parent_dir
#         |
#         |__  child1_dir
#         |    |
#         |    |_ leaf1.txt
#         |
#         |__ child2_dir
#         |    |
#         |    |_ leaf2.txt
#         |
#         |__ parent_leaf.txt
#         |
#         |__ text_file.txt
#     
# If you are currently in parent_dir and trying to get to leaf1.txt, the relative path would be (child1_dir/leaf1.txt). It's a relative path because it is relative to your current location.
# 
# The absolute path to leaf1.txt is (/parent_dir/child1_dir/leaf1.txt), it starts from the root "/" all the way to the destination file. It's absolute because it starts from the absolute root.
# 
# In Python, you can use relative or absolute paths; however, it might be useful to convert a relative path into an absolute path using the function `os.path.abspath(path)`. The function returns a string containing the absolute path to a file or directory specified by the relative path passed as an argument.
# 
# ```python
# In [1]: import os.path
# In [2]: os.path.abspath('child1_dir/leaf1.txt')
# Out[2]: '/parent_dir/child1_dir/leaf1.txt'
# ```
# 
# #### Testing the existence of paths, files, and directories
# The module `os.path` contains common pathname manipulation functions. For example, `os.path.exists(path)` tests whether `path` (relative or absolute) exists in the file system, `os.path.isfile(path)` returns `True` if `path` (relative or absolute) refers to an existing file, and `os.path.isdir(path)` returns `True` if `path` refers to an existing directory. Other functions in the module allow you to get the size of a file, split and join path names regardless of the operating system, and so on. The Python Documentation site at https://docs.python.org/3/library/os.path.html has more information on the `os.path` module.
# 
# NOTE: In UNIX systems, paths are written using a forward slash (/) as separators; however, on Windows systems, paths are written using backslashes (\\) as separators. When joining path names, use `os.path.join` and Python will use the appropriate separator for the platform running the script.
# 

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# In this example, you will get the absolute path to a file and test whether the path exists and if it refers to a file or a directory.

# In[15]:


import os, os.path

# Print the current working directory (should be "parent_dir")
print('The current working directory is:', os.getcwd())

# Find the absolute path to child1_dir/leaf1.txt
abs_path = os.path.abspath('child1_dir/leaf1.txt')
print("Absolute path to leaf1.txt is: ", abs_path)

# Test whether the path exists
if(os.path.exists(abs_path)):
    print("Path exists")
    
    # Test to see if it's a file or directory
    if(os.path.isfile(abs_path)):
       print("It's a file")
    elif (os.path.isdir(abs_path)):
       print("It's a dir")
    
else:
    print("Path doesn't exist")


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Path Operations
# 

# In[16]:


# [ ] Write a program that prompts the user for a file or directory name 
# then prints a message verifying if it exists in the current working directory
import os.path
if os.path.exists(input()):
    print('It exists')
else:
    print('It doesn\' exist')
# --Completed--
import os.path

name = input("Enter a file or directory name: ")

if (os.path.exists(name)):
    print("The file or directory exists in the current working directory")
else:
    print("The file or directory does NOT exist in the current working directory")


# In[22]:


# [ ] Write a program to print the absolute path of all directories in "parent_dir"
# HINTS:
# 1) Verify you are inside "parent_dir" using os.getcwd()
# 2) Use os.listdir() to get a list of files and directories in "parent_dir"
# 3) Iterate over the elements of the list and print the absolute paths of all the directories
import os, os.path
for x in os.listdir():
    if os.path.isdir(x):
        print(os.path.abspath(x))
# --Completed--
import os, os.path

# 1) Verify you are inside "parent_dir" using os.getcwd()
# Print the current working directory (should be "parent_dir")
print('The current working directory is:', os.getcwd())

# 2) Use os.listdir() to get a list of files and directories in "parent_dir"
files_dir_lst = os.listdir()

# 3) Iterate over the elements of the list and print the absolute paths of all the directories
for element in files_dir_lst:
    if(os.path.isdir(element)):
        print(os.path.abspath(element))

