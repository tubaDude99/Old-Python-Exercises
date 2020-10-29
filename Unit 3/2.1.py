#!/usr/bin/env python
# coding: utf-8

# # Section 2.1: Boolean Expressions and Compound Conditionals
# * and, or, not
# * if
# 
# ### Students will be able to: 
# * Describe the fundamental Boolean operators (and, or, not)
# * Use Boolean operators to combine comparisons
# * Recognize that different Boolean expressions can yield equal results
# * Employ combined comparisons to control program flow (i.e. `if` statements)
# 

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Boolean Operators
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/3fbe7bdc-1d33-47c8-b8dd-74251ab74143/DEV330x-2_1a_boolean_operators.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/30bf5f02-eda6-406f-a255-14d74d15ca76/DEV330x-2_1a_boolean_operators.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# #### `bool` data type
# Adding two numbers in Python results in another number; however, if two numbers were compared (i.e. to test for equality), the result would be of Boolean (`bool`) type. Unlike `int` and `float`, which can take many values, `bool` has only two values `True` and `False`. 
# 
# ```python
# In [1]: 5 == 6
# Out[1]: False
# 
# In [2]: 5 <= 6
# Out[2]: True
# ```
# 
# Comparing `string` variables or numerical variables is performed using relational operators, the following table lists the relational operators supported in Python
# 
# | Operator | Description |
# |----------|-------------|
# | < | Less than|
# | <=| Less than or equal to|
# | > | Greater than|
# | >= | Greater than or equal to|
# | == | Equal to|
# |!= | Not equal to|
# 
# #### Fundamental `bool` operators
# In addition to supporting numerical operators (+, -, &times; ...), Python also supports Boolean operators. The three basic Boolean operators are: `not`, `and`, `or`.
# 
# ##### `not`
# Is a unary operator; it operates on one variable (operand) by negating it. The following truth table shows the result of negating a `bool` variable `B`.
# 
# |`B`|`not B`|
# |---|-------|
# |False| True|
# |True|False|
# 
# ##### `and`
# Is a binary operator; it operates on two variables (operands). It produces `True` when both variables are `True` and produces `False` otherwise. The following truth table shows the effect of the `and` operator on combining `A` and `B`.
# 
# |`A`|`B`|`A and B`|
# |---|---|---------|
# |False|False|False|
# |False|True|False|
# |True|False|False|
# |True|True|True|
# 
# ##### `or`
# Is a binary operator; it operates on two variables (operands). It produces `True` if either (or both) of the variables is `True` and produces `False` otherwise. The following truth table shows the effect of `or` on combining `A` and `B`.
# 
# |`A`|`B`|`A or B`|
# |---|---|---------|
# |False|False|False|
# |False|True|True|
# |True|False|True|
# |True|True|True|
# 
# These operators are typically used to combine relational expressions rather than the constants `True` and `False`. This will allow you to construct more powerful conditional statements (i.e. `if` statements).
# 
# NOTE: `not` has the highest precedence, followed by `and`, then `or`. Similar to arithmetic operators, you can control the precedence using the parentheses operator `()` to group relational expressions.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### not

# In[1]:


# not operator
print("not True = ", not True)
print("not False = ", not False)


# ### `and`

# In[2]:


# and operator
print("False and False = ", False and False)
print("False and True = ", False and True)
print("True and False = ", True and False)
print("True and True = ", True and True)


# ### `or`

# In[3]:


# or operator
print("False or False = ", False or False)
print("False or True = ", False or True)
print("True or False = ", True or False)
print("True or True = ", True or True)


# ### Combining operators

# In[4]:


print("True and not False =", True and not False)
print("False or not True = ", False or not True)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Boolean Operators

# ### Boolean values (`True`, `False`)

# In[5]:


# [ ] Use relational and/or arithmetic operators with the variables x and y to write:
# 3 expressions that evaluate to True (i.e. x >= y)
# 3 expressions that evaluate to False (i.e. x <= y)

x = 84
y = 17

