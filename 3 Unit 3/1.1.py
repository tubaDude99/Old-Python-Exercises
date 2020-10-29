#!/usr/bin/env python
# coding: utf-8

# # Section 1.1: Using Python Modules
# * import, import as
# * math: sqrt, //, %, \**
# * order of operations
# * ceil, floor
# * random: random.randint(a, b), randrange(start, stop[,step])
# * random: random.choice(seq), random.shuffle(x[,random])
# 
# ### Students will be able to:
# * Import different Python modules
# * Compute mathematical expressions using functions from the math module
# * Recognize the effect of operator precedence
# * Round real numbers to the nearest integer
# * Generate (pseudo-)random integers
# * Select a random element from a list
# * Shuffle the elements of a list

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Importing Modules
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/0bcc8dce-3438-4a5f-848e-80d12efa4aeb/DEV330x-1_1a_importing_modules.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/345425d1-481c-452d-8809-9677020d5bb9/DEV330x-1_1a_importing_modules.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# When writing code, you do not have to create everything from scratch. As a matter of fact, you are encouraged to use previously developed functions written by other programmers. Such code is usually distributed as a library of functions and other facilities. Libraries are further organized into `modules` that contain related code. 
# 
# A module is basically a file that contains functions, variable, and classes. To use a function from a module, you need to import that module to your code. There are several ways to import a module; the following examples show you how to import and use the power function `pow` to compute 2<sup>3</sup>, and 5<sup>2</sup>.
# 
# ### Importing the whole library
# ```python
# # import the whole math library
# import math
# 
# # compute 2 to the power 3
# math.pow(2, 3)
# 
# # compute 5 to the power 2
# math.pow(5, 2)
# ```
# 
# ### Importing the whole library and renaming it
# ```python
# # import the whole math library and rename it ml
# import math as ml
# 
# # compute 2 to the power 3
# ml.pow(2, 3)
# 
# # compute 5 to the power 2
# ml.pow(5, 2)
# ```
# 
# ### Importing only the `pow` function
# In this case, there is no need to refer to the `math` module when using `pow`.
# 
# ```python
# # import the `pow` function
# from math import pow
# 
# # compute 2 to the power 3
# pow(2, 3)
# 
# # compute 5 to the power 2
# pow(5, 2)
# ```

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Importing the `fabs` Function
# The following examples show you how to import and use the 'fabs' function, which calculates the absolute value of a number.
# * |-5| = 5
# * |12| = 12

# In[1]:


import math
x = -5
math.fabs(x)


# In[2]:


import math as ml
y = 12
ml.fabs(y)


# In[3]:


from math import fabs
fabs(-5)


# ---
# <font size="6" color="#B24C00" face="verdana"><B>Task 1</B></font>
# 
# ## Importing Modules
# 
# ### Finding the greatest common divisor
# The `math` module contains many useful functions. Skim through the Python Documentation Site's math page at https://docs.python.org/3/library/math.html and find an appropriate function that can compute the greatest common divisor of two numbers.

# In[4]:


# [ ] Import the math module and use an appropriate function to find the greatest common divisor of 16 and 28
import math

# --Completed--
from math import gcd
print(gcd(16, 28))


# In[7]:


# [ ] Prompt the user to input 2 positive integers then print their greatest common divisor

# --Completed--
import math
a = int(input("Enter a positive integer [a]: "))
b = int(input("Enter a positive integer [b]: "))
print("The greatest common divisor is: ", gcd(a, b))


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# ## Using `math` Functions
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/bc5c9d63-316c-4cef-861b-441f6f7693d5/DEV330x-1_1b_use_math_functions.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/53d6d81c-35b3-438d-9ab3-c3da5b17049e/DEV330x-1_1b_use_math_functions.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# The Python Documentation Site's page on [math](https://docs.python.org/3.6/library/math.html) module contains a lot of mathematically useful functions and constants. For example, it contains trigonometric functions such as `cos` and `sin`, and other functions such as `sqrt`.
# 
# ### Square root
# 
# The `sqrt` function computes the square root of a number. The following examples show how to compute:
# * &radic;<span style="text-decoration: overline">5</span>
# * &radic;<span style="text-decoration: overline">30</span>
# 
# ```python
# from math import sqrt
# 
# #compute the square root of 5
# sqrt(5)
# 
# #compute the square root of 30
# sqrt(30)
# ```
# 
# ### Other arithmetic operators
# 
# #### Division operator `/`
# Normal division is performed by the `/` operator. For example:
# 
# <sup>5</sup>/<sub>2</sub> = 2 <sup>1</sup>/<sub>2</sub> = 2.5
# 
# ```python
# In [1]: 5/2
# Out[1]: 2.5
# ```
# 
# #### Integer division operator `//`
# We can keep the integer and discard the fractional remainder by using the integer division operator `//`.
# 
# ```python
# In [1]: 5//2
# Out[1]: 2
# ```
# 
# #### Modulo operator `%` 
# The modulo operator is opposite to the integer division operator; it keeps the remainder of a division.
# 
# ```python
# In [1]: 5%2
# Out[1]: 1
# ```
# 
# #### Exponent operator `**`
# We saw earlier that the `pow` function from the `math` module computes the exponent. We can achieve the same functionality using the exponent `**` operator. To compute 2<sup>3</sup> and 5<sup>2</sup>:
# 
# ```python
# In [1]: 2**3
# Out[1]: 8
# 
# In [2]: 5**2
# Out[2]: 25
# ```
# 
# 

