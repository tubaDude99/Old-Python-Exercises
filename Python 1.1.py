#!/usr/bin/env python
# coding: utf-8

# # Section 1.1
# ##  Getting Started with Python in Jupyter Notebooks
# - **Python 3 in Jupyter notebooks**
# - **`print()`**
# - **Comments** 
# - Data types basics
# - Variables
# - Addition with Strings and Integers 
# - Errors
# - Character art  
# 
# -----
# 
# ### Students will be able to
# - **Use Python 3 in Jupyter notebooks**  
# - **Write working code using `print()` and `#` comments**  
# - Combine Strings using string addition (`+`)
# - Add numbers in code (`+`) 
# - Troubleshoot errors
# - Create character art

# ## Concept: Hello World! - Python `print()` Statement
# Using code to write "Hello World!" on the screen is the traditional first program when learning a new language in computer science.
# 
# Python has a very simple implementation: 
# ```Python
# print("Hello World!")
# ```  

# ## "Hello World!" 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/6f5784c6-eece-4dfe-a14e-9dcf6ee81a7f/Unit1_Section1.1-Hello_World.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/6f5784c6-eece-4dfe-a14e-9dcf6ee81a7f/Unit1_Section1.1-Hello_World.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# Our "Hello World!" program worked because this notebook hosts a Python interpreter that can run Python code cells.   
# 
# Try showing:
# ```Python 
# "Hello programmer!" 
# ``` 
# Enter new text inside the quotations in the cell above. Click on the cell to edit the code. 
# 
# What happens if any part of &nbsp;`print`&nbsp; is capitalized or what happens there are no quotation marks around the greeting?
# ## Methods for running the code in a cell
# 1. **Click in the cell below** and **press "Ctrl+Enter"** to run the code.  
# 2. **Click in the cell below** and **press "Shift+Enter"** to run the code and move to the next cell.  
# 3. **Menu: Cell**...  
#   a. **> Run Cells** runs the highlighted cell(s).  
#   b. **> Run All Above** runs the highlighted cell and above.  
#   c. **> Run All Below** runs the highlighted cell and below. 

# ### Example

# In[1]:


# [ ] Review the code, run the code

print("Hello World")


# ## Concept: Comments
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/34e2afb1-d07a-44ca-8860-bba1a5476caa/Unit1_Section1.1-Comments.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/34e2afb1-d07a-44ca-8860-bba1a5476caa/Unit1_Section1.1-Comments.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# When coding, programmers include comments for explanation of how code works for reminders and to help others who encounter the code.
# ### Comments start with the  `#`  symbol

# ### Example

# In[2]:


# This is how a comment looks in Python code
# Every comment line starts with the # symbol


# ## Task 1: Program: "Hello World!" with comment
# - Add a comment describing the code purpose
# - Create an original "Hello World" style message

# In[3]:


# An introduction
print("Greetings Human")


# ## Concept: Notebooks and Libraries
# Jupyter Notebooks provide a balance of jotting down important summary information along with proving a live code development environment where we can write and run Python code.  This course uses cloud hosted Jupyter [Notebooks](https://notebooks.azure.com) on Microsoft Azure and we will walk through the basics and some best practices for notebook use.  
# 
# ### Add a notebook library
# - New: https://notebooks.azure.com/library > New Library
# - Link: from a shared Azure Notebook library link > open link, sign in> clone and Run
# - Add: open library > Add Notebooks > from computer > navigate to file(s)
# 
# ### Work in notebook cells  
# - **Markdown cells** display text in a web page format. Markdown is code that formats the way the cell displays (*this cell is Markdown*).
# &nbsp;  
# - **Code cells** contain Python code and can be interpreted and run from a cell. Code cells display code and output.  
# &nbsp;  
# - **In edit** or **previously run:** cells can display in editing mode or cells can display results of *code* having been run. 
#   
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/6b9134fc-c7d7-4d25-b0a7-bdb79d3e1a5b/Unit1_Section1.1-EditRunSave.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/6b9134fc-c7d7-4d25-b0a7-bdb79d3e1a5b/Unit1_Section1.1-EditRunSave.vtt","srclang":"en","kind":"subtitles","label":"english"}])
#  
# ### Edit mode  
# - **Text** cells in editing mode show markdown code.
# - Markdown cells keep editing mode appearance until the cell is run.
# - **Code** (Python 3) cells in editing look the same after editing, but may show different run output.
# - Clicking another cell moves the green highlight that indicates which cell has active editing focus. 
#   
# ### Cells need to be saved
# - The notebook will frequently autosave.
# - **Best practice** is to manually save after editing a cell using **"Ctrl + S"** or alternatively, **Menu: File > Save and Checkpoint**.
# 

# ## Concept: Altering Notebook Structure
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/cb195105-eee8-4068-9007-64b2392cd9ff/Unit1_Section1.1-Language_Cells.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/cb195105-eee8-4068-9007-64b2392cd9ff/Unit1_Section1.1-Language_Cells.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Add a cell
# - Highlight any cell and then... add a new cell using **Menu: Insert > Insert Cell Below** or **Insert Cell Above**.
# - Add with Keyboard Shortcut: **"ESC + A"** to insert above or **"ESC + B"** to insert below.
# 
# ### Choose cell type
# - Format cells as Markdown or Code via the toolbar dropdown or **Menu: Cell > Cell Type > Code** or **Markdown**. 
# - Cells default to Code when created but can be reformatted from Code to Markdown and vice versa.  
# 
# ### Change notebook page language
# - The course uses Python 3 but Jupyter Notebooks can be in Python 2 or 3 (and a language called R).
# - To change a notebook to Python 3 go to **"Menu: Kernel > Change Kernel> Python 3"**.
# 

# ## Task 2: Insert a new cell
# -  Insert a new Code cell below with a comment describing the task.
# -  Edit the cell: add print() with the message "after edit, save!"
# -  Run the cell.

# In[4]:


# A reminder
print("after edit, save!")


# ### Insert another new cell
# - Insert a new Code cell below.
# - Edit the cell: add print() with the message showing the keyboard Shortcut to save **Ctrl + S**.
# - Run the cell.

# In[5]:


print("Ctrl + S")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