print(x > y)
print(y < x)
print(x != y)

print(x == y)
print(x < y)
print(y > x)


# ### Boolean operators (`not`, `and`, `or`)

# In[6]:


# [ ] Use the basic Boolean operators with the variables x and y to write:
# 3 expressions that evaluate to True (i.e. not y)
# 3 expressions that evaluate to False (i.e. x and y)

x = True
y = False
print(not not True)
print(x or y)
print(x and x)
print(not x)
print(x and y)
print(y or y)


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Combining Comparisons
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/58c04190-4f7f-4587-b4e2-71366d93a8c1/DEV330x-2_1b_combining_compariso.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ca4da009-b4b9-486a-a4dd-58b58817c325/DEV330x-2_1b_combining_comparisons.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# The basic `bool` operators can be used to combine multiple relational tests. For example, say you want to test whether a variable `x` contains a number within a certain range (i.e. 10 &leq; x &leq; 20). You can perform this test, by checking whether the number is greater than or equal to 10 and whether the number is less than or equal to 20.
# 
# ```python
# In [1]: x = 11
# In [2]: (x >= 10) and (x <= 20)
# Out[2]: True
# 
# In [3]: x = 9
# In [4]: (x >= 10) and (x <= 20)
# Out[4]: False
# ```
# 
# The relational tests need not be numerical. For example, you can test whether a variable `c` contains a capital letter (i.e. 'A' &leq; c &leq; 'Z').
# 
# ```python
# In [1]: c = 'N'
# In [2]: (c >= 'A') and (c <= 'Z')
# Out[2]: True
# 
# In [3]: c = 'n'
# In [4]: (c >= 'A') and (c <= 'Z')
# Out[4]: False
# ```

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Testing whether a number is outside a range
# 

# In[7]:


# Testing if x is outside the range [10, 20]

x = 11
(x < 10) or (x > 20)


# In[8]:


# Testing if x is outside the range [10, 20]

x = 50
(x < 10) or (x > 20)


# ### Testing whether a number is positive and odd
# You can combine relational operators, arithmetic operators, and Boolean operators to generate powerful Boolean expressions. In this example, you will test whether a number is both positive and odd.

# In[9]:


# Testing if x is a positive and odd number

x = 11
(x > 0) and (x % 2 != 0)


# In[10]:


# Testing if x is a positive and odd number

x = -11
(x > 0) and (x % 2 != 0)


# In[11]:


# Testing if x is a positive and odd number

x = 22
(x > 0) and (x % 2 != 0)


# ### Testing using 2 different variables
# You can combine Boolean expressions of different variables. In this example, you will test whether a driver's name starts with the letter `C` and she is 18 years or younger.

# In[12]:


# Driver information
name = 'Colette'
age = 17

# Testing if name starts with `C` and the age is 18 or less
(name.startswith('C')) and (age <= 18)


# In[13]:


# Driver information
name = 'John'
age = 17

# Testing if name starts with `C` and the age is 18 or less
(name.startswith('C')) and (age <= 18)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Combining Comparisons

# In[14]:


# [ ] Write an expression to test if x is an even number outside the range [-100, 100]
x = -99

((x < -100) or (x > 100)) and (x % 2 == 0)
# Test your expression with:
# x = 104 (True)
# x = 115 (False)
# x = -106 (True)
# x = -99 (False)


# In[15]:


# [ ] Write an expression to test if a string s starts and ends with a capital letter
# HINT: You might find the function `str.isupper()` useful
s = "Not Capital"
s[0].isupper() and s[-1].isupper()
# Test your expression with
# s = "CapitaL" (True)
# s = "Not Capital" (False)


# In[20]:


# [ ] Write an expression to test if a string s contains a numerical value
# then test if the value is greater than the value stored in x
# HINT: Use the functions `s.isnumeric()` and `float(s)`

# Test your expression with
# s = "39"
# x = 24
# Expression should yield True

# s = "a39"
# x = 24
# Expression should yield False

