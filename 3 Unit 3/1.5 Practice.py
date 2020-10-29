#!/usr/bin/env python
# coding: utf-8

# # Module 1 Practice
# 
# ### Students will be able to:
# 
# ## 3-1.1 Using Python Modules
# * Import different Python modules
# * Compute mathematical expressions using functions from the math module
# * Recognize the effect of operator precedence
# * Round real numbers into the nearest integer
# * Generate (pseudo-)random integers
# * Select a random element from a list
# * Shuffle the elements of a list
# 
# ##  3-1.2 Working with Date and Time
# * Assign and modify a time object (variable)
# * Assign and modify a date object (variable)
# * Get the current local date
# * Assign and modify a datetime object (variable)
# * Split a datetime object into separate time and date objects
# * Combine time and date objects into datetime objects
# * Display a datetime object as a formatted string
# 
# ## 3-1.3 Date and Time Arithmetic
# 
# * Create timedelta objects
# * Use timedelta objects to perform date arithmetic
# * Compare two datetime objects
# * Build a useful application using timedelta arithmetic
# 
# ## 3-1.4 File System
# 
# * Identify the platform running a Python script ('Linux', 'win32', 'Darwin')
# * Get the current working directory
# * Change the current working directory
# * List the content of the current working directory
# * Create a new directory
# * Remove a directory
# * Rename files and/or directories
# * Recognize the difference between a relative path and an absolute path
# * Test if a path exists
# * Test if a specific file or directory exists

# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## `math` module
# 

# In[1]:


# [ ] Use the math module to display an accurate value for pi
from math import pi
print(pi)


# In[2]:


# [ ] Write a program to:
# 1) find all the numbers in a list that are divisible by 3
# 2) display the square root of these numbers
# 3) use a rounding function to display the square roots while ignoring the decimal fraction
from math import sqrt, trunc
lst = [23, 45, 65, 2345, 42, 76, 37, 87, 647, 35, 37 ,39, 898, 92, 18]
for x in lst:
    if x%3 == 0:
        print(x,sqrt(x),trunc(sqrt(x)))


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Mathematical operators
# 

# ### Coin calculators
# 
# In the following exercises, you will develop functions to count the number of coins in a certain dollar amount. You will then use these functions to write a program that can calculate the change due to a customer in coins.

# #### Quarters

# In[3]:


# [ ] Complete the function `quarters_count` so it calculates and prints the number of quarters in `input_cents`
# The function input `input_cents` should be in cents 
# The function should print the number of calculated quarters in `input_cents`
# The function should return the number of remaining cents `remaining_cents` (which is less than 25, why?)
# HINT: You might want to use % and // operators
def quarters_count(cents):
    print(cents//25)
    return(cents%25)

# test with $2
# Output should be: 8 quarter\s
dollars = 2
total_cents = dollars * 100
remaining_cents = quarters_count(total_cents)

# test with $5.30
# Output should be: 21.0 quarter\s
dollars = 5.30
total_cents = dollars * 100
remaining_cents = quarters_count(total_cents)

# test with $9.49
# Output should be: 37.0 quarter\s
dollars = 9.49
total_cents = dollars * 100
remaining_cents = quarters_count(total_cents)


# #### Dimes

# In[4]:


# [ ] Complete the function `dimes_count` so it calculates and prints the number of dimes in `input_cents`
# The function input `input_cents` should be in cents 
# The function should print the number of calculated dimes in `input_cents`
# The function should return the number of remaining cents `remaining_cents` (which is less than 10, why?)
# HINT: You might want to use % and // operators

def dimes_count(cents):
    print(cents//10)
    return(cents%10)

# test with $2
# Output should be: 20 dime\s
dollars = 2
total_cents = dollars * 100
remaining_cents = dimes_count(total_cents)

# test with $5.30
# Output should be: 53.0 dime\s
dollars = 5.30
total_cents = dollars * 100
remaining_cents = dimes_count(total_cents)

# test with $9.49
# Output should be: 94.0 dime\s
dollars = 9.49
total_cents = dollars * 100
remaining_cents = dimes_count(total_cents)


# #### Nickels

# In[5]:


# [ ] Complete the function `nickels_count` so it calculates and prints the number of nickels in `input_cents`
# The function input `input_cents` should be in cents 
# The function should print the number of calculated nickels in `input_cents`
# The function should return the number of remaining cents `remaining_cents` (which is less than 5, why?)
# HINT: You might want to use % and // operators

def nickels_count(cents):
    print(cents//5)
    return(cents%5)

# test with $2
# Output should be: 40 nickel\s
dollars = 2
total_cents = dollars * 100
remaining_cents = nickels_count(total_cents)

# test with $5.30
# Output should be: 106.0 nickel\s
dollars = 5.30
total_cents = dollars * 100
remaining_cents = nickels_count(total_cents)

# test with $9.49
# Output should be: 189.0 nickel\s
dollars = 9.49
total_cents = dollars * 100
remaining_cents = nickels_count(total_cents)


# #### Change calculator

# In[8]:


# [ ] Complete the function `coins_due` to calculate and print the change due to a customer in coins
#
# The function `coins_due` has 2 inputs:
#      - `amount_paid`: Amount paid by a customer (in cents)
#      - `item_price`: Purchase price of an item
#
# The function should print:
#      - The number of quarters due
#      - The number of dimes due
#      - The number of nickels due
#      - The number of cents due
#      
# The function does not need to return anything
#
# HINT: Use the functions you developed before `quarters_count`, `dimes_count`, `nickels_count`


def quarters_count(cents):
    print(cents//25, 'quarters')
    return(cents%25)

def dimes_count(cents):
    print(cents//10, 'dimes')
    return(cents%10)

def nickels_count(cents):
    print(cents//5, 'nickels')
    return(cents%5)

def coins_due(paid, price):
    print("Change due:")
    paid -= price
    paid = quarters_count(paid)
    paid = dimes_count(paid)
    paid = nickels_count(paid)
    print(paid, 'pennies')

# Test case:
# amount paid = $10, item price = $5.37
# Output should be: 
#    Change due:
#    18.0 quarter\s
#    1.0 dime\s
#    0.0 nickel\s
#    3.0 cent\s

amount_paid = 10 * 100 # in cents
item_price = 5.37 * 100 # in cents
coins_due(amount_paid, item_price)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# 
# ## Random numbers
# 

# ### Probability of a die roll
# 
# It is possible to mathematically predict the probability (or chance) of getting a certain die roll; however, in this exercise you will use Python to do it without math. The trick is to roll a die a large number of times and count how many times we get a certain roll. You can, then, divide the count by the large number to get the probability. For a fair 6-sided die, the chance of getting any of its faces is about 16.6%

# In[12]:


# [ ] Complete the following program to display the probability of a certain die roll

from random import randint
r = int(input())
def die_roller ():
    return(randint(1, 6))
y = 0
for x in range(1000000):
    if randint(1,6) == r:
        y += 1
print(str(y/10000) + '%')


# ### Roll till you get 11
# 
# In this exercise, you will count the number of times you need to roll a set of 2 dice till you get a roll sum of 11.

# In[19]:


# [ ] Complete the following program so you can count the number of times needed to get a roll sum of 11

from random import randint

def die_roller():
    return(randint(1, 6))

def roll_sum():
    return die_roller() + die_roller()

x = 0
c = 0
while x != 11:
    c += 1
    x = randint(1,6) + randint(1,6)
print(c, 'times')


# ### Pick a candy
# 
# In this exercise, you will write a program to randomly select a candy from a box.

# In[21]:


# [ ] Complete the function `pick_candy` so it returns a candy from box at random
from random import choice
def pick_candy():
    box = ["Taffy", "Brownie", "Cookie", "Candy bar", "Chocolate", "Lollipop", "Gingerbread", "Marshmallow"]
    return(choice(box))

print(pick_candy())


# ### Shuffle a sorted list

# In[23]:


# [ ] Write a program to shuffle the following sorted list

lst = [3, 5, 9, 29, 35, 59, 62, 69, 102, 394, 594, 1993]

from random import shuffle
shuffle(lst)

print(lst)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4</B></font>
# 
# ## Working with date and time
# 

# ### Current date and time

# In[26]:


# [ ] Write a program that displays the current time as (HH:MM AM/PM) (example 02:28 PM)
from datetime import datetime

now = datetime.today()
now.strftime("%I:%M %p")


# In[27]:


# [ ] Write a program that displays the current time as (HH:MM:SS) (example 14:28:10)

from datetime import datetime

now = datetime.today()
now.strftime("%H:%M:%S")


# In[29]:


# [ ] Write a program that displays the current date as (Friday, December 15, 2017)

from datetime import date

now = date.today()
now.strftime("%A, %B %d, %Y")


# ### American VS European date format
# 
# In the United States, the date is formatted as Month/Day/Year; whereas, in Europe the date is formatted as Day/Month/Year. In this exercise, you will write two functions that will display a `datetime` object in the American or European format.

# In[31]:


# [ ] Complete the functions `american_format(d)` and `european_format(d)` to display the datetime object d in the proper format

from datetime import datetime

def american_format(d):
    return(d.strftime("%m/%d/%y"))
    
def european_format(d):
    return(d.strftime("%d/%m/%y"))
    
# test
d = datetime(month = 2, year = 2012, day = 13)

print("American format:", american_format(d))
print("European format:", european_format(d))


# ### Birthday days

# In[35]:


# [ ] Write a program to display a list of all your birthdays from the day you were born till 2025.
# You should also show the weekdays so you can see which of them was (or will be) on a weekend
from datetime import datetime

# Modify according to actual birthday
birthday = datetime(month = 3, day = 28, year = 2000)

def date_format(d):
    print(d.strftime("%A, %B %d, %Y"))
    
for y in range(birthday.year, 2026):
    date_format(birthday.replace(year = y))


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 5</B></font>
# 
# ## Date and Time Arithmetic
# 

# ### `timedelta`

# In[36]:


# Write a program to find out how many minutes are in a 4-week period
# Hint: Use a timedelta object and the total_seconds() method

from datetime import timedelta
td = timedelta(weeks = 4)
print("4 Weeks has:", td.total_seconds() / 60, "minutes")


# ### Date arithmetic

# In[37]:


# [ ] Write a program to compute the number of days remaining in the current year

from datetime import datetime

# today's date
now = datetime.today()

# last day of the current year
last_day = datetime(month = 12, day = 31, year = now.year)

# total number of days remaining in the current year
days_remaining = last_day - now

print(days_remaining.days, "days remaining in the current year")


# ### Comparing `datetime` objects

# In[38]:


# [ ] Complete the program below to find out if July 4th is within 10 days of today's date,
# if it is, find out if has passed or not


from datetime import datetime

# get today's date
todays_date = datetime.today()

# 4th of July of current year
july_4th = datetime(month = 7, day = 4, year = todays_date.year)

days_difference = todays_date - july_4th

if(abs(days_difference.days) < 10):
    if(july_4th < todays_date):
        print("July 4th has passed less than 10 days ago")
    else:
        print("July 4th is less than 10 days from today")
else:
    print("July 4th is not within 10 days from today")
    


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 6</B></font>
# 
# ## File System
# 

# ### Directory operations

# In[42]:


# [ ] Complete the following program to:
# 1) navigate to `parent_dir` directory (if not already in it)
# 2) create a new directory called `practice_1`
# 3) change the working directory to `practice_1`
# 4) display the current working directory to verify you are in the correct location
# 5) create a new directory called `practice_2`
# 6) verify that `practice_2` was created by listing the content of the current directory
# 7) rename `practice_2` as `sub_practice_2`
# 8) verify the name was successful changed by listing the content of the current directory
# 9) remove `sub_practice_2`
# 10) change working directory to the parent directory using `..`
# 11) remove `practice_1`
# 12) verify your current working directory and display its content

import os, os.path
# 1) navigate to `parent_dir` directory (if not already in it)
if('parent_dir' not in os.getcwd()):
    # Changing the current working directory to parent dir
    print("Changing working dir to parent_dir")
    os.chdir('parent_dir')
    print("Current working directory:", os.getcwd())

# 2) create a new directory called `practice_1`
os.mkdir('practice_1')

# 3) change the working directory to `practice_1`
os.chdir('practice_1')

# 4) display the current working directory to verify you are in the correct location
print(os.getcwd())

# 5) create a new directory called `practice_2`
os.mkdir('practice_2')

# 6) verify that `practice_2` was created by listing the content of the current directory
print(os.listdir())

# 7) rename `practice_2` as `sub_practice_2`
os.rename('practice_2','sub_practice_2')

# 8) verify the name was successful changed by listing the content of the current directory
print(os.listdir())

# 9) remove 'sub_practice_2'
os.rmdir('sub_practice_2')

# 10) change working directory to the parent directory using `..`
os.chdir('..')

# 11) remove `practice_1`
os.rmdir('practice_1')

# 12) verify your current working directory and display its content
print(os.getcwd())


# In[5]:


os.getcwd()


# ### Path operations

# In[3]:


# [ ] Write a program that prompts the user for a file or directory name
# if it exists in the current working directory, it prints whether it is a file or directory
import os, os.path
print(os.getcwd())
f = input()
if os.path.exists(f):
    if os.path.isfile(f):
        print('It exists and is a file')
    elif os.path.exists(f):
        print('It exists and is a directory')
else:
    print('It does not exist')
# --Completed--
import os.path

name = input("Enter a file or directory name: ")

if (os.path.exists(name)):
    if (os.path.isfile(name)):
        print(name, "is a file in the current working directory")
    elif (os.path.isdir(name)):
        print(name, "is a directory in the current working directory")
else:
    print(name, "does NOT exist in the current working directory")


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Module 1 Project</B></font>
# 
# ## Directory creator
# 
# 

# In[6]:


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
from datetime import date, time, datetime
import datetime
from random import randrange

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
    d = datetime.today()
    return int((d.minute + 15)**0.5)

def name_generator():
    """
    Generate a single directory name using the pattern (MM_DD_YY_randnum).
    
    args:
         NONE
    
    returns:
         `dir_name`: string containing a valid directory name
    """
    return(datetime.strftime("%m_%d_%y_") + str(randrange(10000,50000)))

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
    for x in range(directory_count()):
        directory_creator(name_generator)

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
         
    hint: 
        this requires very little code
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


# In[2]:


os.getcwd()

