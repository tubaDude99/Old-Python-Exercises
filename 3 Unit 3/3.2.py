#!/usr/bin/env python
# coding: utf-8

# # Section 3.2: Files
# * os.remove, os.unlink
# * os.path.exists, os.path.isdir, os.path.isfile
# * `with`
# 
# ### Students will be able to:
# * Delete files
# * Check that a file exists
# * Check if a path is a file or directory
# * Handle file exceptions
# * Use `with` statement close an open file after catching an exception

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# ## Deleting Files
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/1d72623a-7acc-41d3-a6cd-24ccad5f8524/DEV330x-3_2a_delete_files.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/20ac0aa5-5767-44b6-9291-f3d8beb0877f/DEV330x-3_2a_delete_files.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# In module 1 you explored the `os` module and used some of its methods to interact with the file system. You changed the working directory, listed the content of a path, created new directories, removed directories, and renamed files and directories. In addition to these utilities, Python's `os` module allows you to remove specific files using the `os.remove(path)` or `os.unlink(path)` functions. Both functions are semantically identical; however, their functionality slightly differs depending on the platform running your program. For now, we will consider them equivalent and use `os.remove(path)` to delete a file.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Removing a file

# In[1]:


import os

# Create a file to be deleted
file_path = "parent_dir/tmp_file_to_be_deleted.txt"
f = open(file_path, 'w')
f.close()

# list the content of parent_dir
print('Content of "parent_dir" after creating the file:')
print(os.listdir("parent_dir"))
print()

# delete the file
os.remove(file_path)

# list the content of parent_dir
print('Content of "parent_dir" after removing the file')
print(os.listdir("parent_dir"))


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>

# ## Setting Up the Environment (no coding required)
# This code segment creates a directory named `files_exercises` that contains five subdirectories named `dir_1`, `dir_2`, ...`dir_5` and 100 text files named sequentially from 0 to 99. The first line of each text file is a random number from 1000 to 9999.

# In[9]:


# Do not modify or add anything to this code segment.
# This code segment must be run before attempting any of the tasks in this lesson.
# It prepares the directories and files necessary to complete the tasks.

import os, random, shutil

# Navigate to `parent_dir` directory (if not already in it)
current_path = os.getcwd()
if ("parent_dir" in current_path):
    nb_path = current_path.split("parent_dir")[0]
else:
    nb_path = current_path
print("Changing working dir to parent_dir")
os.chdir(os.path.join(nb_path,'parent_dir'))
print("Current working directory:", os.getcwd())

# Remove the `files_exercises` directory (if it exists)
if('files_exercises' in os.listdir()):
    print('Removing "files_exercises"')
    shutil.rmtree('files_exercises')
    
# Create a new directory called `files_exercises`
print('Making "files_exercises"')
os.mkdir('files_exercises')

# Change the working directory to `files_exercises`
print('Changing working directory to "files_exercises"')
os.chdir('files_exercises')

# Display the current working directory to verify you are in the correct location
print("Current working directory:", os.getcwd())

# Create 100 text files, the first line of each file is a random number in the range [1000, 9999]
print("Creating 100 text files")
random.seed(25000) # to get the same random numbers every time the setup runs
for i in range(100):
    file_name = str(i) + ".txt"
    f = open(file_name, 'w')
    f.write(str(random.randint(1000, 9999)))
    f.close()

# Create 5 directories
print("Creating 5 directories")
for i in range(1, 6):
    os.mkdir("dir_"+str(i))

print("Environment setup completed!")


# ## Deleting Files

# In[14]:


# [ ] Complete the following program to delete the first 10 files inside `files_exercises` (0.txt, 1.txt ... 9.txt)
# Make sure the to run the environment setup code before running your own program.

import os

if ('files_exercises' not in os.getcwd()):
    print("STOP!!!! Run the environment setup code!")

# list the content of `files_exercises`
print('Content of "files_exercises" before removing the files')
print(os.listdir()) 

#TODO: delete the first 10 files
for x in range(10):
    print('Removing %i.txt'%x)
    os.remove(str(x) + '.txt')
