#!/usr/bin/env python
# coding: utf-8

# # Section 2.3: Containment, Identity, and Operator Precedence
# * Containment (in, not in)
# * Identity (is, is not)
# * Operator precedence
# 
# ### Students will be able to: 
# * Test whether a list contains a certain element
# * Test whether a string is contained in another string
# * Test the identity of objects (i.e. int, float, lists, string)
# * Recognize the effects of operator precedence (including assignment (=), relational (<, >=,...), Boolean (and, or, not), arithmetic (/ // % * + -), identity (is), and containment (in))
# 

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Containment (`in`, `not in`)
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/2326044b-af10-484c-92e2-9d030651b532/DEV330x-2_3a_containment.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/247ee553-c187-4afa-b711-1f7a4dcaf578/DEV330x-2_3a_containment.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# You will commonly encounter the need to test whether an element is contained in another container (i.e. list, tuple, string, etc.). For example, you might want to test whether `5` is an element of the list `[4, 8, 5, 6]`, or you might need to know if a substring `"or"` is contained within another string `"Hello World"`. It is possible to perform these tests by iterating over the elements of the container (list) and comparing them one by one to the element of interest. However, because this procedure is commonly used, Python has a containment operator (`in`), which can perform this procedure much more efficiently.
# 
# NOTE: You can test if an element is NOT contained in another container by using the (`not in`) operator.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 

# ### List containment
# 
# #### Is a number contained in a list?
# In this example, you will see how to test if a number is contained in another list of numbers

# In[1]:


lst_container = [4, 8, 5, 6]

x = 5
if (x in lst_container):
    print(x, "is contained in list")
else:
    print(x, "is NOT contained in list")
    

x = 10
if (x in lst_container):
    print(x, "is contained in list")
else:
    print(x, "is NOT contained in list")


# #### Is an element contained in a list?
# A Python list can contain elements of different types. In this example, you will test if an element is contained in a list containing a: number, list, string.

# In[2]:


lst_container = [4, [7, 3], 'string element']

# 4 is an element in lst_container
x = 4
print(x, "contained in lst_container:", x in lst_container)

# 7 is an element of a list inside lst_container, but it is NOT an element of the lst_container
x = 7
print(x, "contained in lst_container:", x in lst_container)

# [7, 3] is an element of lst_container
x = [7, 3]
print(x, "contained in lst_container:", x in lst_container)


# ### String containment
# 
# You can test if a substring is contained in another larger string.

# In[3]:


sentence = "This is a test sentence"
word1 = "test"
word2 = "something"

# testing if word1 is a substring of sentence
if (word1 in sentence):
    print(word1, "is contained in:", sentence)
else:
    print(word1, "is not contained in:", sentence)
    
# testing if word2 is a substring of sentence
if (word2 in sentence):
    print(word2, "is contained in:", sentence)
else:
    print(word2, "is not contained in:", sentence)
    
# another method to test if word2 is a substring of sentence
# using the not operator
if (word2 not in sentence):
    print(word2, "is not contained in:", sentence)
else:
    print(word2, "is contained in:", sentence)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Containment (`in`, `not in`)

# ### Number containment

# In[5]:


# [ ] Write a program to prompt the user for an integer input between 0 and 100
# then print if the number is contained in `lst`

lst = [22, 89, 69, 78, 58, 22, 56, 13, 74, 8, 32, 58, 8, 63, 46, 79, 9, 38, 25, 96]
while 1:
    x = int(input())
    if 0 < x < 100:
        break
if x in lst:
    print("yes")
else:
    print("no")


# ### List containment

# In[11]:


# [ ] The `records` list contains information about a company's employees
# each of the elements in `records` is a list containing the name and ID of an employee.
# Write a program to test if `applicant` is contained in `records` and display an appropriate message

# Records of names and IDs
records = [['Colette', 22347], ['Skype', 35803], ['Alton', 45825], ['Jin', 24213]]

applicant = ['Joana', 20294]
if applicant in records:
    print("person")
else:
    print('nonperson')


# ### String containment

# In[13]:


# [ ] Write a program to prompt the user for a letter (capital or small) then print if the letter is a vowel
# HINT: Use a string containing all the vowels and the `in` or `not in` operator
if input() in 'aeiouAEIOU':
    print("vowel")