s = "a39"
x = 24
s.isnumeric() and float(s) > x


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Boolean Expressions Equality
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/8bc3d44c-4851-496d-a33d-855c77f4adaf/DEV330x-2_1c_boolean_expressions.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b08216e6-86f6-4f4b-af71-42eb0239db3c/DEV330x-2_1c_boolean_expressions_equality.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# It is possible to write two (or more) different Boolean expressions that yield the same results. Let's revisit the example testing whether x is within the range [10, 20].

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Expression 1: Test whether `x` is within [10, 20]

# In[21]:


x = 11
(x >= 10) and (x <= 20)


# In[22]:


x = 30
(x >= 10) and (x <= 20)


# ### Expression 2: Test whether `x` is within [10, 20]

# In[23]:


x = 11
not((x < 10) or (x > 20))


# In[24]:


x = 30
not((x < 10) or (x > 20))


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# 
# ## Boolean Expressions Equality

# In[26]:


# [ ] Write an expression equivalent to the one below 
# to test if x is outside the range [10, 20] (seen in a previous example)

# (x < 10) or (x > 20)
x = 50
print(not(10<=x<=20))
# Test your expression with 
# x = 11 (False)
# x = 50 (True)


# In[28]:


# [ ] Write a second expression to test if x is an even number outside the range [-100, 100]
# Do NOT use the expression you wrote for a previous exercise

# Test your expression with:
# x = 104 (True)
# x = 115 (False)
# x = -106 (True)
# x = -99 (False)
x = -99
print(x%2 == 0 and not(-100<=x<=100))


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Compound Conditionals
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/aa343ee6-2e23-4d66-a56f-d6db613941bc/DEV330x-2_1d_compound_conditiona.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/d896e0b0-5483-4971-9a94-8e60f31b7cc6/DEV330x-2_1d_compound_conditionals.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# 
# Combined Boolean expressions can be used within the testing conditions of `if` and `elif` statements. This will let you write compound conditionals and give you fine control over the program flow. For example, you can test the validity of user input against several combined conditions. Similarly, you can also check the content of a variable against multiple ranges.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Testing validity of user input

# In[31]:


# Solicit user input
x = input("Enter an odd positive number: ")

# Convert the string input into int
x = int(x)

# Test number for validity
if ((x > 0) and (x % 2 != 0)):
    print(x, "is a valid number")
else:
    print(x, "is NOT a valid number")


# ### Testing inclusion in a range

# In[34]:


# Solicit user input
y = input("Enter your birth year: ")

# Convert the string input into int
y = int(y)

# Check the decade membership
if (y < 1970):
    print("You were born before 1970!")
elif (y >= 1970 and y < 1980):
    print("You were born in the 70s!")
elif (y >= 1980 and y < 1990):
    print("You were born in the 80s!")
elif (y >= 1990 and y < 2000):
    print("You were born in the 90s!")
elif (y >= 2000 and y < 2010):
    print("You were born in early 2000s!")
else:
    print("You were born in the current decade!")


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4</B></font>
# 
# ## Compound Conditionals

# In[37]:


# [ ] Write a program to validate that user input is outside the range [0, 100]
x = int(input())
if not(0<=x<=100):
    print("Right")
else:
    print("Wrong")


# ### BMI category 
# The Body Mass Index (BMI) measures the body fat using the weight and height of a person. The BMI is used to classify adults into categories as in the following table.
# 
# |Category|BMI range|
# |--------|---------|
# |Underweight| < 18.5|
# |Normal Weight| 18.5 - 24.9|
# |Overweight|25 - 29.9|
# |Obese| &geq; 30|
# 

# In[41]:


# [ ] Write a program to ask a user for her/his BMI index, then display the user's BMI category
b = float(input("BMI? "))

# Display the BMI category
if (b < 18.5):
    print("Underweight")
elif (18.5 <= b <= 24.9):
    print("Normal weight")
elif (25 <= b <= 29.9):
    print("Overweight")
else:
    print("Obese")