# ---
# <font size="6" color="#00A0B2" face="verdana"><B>Examples</B></font>
# 
# ### Pythagorean theorem
# 
# We can use the Pythagorean theorem (see the Wikipedia Site page on the [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem)) to compute the hypotenuse length of a right triangle as follows:
# 
# h<sup>2</sup> = a<sup>2</sup> + b<sup>2</sup>
# 
# h = &radic;<span style="text-decoration: overline">a<sup style="vertical-align:-0.5ex">2</sup> + b<sup style="vertical-align:-0.5ex">2</sup></span>
# 
# In Python, we can compute `h` as follows:
# 

# In[8]:


from math import sqrt
a = 3
b = 4
h = sqrt(a ** 2 + b ** 2)
print(h)


# ### Even or Odd?
# 
# To test if a number is even or odd, we usually divide it by 2 and check the remainder. If the remainder is 0, the number is even; otherwise, the number is odd. We can use the modulo operator to test for the remainder as follows:

# In[9]:


# Even number (print 0)
print(102 % 2)

# Odd Number (print 1)
print(77 % 2)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Using `math` Functions

# In[10]:


# [ ] Fill out the function is_even with a code block that returns True if n is even and returns False if n is odd

def is_even(n):
    return (n%2)==0

# Test the function 
x = 5
if is_even(x):
    print("Number is even")
else:
    print("Number is odd")

    
# --Completed--
def is_even(n):
    return (n % 2) == 0

# Test the function 
x = 5
if is_even(x):
    print("Number is even")
else:
    print("Number is odd")


# In[12]:


# [ ] Use the function is_even to print the square root of all the even numbers in the following list

l = [25, 34, 193, 2, 81, 26, 44]

def is_even(n):
    return (n % 2) == 0

from math import sqrt

for x in l:
    if is_even(x):
        print(x**0.5)
# --Completed--
l = [25, 34, 193, 2, 81, 26, 44]

def is_even(n):
    return (n % 2) == 0

from math import sqrt

for num in l:
    if is_even(num):
        print(sqrt(num))


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# ## Operator Precedence
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c81d803d-cfdd-419d-8eb0-632e7a92615b/DEV330x-1_1c_operator_precedence.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b79bb936-c26a-4839-b5ec-b9a2b0cce7b0/DEV330x-1_1c_operator_precedence.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# Similar to arithmetic operators, Python's operators also have precedence. The following table shows some of the operators we have seen in order from highest to lowest precedence.
# 
# | Operator | Description |
# |----------|-------------|
# | () | Parentheses|
# | \** | Exponentiation| 
# | *, /, //, %| Multiplication, division, integer division, modulo|
# |+, -| Addition, subtraction|
# 
# The parentheses can be used to group code to achieve the precedence you want.

# ---
# <font size="6" color="#00A0B2" face="verdana"><B>Examples</B></font>
# 
# 
# ### 5 + 2 &times; 8
# 
# Multiplication has a higher precedence, so the answer is: 5 + 16 = 21.

# In[13]:


5 + 2 * 8


# If you meant the calculation to be 7 &times; 8 = 56, you should use parentheses as (5 + 2) &times; 8.
# 

# In[14]:


(5 + 2) * 8


# ### <sup>12</sup> / <sub>4 * 3</sub>
# 
# The answer should be <sup>12</sup> / <sub>12</sub> = 1.

# In[15]:


12 / 4 * 3


# The expression resulted in a wrong answer because all three operators have the same precedence, and the expression was evaluated from left to right. There are 2 ways to fix this issue:

# In[16]:


# Method 1
12 / (4 * 3)


# In[17]:


# Method 2
12 / 4 / 3


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# 
# ## Operator Precedence

# In[18]:


# [ ] Correct the following expression so the answer is 10

(4 + 16) / 2

# --Completed--
(4 + 16) / 2


# In[19]:


# [ ] Correct the following expression so the answer is 250; review the operator precedence table and use only one () pair

