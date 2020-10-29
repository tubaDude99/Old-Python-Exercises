#!/usr/bin/env python
# coding: utf-8

# # Section 2.1
# ## Simple Functions
# - **Creating a simple function with a parameter**
# - Exploring functions with `return` values 
# - Creating functions with multiple parameters
# - Sequence in Python  
# 
# -----
# 
# ### Student will be able to
# - **Create functions with a parameter**  
# - Create functions with a `return` value 
# - Create functions with multiple parameters
# - Use knowledge of sequence in coding tasks  
# - Use coding best practices 

# ## Concept: Functions with Arguments
# Functions are used for code tasks that are intended to be reused. 
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/621d10f8-23d5-4571-b0fd-aa12b0de98d8/Unit1_Section3.1-function-arguments.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/621d10f8-23d5-4571-b0fd-aa12b0de98d8/Unit1_Section3.1-function-arguments.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# Python allows us to create **User Defined Functions** and provides many **Built-in Functions** such as **`print()`**.  
# - **`print()`** can be called using arguments (or without) and sends text to standard output, such as the console. 
# - **`print()`** uses **Parameters** to define the variable Arguments that can be passed to the Function. 
# - **`print()`** defines multiple string/numbers parameters which means we can send a long list of Arguments to **`print()`**, separated by commas.   
# - **`print()`** can also be called directly with just its name and empty parenthesis and it will return a blank line to standard output.

# ### Examples

# In[16]:


print('Hello World!', 'I am sending string arguments to print ')


# In[17]:


student_age = 17
student_name = "Hiroto Yamaguchi"
print(student_name,'will be in the class for',student_age, 'year old students.')


# In[18]:


print("line 1")
print("line 2")
# line 3 is an empty return - the default when no arguments
print()
print("line 4")


# ## Task 1: Passing arguments to `print()` 
# ### Many arguments can be passed to print 
# 
# - Update the print statement to use **`print()`** with **8** or more arguments

# In[19]:


#[ ] increase the number of arguments used in print() to 8 or more 
student_age = 17
student_name = "Hiroto Yamaguchi"
print(student_name,'will be in the class for',student_age, 'year old students.',"string thing",3.141592,10000,"VArIAbLES")


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B></B></font>
# ## Concept: Simple Functions
# Creating user-defined functions is at the core of computer programming.  Functions enable code reuse and make code easier to develop and maintain.
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/35458114-6211-4d10-85bc-7c4eb7834c52/Unit1_Section3.1-Simplest_Functions.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/35458114-6211-4d10-85bc-7c4eb7834c52/Unit1_Section3.1-Simplest_Functions.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Basics of a user-defined function
# - Define a function with **`def`** 
# - Use indentation (4 spaces)
# - Define parameters
# - Optional parameters 
# - **`return`** values (or none)
# - Function scope (basics defaults)  
# 

# ### `def some_function():`
# Use the &nbsp;**`def`** &nbsp;statement when creating a **function**.  
# - Use a function name that **starts with a letter** or underscore (usually a lowercase letter).
# - Function names can contain **letters, numbers or underscores**.
# - Parentheses &nbsp; **()**  &nbsp; follow the function name.
# - A colon &nbsp; **:**  &nbsp; follows the parenthesis.
# - The code for the function is indented under the function definition (use 4 spaces for this course).
# 
# ```python
# def some_function():
#    #code the function tasks indented here    
# ```
# The **end of the function** is denoted by returning to **no indentation**.

# ### Examples

# In[2]:


# defines a function named say_hi
def say_hi():
    print("Hello there!")
    print("goodbye")


# In[3]:


# define three_three 
def three_three():
    print(33) 


# 
# ## Concept: Calling Functions
# Call a simple function using the function name followed by parentheses.  For instance, calling print is  
# **`print()`**

# ### Examples

# In[5]:


# Program defines and calls the say_hi & three_three functions
# [ ] review and run the code

def say_hi():
    print("Hello there!")
    print("goodbye")
# end of indentation ends the function

# define three_three 
def three_three():
    print(33) 

# calling the functions
say_hi()
print()
three_three()


# ## Task 2: Define and call a simple function `yell_it()` 
# ### `yell_it()` &nbsp; prints the phrase with "!" concatenated to the end
# - Takes no arguments
# - Indented function code does the following
#   - Define a variable for called **`phrase`** and intialize with a short *phrase*
#   - Prints **`phrase`** as all upper-case letters followed by "!"
# - Call &nbsp; `yell_it` &nbsp; at the bottom of the cell after the function &nbsp;**`def`**.&nbsp; (**Tip:** no indentation should be used.)

# In[26]:


#[ ] define (def) a simple function called yell_it() and call the function

def yell_it(phrase):
    return(phrase + "!")
print(yell_it(input("What do you want to yell?")))


# ## Concept: Function Parameters
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c84008fa-2ec9-4e4b-8b6b-15b9063852a1/Unit1_Section3.1-funct-parameter.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c84008fa-2ec9-4e4b-8b6b-15b9063852a1/Unit1_Section3.1-funct-parameter.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# **`print()`** and **`type()`** are examples of built-in functions that have **parameters** defined.  
#   
# **`type()`** has a parameter for a **Python Object** and sends back the *type* of the object.
#   
# An **Argument** is a value given for a parameter when calling a function.  
# - **`type`** is called providing an **Argument** - in this case the string *"Hello"*
# ```python
# type("Hello")
# ```  
# 
# ### Defining function parameters
# - Parameters are defined inside of the parentheses as part of a function **`def`** statement
# - Parameters are typically copies of objects that are available for use in function code
# ```python
# def say_this(phrase):  
#       print(phrase)
# ```  
# ### Functions can have default arguments
# - Default arguments are used if no argument is supplied
# - Default arguments are assigned when creating the parameter list
# ```python
# def say_this(phrase = "Hi"):  
#       print(phrase)
# ```

# ### Example

# In[ ]:


# yell_this() yells the string Argument provided
def yell_this(phrase):
    print(phrase.upper() + "!")
    
# call function with a string
yell_this("It is time to save the notebook")


# In[ ]:


# use a default argument
def say_this(phrase = "Hi"):  
    print(phrase)
        
say_this()
say_this("Bye")


# ## Task 3: Define `yell_this()` and call with variable argument 
# - Define variable &nbsp; **`words_to_yell`** &nbsp; as a string gathered from user&nbsp; `input()`
# - Call &nbsp;**`yell_this()`** &nbsp;with &nbsp; **`words_to_yell`** &nbsp;as argument
# - Get user input() for the string words_to_yell

# In[7]:


# [ ] define yell_this() 
def yell_this(yell):
    return(yell + "!")
# [ ] get user input in variable words_to_yell
words_to_yell = input("What shall I yell?")
# [ ] call yell_this function with words_to_yell as argument
print(yell_this(words_to_yell))


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