else:
    print("not vowel")


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Identity (`is`, `is not`)
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/a15e74d8-691d-4c4b-8629-ec176f7ee4e7/DEV330x-2_3b_identity.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/df49ad45-b704-4f36-b744-6bee05f147c5/DEV330x-2_3b_identity.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# Python is an object-oriented programming language that utilizes objects. You have been using objects; however, you have called them variables and lists. Python saves objects in certain memory locations, knowing the locations is of little importance; however, knowing if two seemingly different objects are at the same memory location is important. This will be critically important when dealing with sequences such as list, tuples, strings, and dictionaries.
# 
# In Python, the concepts of identity and equality are related but not the same, for example:
# * When two objects are saved in the same memory location, they are equal and identical
# * When two objects are saved in different memory locations and contain the same information, they are equal but not identical
# * When two objects are saved in different memory locations and contain different information, they are not equal nor identical
# 
# You can test whether two objects contain the same information using the equality operators `==` or `!=`. To test whether two objects are identical, you need to use the identity operators `is` or `is not`.
# 

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# In the following examples, when objects are identical, it is implied they are saved in the same memory location.

# ### Identity of variables containing numerical literals
# 
# #### `int` literals
# Equal `int` literals are saved in the same memory location

# In[14]:


# x, y: equal, identical 
x = 5
y = 5
print("x equal y ? ", x == y)
print("x is identical to y ?", x is y)


# In[15]:


# x, y: not equal, not identical
x = 5
y = 6
print("x equal y ? ", x == y)
print("x is identical to y ?", x is y)


# #### `float` literals
# 
# Equal `float` literals are not identical. In other words, equal `float` literals are saved in different memory locations.

# In[16]:


# x, y: equal, not identical 
x = 5.6
y = 5.6
print("x equal y ? ", x == y)
print("x is identical to y ?", x is y)


# In[17]:


# x, y: not equal, not identical 
x = 5.6
y = 10.6
print("x equal y ? ", x == y)
print("x is identical to y ?", x is y)


# ### Identity of variables containing lists
# 
# The following examples are particularly important to understanding the concept of identity and equality. You will see how you can create two equal but not identical lists, then you will see how to create two identical (and equal) lists and the effect of changing one on the other.

# #### Equal but not identical lists
# You can create two equal but not identical lists, by assigning the same list literal to two different variables. A change in one of the list does not have any effect on the content of the other.

# In[18]:


# Different lists containing the same data
x = [4, 9, 8]
y = [4, 9, 8]

# x and y are equal, because they contain the same data
# x and y are NOT identical, because they are saved in different memory locations
print("x equal y ? ", x == y)
print("x is identical to y ?", x is y)

# Because they are not identical, changing x does not affect y
x[1] = 5

print()
print("After changing x[1]")
print("x =", x)
print("y =", y)
print("x equal y ? ", x == y)
print("x is identical to y ?", x is y)


# #### Equal and identical lists
# Two variables referring to the same list are called identical variables. They can be treated as two names for the same list; in other words, both of the variables refer to the same memory location and a change in one is reflected as the same change in the other. You can simply create an identical variable by assigning it the variable of interest. The following example illustrates this idea.

# In[19]:


# Identical list
x = [4, 9, 8]
y = x

# x and y are equal, because they contain the same data
# x and y are identical, because they are saved in the same memory location
print("x equal y ? ", x == y)
print("x is identical to y ?", x is y)

# Because they are identical, changing x also changes y
x[1] = 5

print()
print("After changing x[1]")
print("x =", x)
print("y =", y)
print("x equal y ? ", x == y)
print("x is identical to y ?", x is y)


# ### Identity of variables containing string literals
# 
# String identity and equality is very similar to that of lists. However, when you assign equal strings to different variables, the interpreter might detect this and optimize the code by making the variables identical.

# In[30]:


# s1, s2: equal, not identical
s1 = 'whole milk'
s2 = 'whole milk'
print("s1 equal s2 ? ", s1 == s2)
print("s1 is identical to s2 ?", s1 is s2)
print("s1 is not identical to s2 ?", s1 is not s2)


# In[29]:


# s1, s2: equal, identical
s1 = 'whole milk'
s2 = s1
print("s1 equal s2 ? ", s1 == s2)
print("s1 is identical to s2 ?", s1 is s2)
print("s1 is not identical to s2 ?", s1 is not s2)


# In[22]:


# s1, s2: equal, identical (after interpreter optimization)
s1 = 'python'
s2 = 'python'
print("s1 equal s2 ? ", s1 == s2)
print("s1 is identical to s2 ?", s1 is s2)
print("s1 is not identical to s2 ?", s1 is not s2)


# In[23]:


# s1, s2: not equal, not identical 
s1 = 'python'
s2 = 'java'
print("s1 equal s2 ? ", s1 == s2)
print("s1 is identical to s2 ?", s1 is s2)
print("s1 is not identical to s2 ?", s1 is not s2)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Identity (`is`, `is not`)

# ### Identity of variables containing strings

# In[2]:


# [ ] Write a program to:
# 1) Create a variable `e` that is equal but NOT identical to `s`
# 2) Test the equality and identity of `s` and `e` and print the results
# 3) Create a variable `i` that is equal and identical to `s`
# 4) Test the equality and identity of `s` and `i` and print the results
# 5) Test the equality and identity of `e` and `i` and print the results