# list the content of `files_exercises`
print('Content of "files_exercises" after removing the files')
print(os.listdir()) 


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Checking File Existence
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/027dbcb7-2896-4c4e-a08e-2049e8f1293a/DEV330x-3_2b_check_file_existenc.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/f75d3d91-4e4d-489b-9406-f81e5e9a05db/DEV330x-3_2b_check_file_existence.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# In the previous section, you deleted a file assuming that it exists and assuming it is actually a file. In reality, these assumptions are not always true and you should consider them when writing programs that deal with files.
# 
# #### Removing a file that doesn't exist
# Raises a `FileNotFoundError` exception. 
# 
# ```python
# # Removing a file that does not exist
# file_path = "parent_dir/fictitious_file.txt"
# os.remove(file_path)
# 
# -------------------------------------------------------------------------
# FileNotFoundError                       Traceback (most recent call last)
# <ipython-input-8-9e62af9a8388> in <module>()
#       1 # Removing a file that does not exist
#       2 file_path = "parent_dir/fictitious_file.txt"
# ----> 3 os.remove(file_path)
# 
# FileNotFoundError: [Errno 2] No such file or directory: 'parent_dir/fictitious_file.txt'
# ```
# 
# #### Removing a directory using `os.remove`
# When a directory is passed as an argument for `os.remove` a `PermissionError` is raised.
# 
# ```python
# # Passing a directory path to os.remove
# dir_path = "parent_dir"
# os.remove(dir_path)
# 
# -------------------------------------------------------------------------
# PermissionError                         Traceback (most recent call last)
# <ipython-input-9-698c1518adf7> in <module>()
#       1 # Passing a directory path to os.remove
#       2 dir_path = "parent_dir"
# ----> 3 os.remove(dir_path)
# 
# PermissionError: [Errno 1] Operation not permitted: 'parent_dir'
# ```
# 
# ### Simple solution
# In module 1 you were able to check if a path exists using `os.path.exists(path)`; in addition, you were able to figure out if a `path` is a file or directory using `os.path.isfile` and `os.path.isdir` respectively. You can use these functions to test a path and avoid the exceptions above.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 

# In[10]:


import os.path

file_path = "parent_dir/fictitious_file.txt"

# Removing a file

# Check if the path exists
if (os.path.exists(file_path)):
    if (os.path.isfile(file_path)):
        os.remove(file_path)
    else:
        print("Cannot remove a directory")
else:
    print("path does not exist")


# In[11]:


import os.path

file_path = "parent_dir"

# Removing a file

# Check if the path exists
if (os.path.exists(file_path)):
    if (os.path.isfile(file_path)):
        os.remove(file_path)
    else:
        print("Cannot remove a directory")
else:
    print("path does not exist")


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Checking File Existence
# 

# In[18]:


# [ ] Write a program to delete all the even numbered files inside `files_exercises`
# Make sure the to run the environment setup code before running your own program.

import os

if ('files_exercises' not in os.getcwd()):
    print("STOP!!!! Run the environment setup code!")

for x in range(0,100,2):
    x = str(x) + '.txt'
    try:
        os.remove(x)
    except:
        pass


# In[19]:


# [ ] Write a program to delete all the directories inside `files_exercises`
# Make sure the to run the environment setup code before running your own program.

import os

if ('files_exercises' not in os.getcwd()):
    print("STOP!!!! Run the environment setup code!")
for x in os.listdir():
    if os.path.isdir(x):
         os.rmdir(x)


# In[21]:


# [ ] Write a program to ask the user for a file number, 
# then delete the file if it exists or display an appropriate error message if it does not.
# Make sure the to run the environment setup code before running your own program.

# Test your program with the following:
# case 1: user inputs 84, 84.txt should be deleted
# case 2: user inputs 84 (again), a File does not exist message is printed
# case 3: user inputs 5, 5.txt should be deleted

import os

if ('files_exercises' not in os.getcwd()):
    print("STOP!!!! Run the environment setup code!")

i = input("Number:") + '.txt'
if os.path.exists(i):
    os.remove(i)
else:
    print("Noop")


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# ## Handling File Exceptions
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b520f3b2-cb14-4093-8308-30ff3bc63f86/DEV330x-3_2c_handling_file_excep.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/66061025-1730-40e2-b57b-28f7254de964/DEV330x-3_2c_handling_file_exceptions.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# In the previous example, you anticipated some errors and tried to avoid them by testing that a path exists and whether it is to a file or directory. However, you still assumed the results of these tests are static and won't change while your program is running. This assumption might lead to errors again. For example, say you test for the existence of a file and determine that the file exists at the given path, and right after that another program moves the file; if your program attempts to remove the file, it will raise a `FileNotFoundError` because the file no longer exists in that location. Of course, this is considered an unhandled exception and your program will stop executing and display the error message as before.
# 
# Python's philosophy in this case is to deal with these errors as exceptions and handle them using the techniques you saw in a previous lesson. This way, you can also deal with unexpected exceptions.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# In these examples we use exception handling to make sure that a file exists and that it is a file.