2 * (3 + 2) ** 3

# --Completed--
2 * (2 + 3) ** 3


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Rounding Numbers
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c145efb2-b5b6-4f26-b7b4-b5e0006b75e2/DEV330x-1_1d_rounding_numbers.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/9bee71b0-296f-40a2-9837-d5c375a28f52/DEV330x-1_1d_rounding_numbers.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# In some cases, you need to round a real number into an integer. For example, 31.8 can be rounded up to the next integer (32), and it can also be rounded down (to 31).
# 
# #### Ceiling
# A real number can be rounded up in Python using the `ceil` function from the `math` module. The function takes a real number `x` and returns the smallest integer value greater than or equal to `x`.
# 
# ```python
# # importing the math library
# import math
# 
# # round up
# x = math.ceil(31.8)
# print(x) #will print 32
# ```  
# 
# #### Truncate
# The function `trunc` from the `math` module can round a real number into an integer by ignoring (truncating) the fraction part.
# 
# ```python
# # importing the math library
# import math
# x = math.trunc(31.8)
# print(x) #will print 31
# ```
# 
# #### Floor
# A real number can be rounded down in Python using the `floor` function from the `math` module. The function takes a real number `x` and returns the largest integer value less than or equal to `x`.
# 
# ```python
# # importing the math library
# import math
# 
# # round down
# x = math.floor(31.8)
# print(x) #will print 31
# ```  

# ---
# <font size="6" color="#00A0B2" face="verdana"><B>Examples</B></font>
# 
# You and a friend participated in a programming contest. Your hard work paid off, and your team won a prize of \$213, which you decide to split evenly. Unfortunately, you were given the prize in \$1 bills and neither of you has any coins. How should you split the prize?
# 
# An equal division of the prize is <sup>213</sup>/<sub>2</sub> = 106.5; however, you cannot get \$0.5 without destroying one of the \$1 bills, so you decide to use Python to round:

# In[20]:


from math import floor, ceil, trunc

prize = 213

option1 = floor(213 / 2)
print("You get", option1, " and your friend gets ", prize - option1)


# In[21]:


from math import floor, ceil, trunc

prize = 213

option2 = ceil(213 / 2)
print("You get", option2, " and your friend gets ", prize - option2)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4</B></font>
# 
# ## Rounding Numbers
# 

# In[22]:


# [ ] Use an appropriate rounding function to round 75.34 to 75 and then to 76

import math

x = 75.34
print(math.floor(x))
print(math.ceil(x))
# --Completed--

# Rounding down
## Option 1
print(math.trunc(x))

## Option 2
print(math.floor(x))

# Rounding up
print(math.ceil(x))


# ### `float` error rounding
# Representing `float` numbers in a computer is prone to rounding errors. In this task you should use one of the rounding functions to fix the error.

# In[25]:


# [ ] Use an appropriate rounding function to fix the following `float` error
from math import ceil
# Price of a chocolate box
p = 4.35

# Quantity needed
q = 200

# Order total price (Should be 4.35 * 200 = $870.00)
total = ceil(p * q)

print("Total price: ", total)

# --Completed--
import math

# Price of a chocolate box
p = 4.35

# Quantity needed
q = 200

# Total price (Should be 4.35 * 200 = $870.00)
total = math.ceil(p * q)

print("Total price: ", total)


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Generating Random Integers
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/fe1131a0-8ca7-477a-afd8-9c31b420ac8a/DEV330x-1_1e_generate_random_int.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/d9f2cf12-3277-4b38-89a1-4fb356e40aef/DEV330x-1_1e_generate_random_integer.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# If you are programming a Sudoku game that generates the same pattern every time you start it, chances are you will not play it many times. Introducing some randomness would make the game much more interesting. Python has several random number generator functions in the `random` module. You need only to import the module and use an appropriate function that suits your application.
# 
# #### Random integer between a and b
# The function `randint(a, b)` generates a random number n, where a &leq; n &leq; b
# 
# The following generates a number between 1 and 10:
# 

# In[26]:


from random import randint
print(randint(1, 10))


# #### Random integer from a range
# The randrange(start, stop[, step]) function generates a random number from a range of integers between start (included) and stop (excluded) with an optional step. The following generates a number between 1 and 10:

# In[27]:


from random import randrange
print(randrange(1, 11))


# In this case start = 1 and stop = 11 and we didn't specify the step value, which is 1 by default.
# 
# If step were specified as a value other than 1, such as 2, then `randrange(1, 11, 2)` would generate a number from the following range [1, 3, 5, 7, 9]. In other words, the randrange randomly selects a value from the range of integer numbers between 1 (included) and 11 (excluded) where the elements are separated by 2.

# In[28]:


from random import randrange
print(randrange(1, 11, 2))


# ---
# <font size="6" color="#00A0B2" face="verdana"><B>Examples</B></font>
# 
# ### Die roller
# If you are designing a game, it will be useful to have a function that can roll a die for you. The following shows a function that generates a single die roll:

# In[29]:


from random import randint

def die_roller():
    return (randint(1, 6))


# roll a die
print(die_roller())


# ### Odd random integers
# The following example shows you how to generate a random odd integer n, such that 1 &leq; n < 102:

# In[43]:


from random import randrange

def odd_random():
    return (randrange(1, 102, 2))

# Generate an odd random integer
print(odd_random())


# ---
# <font size="6" color="#B24C00" face="verdana"><B>Task 5</B></font>
# 
# ## Generating Random Integers
# 

# In[45]:


# [ ] Modify the die_roller() function to use randrange instead of randint
from random import randrange

def die_roller ():
    return (randrange(1, 7))

# --Completed--
from random import randrange

def die_roller ():
    return (randrange(1, 7))

# roll a die
print(die_roller())


# In[52]:


# [ ] Modify the odd_random() function to use randint instead of randrange
from random import randint

def odd_random():
    return(randint(1,51)*2-1)
print(odd_random())
# --Completed--
from random import randint

def odd_random():
    num = 0
    while(num % 2 == 0):
        num = randint(1, 102)
    return num

# Generate an odd random integer
print(odd_random())


# In[54]:


# [ ] Complete the function dice_roller() so it rolls 2 dice
# Use the die_roller function

from random import randint

def die_roller():
    return(randint(1, 6))

def dice_roller():
    return [die_roller(),die_roller()]

print(dice_roller())

# --Completed--

from random import randint

def die_roller():
    return(randint(1, 6))

def dice_roller():
    return [die_roller(), die_roller()]

print(dice_roller())


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Random Sequences
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/6cf75c18-0978-4ca4-bb48-81f5acd6d7dd/DEV330x-1_1f_random_sequences.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/6131f1bf-99d8-4812-9af8-6fd4b5ab6f18/DEV330x-1_1f_random_sequences.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# ### Selecting an element from a list
# In certain cases, you want to select an element from a range of non-integers or even a list of non-numeric elements. In such cases `randint` and `randrange` will not work; however, the `random` module comes with a `choice` function that returns a randomly chosen element from a list passed as an argument. For example, if you are designing a "Rock, Paper, Scissors" game, and you want the computer to choose one of the `string` options randomly, you need to use the `choice` function.
# 

# In[57]:


from random import choice

# Select Rock, Paper, or Scissors
def RPS():
    options = ['Rock', 'Paper', 'Scissors']
    # return one of the elements at random
    return (choice(options))

# Generate an option
print(RPS());


# ### Shuffling the elements of a list
# 
# Sometimes you do not want to choose a random element from a list, but rather you want to shuffle the content of a list. Say you want to rearrange a list of names to a random order. The function `shuffle` shuffles the elements of list in place as illustrated below:
# 

# In[62]:


from random import shuffle

x = ['Ana', 'John', 'Mike', 'Sally']

shuffle(x)

print(x)


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Picking a random playing card
# 
# Say you want to design a card game, and you want a function to pick one of the 52 cards at random. The `choice` function is a good fit.

# In[63]:


from random import choice

def pick_card():
    card_type = ['Clubs', 'Diamonds', 'Hearts', 'Spades'];
    card_number = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    
    # choose a type at random
    t = choice(card_type)
    n = choice(card_number)
    
    return [n, t]

# Show the randomly picked card
print(pick_card())


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 6</B></font>
# 
# ## Random Sequences

# In[66]:


# [ ] Modify the pick_card() function to use `shuffle` instead of choice
from random import choice

def pick_card():
    card_type = ['Clubs', 'Diamonds', 'Hearts', 'Spades'];
    card_number = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    shuffle(card_type)
    shuffle(card_number)
    t = card_type[0]
    n = card_number[0]
    
    return [n, t]
print(pick_card())
# --Completed--
from random import shuffle, randint

def pick_card():
    card_type = ['Clubs', 'Diamonds', 'Hearts', 'Spades'];
    card_number = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    
    # shuffle elements of both lists
    shuffle(card_type)
    shuffle(card_number)
    
    # choose an elements from the shuffled lists
    t = card_type[randint(0, 3)]
    n = card_number[randint(0, 12)]
    
    return [n, t]

# Show the randomly picked card
print(pick_card())


# In[68]:


# [ ] The following list contain the 10 most populous American cities; write code to randomly select one of the cities to visit
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
from random import choice
print(choice(cities))
# --Completed--
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

from random import choice

# Select a city
city = choice(cities)

print(city)