s = "Whole Wheat Bread"
e = "Whole Wheat Bread"
print('e and s:')
if s == e:
    print("equal")
else:
    print('not egual')
if s is e:
    print('identical')
else:
    print('not identical')
print('i and s:')
i = s
if s == i:
    print("equal")
else:
    print('not egual')
if s is i:
    print('identical')
else:
    print('not identical')


# ### Identity of variables containing lists

# In[4]:


# [ ] Write a program to:
# 1) Create a variable `e` that is equal but NOT identical to `x`
# 2) Test the equality and identity of `x` and `e` and print the results
# 3) Create a variable `i` that is equal and identical to `x`
# 4) Test the equality and identity of `x` and `i` and print the results
# 5) Test the equality and identity of `e` and `i` and print the results

x = [[-1, 2],[3, 4],[-5, 6]]
e = [[-1, 2],[3, 4],[-5, 6]]
print('e and x:')
if x == e:
    print("equal")
else:
    print('not egual')
if x is e:
    print('identical')
else:
    print('not identical')
print('\nx and i:')
i = x
if x == i:
    print("equal")
else:
    print('not egual')
if x is i:
    print('identical')
else:
    print('not identical')
print('\ne and i:')
if i == e:
    print("equal")
else:
    print('not egual')
if i is e:
    print('identical')
else:
    print('not identical')


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Operator Precedence
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/38d94845-3999-49d3-91a7-0f049921bb73/DEV330x-2_3c_operator_precedence.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c0b27a76-d780-4f44-9219-5bbc3d408978/DEV330x-2_3c_operator_precedence.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# You have seen that the Boolean operator `not` has a higher precedence than the Boolean operators `and` and `or`. You also know that in arithmetic expressions, multiplication has a higher precedence than addition and subtraction. In Python, you can combine different operator types in the same expression (`3 + 1 > 5`); when you do, operator precedence still applies. The following table summarizes operator precedence from lowest precedence to highest precedence. Operators in the same row have the same precedence, and the precedence is resolved from left to right, for example in (`3 * 6 / 9`), `*` and `/` have the same precedence, and Python will perform the multiplication first (`18 / 9`) followed by the division (`2`).
# 
# |Operator| Short Description|
# |--------|------------------|
# |or| Boolean or|
# |and| Boolean and|
# |not| Boolean not|
# |in, not in, is , is not, <, <=, >, >=, !=, ==| Containment and identity test, relational comparison|
# |+, -| Arithmetic addition and subtraction|
# |\*, /, //, % | Arithmetic, multiplication, division, int division, modulo|
# |\*\* | Exponentiation|
# |(), [], {}| Parentheses, brackets|
# 
# NOTE: When in doubt, use the parentheses operator to control the precedence in an expression

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# Use the operator precedence table to predict the outcome of these examples before looking at the answers.

# ### Arithmetic operations

# In[5]:


# * has higher precedence
2 + 3 * 6


# In[6]:


# To change precedence, we add ( )
(2 + 3) * 6


# ### Combined operations

# In[7]:


# Arithmetic and relational operations
3 * 2 < 10


# In[8]:


# Exponentiation has a higher precedence
2**3 + 1 == 16


# In[10]:


# Adding () changes the precedence of 3 + 1 and the exponentiation operator
2 ** (3 + 1) == 16


# In[11]:


# Arithmetic, relational, and Boolean operators
2 ** (3 + 1) == 16 and 3 * 2 < 10


# In[12]:


# Arithmetic, relational, Boolean, and containment operators
2 ** (3 + 1) != 16 or 3 * 2 in [5, 6, 3]


# ### Unexpected outcome!
# The following 2 examples generate unexpected outcomes!

# In[13]:


# Unexpected outcome!
6 < 10 != True


# In[14]:


# Unexpected outcome!
6 < 10 != False


# What is actually being evaluated is:
# 
# First case:
# ```python
# (6 < 10) and (10 != True)
# ```
# 
# Second case:
# ```python
# (6 < 10) and (10 != False)
# ```
# 
# In both cases, 10 is not logical and doesn't equal `True` or `False`. Therefore, both expressions are evaluated as (`True and True`) which is `True`. 
# 
# You might face similar confusing cases. It is highly recommended that you use `()` to fix and debug such cases.

# In[15]:


# Expected outcome after adding ()
(6 < 10) != True


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# 
# ## Operator Precedence

# In[16]:


# [ ] Correct the following expression so the answer is `True`

(6 + 2 < 9) == True


# In[21]:


# [ ] Correct the following expression so the answer is `True`

3 ** (2 + 1) >= 3 * 8 + 1


# In[22]:


# [ ] Correct the following expression so the answer is `True`

(5 + 3) * 2 == 16


# In[23]:


# [ ] Correct the following expression so the answer is `True`

4 > 3 and (5 + 6 > 7) == True