# In[22]:


import os.path

file_path = "parent_dir/fictitious_file.txt"

# Remove a file

try:
    os.remove(file_path)
except FileNotFoundError as exception_object:
    print("Cannot find file: ", exception_object)
except PermissionError as exception_object:
    print("Cannot delete a directory: ", exception_object)
except Exception as exception_object:
    print("Unexpected exception: ", exception_object)


# In[28]:


import os.path

file_path = "parent_dir"

# Remove a file

try:
    os.remove(file_path)
except FileNotFoundError as exception_object:
    print("Cannot find file: ", exception_object)
except PermissionError as exception_object:
    print("Cannot delete a directory: ", exception_object)
except Exception as exception_object:
    print("Unexpected exception: ", exception_object)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# 
# ## Handling File Exceptions
# 

# In[30]:


# [ ] Write a program to ask the user for a file number, 
# then delete the file if it exists or display an appropriate error message if it does not.
# Use file exception handling instead of file existence tests.
# Make sure to run the environment setup code before running your own program.

# Test your program with the following:
# Case 1: When the user inputs 84, the program should delete the file 84.txt
# Case 2: When the user inputs 84 (again), the program should print a File Not Found error message
# Case 3: When the user inputs 5, the program should delete the file 5.txt

import os

if ('files_exercises' not in os.getcwd()):
    print("STOP!!!! Run the environment setup code!")

i = input("Enter a file number to be deleted: ") + ".txt"
try:
    os.remove(i)
    print("Removing", i)
except FileNotFoundError as exception_object:
    print("Cannot find file: ", exception_object)
except PermissionError as exception_object:
    print("Cannot delete a directory: ", exception_object)
except Exception as exception_object:
    print("Unexpected exception: ", exception_object)


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## `with` Statements
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/0533563a-7174-4ca5-a0f1-fc1295503f71/DEV330x-3_2d_with_statement.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/a3973afc-8100-4554-a53a-8983e5cc1d11/DEV330x-3_2d_with_statement.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# After interacting with a file in Python, it is very important to close the file to ensure that all output is written properly and the resources are freed. Sometimes an exception is raised before reaching the `close()` statement, and the file is kept open. This issue can be resolved by placing the `close()` statement inside a `finally` clause. However, because the process of opening and closing a file is very common, Python provides a succinct `with` statement that performs the same task. The syntax of the `with` statement is:
# 
# ```python
# with open(FILE_NAME, MODE) as VARIABLE:
#     code block
# ```
# 

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Without a `with` statement
# In this example, you see that the file is still open after the `except` statement because `file.close()` is never reached.

# In[37]:


file_path = "parent_dir/text_file.txt"
try:
    file = open(file_path, 'r')
    x = int(file.readline()) # Raise an exception if lines are not numeric
    file.close() # Might never be reached if file.write raised an error
except Exception as exception_object:
    print("Unexpected exception:", exception_object)

print("File is closed?", file.closed)


# ### Using a `finally` statement
# The `finally` clause will close the file whether an exception was raised or not.

# In[38]:


file_path = "parent_dir/text_file.txt"

try:
    file = open(file_path, 'r')
    x = int(file.readline()) #raise an exception if lines are not numeric
except Exception as exception_object:
    print("Unexpected exception:", exception_object)
finally:
    file.close() # will be executed whether an exception was raised or not

print("File is closed?", file.closed)


# ### Using a `with` statement
# You need not explicitly close the file; the `with` statement will do it for you.

# In[39]:


file_path = "parent_dir/text_file.txt"

try:
    with open(file_path, 'r') as file:
        x = int(file.readline()) #raise an exception if lines are not numeric
except Exception as exception_object:
    print("Unexpected exception", exception_object)

print("File is closed?", file.closed)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4</B></font>
# 
# ## `with` Statements

# In[44]:


# [ ] Write a program to print the first line of every file inside `files_exercises`
# Use a `with` statement to open (and close) every file
# Make sure the to run the environment setup code before running your own program.


import os

if ('files_exercises' not in os.getcwd()):
    print("STOP!!!! Run the environment setup code!")
for x in os.listdir():
    try:
        with open(x, 'r') as f:
            print(x + ':', f.readline())
    except Exception as e:
        print(e)

