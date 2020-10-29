#!/usr/bin/env python
# coding: utf-8

# # Section 2.2: Advanced Loop Structures
# * pass
# * while, for: break, continue
# * Nested loops
# * Loops containing compound conditional expressions
# 
# ### Students will be able to:
# * Recognize the purpose of a `pass` statement
# * Differentiate between `break` and `continue` statements
# * Control loop iteration using `break` or `continue` 
# * Use nested loops to iterate over the elements of a table
# * Employ compound conditional expressions in a loop structure

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## `pass` statements
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/5155a699-1c10-4769-9f20-646bc569f62a/DEV330x-2_2a_pass.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c47b51bb-9f15-4dea-9a42-b11856121e9d/DEV330x-2_2a_pass.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# The `pass` statement does nothing; however, it still has useful applications. It is typically used as a placeholder, indicating that it will be replaced by valid functioning code. For example, say you are developing a function but you are not ready to write its code; you can use `pass` as a placeholder to make your code syntactically correct and avoid any interpreter errors.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 

# In[1]:


# Does nothing, but syntactically valid
def useless_function():
    pass


# In[2]:


# Does nothing, but syntactically valid
for i in range(10):
    pass


# In[3]:


# Does nothing, but syntactically valid
if (5 < 6):
    pass


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Changing Loop Iterations
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/06d815de-86da-49c0-9e98-da56934d8d1f/DEV330x-2_2b_changing_loop_itera.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/d3e85125-08ca-4fa9-b063-48e992bd6fab/DEV330x-2_2b_changing_loop_iteration.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# ### `break` statements
# It is sometimes useful to stop a loop and then resume executing the code that follows. This process is called breaking a loop and can be achieved in Python using a `break` statement. A `break` statement can be used with `while` or `for` loops and it breaks the innermost loop of nested loops. 
# 
# A `break` statement is useful for improving the efficiency of your code. For example, assume you are looping over the elements of an unsorted list looking for the first occurrence of a 0. If a 0 is encountered earlier in the search, there is no need to continue the search and a loop break would be very desirable. `break` statements can also be used to break out of infinite loops.
# 
# ### `continue` statements
# Sometimes you do not need to break out of a loop, but you want to skip an iteration and jump to the next one. This can be done in Python using the `continue` statement. A `continue` statement can be used with `while` or `for` loops, and it applies to the innermost loop of nested loops. A `continue` statement is used to improve the efficiency of code by skipping unnecessary iterations.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### `break` statements
# 
# #### Breaking loops to improve efficiency

# In[4]:


# Find the index of the first occurrence of 611 in an arbitrarily long list

# Define a long list
lst = [976, 618, 812, 898, 804, 689, 611, 630, 467, 411, 648, 931, 618, 425, 328, 196, 56, 615, 458, 166, 115, 118, 22, 585, 213, 855, 615, 478, 234, 360, 981, 174, 993, 627, 911, 385, 219, 577, 540, 49, 164, 109, 893, 727, 687, 709, 971, 781, 802, 701, 789, 421, 863, 44, 573, 91, 140, 338, 36, 102, 502, 723, 134, 336, 940, 969, 649, 598, 413, 307, 929, 951, 993, 436, 149, 280, 907, 733, 713, 268, 29, 946, 102, 277, 352, 449, 527, 201, 566, 643, 118, 587, 717, 358, 542, 223, 846, 244, 83, 268]

# Find the index (without break)
index = 0
iteration_count = 0
for num in lst:
    if (num == 611):
        found_at = index
    index = index + 1
    iteration_count = iteration_count + 1

print("Without using a break, 611 was found at index:", found_at, "using", iteration_count, "iterations")



# Find the index (with break)
index = 0
iteration_count = 0
for num in lst:
    if (num == 611):
        found_at = index
        break # adding a break to improve efficiency
    index = index + 1
    iteration_count = iteration_count + 1

print("Using a break, 611 was found at index:", found_at, "using", iteration_count, "iterations")


# #### Breaking infinite loops
# Infinite loops have some applications, and a `break` statement would be necessary to break such loops and continue executing the rest of a program. For example, infinite loops are useful for prompting the user for specific input, and should be broken when valid input is entered.

# In[5]:


# Prompt the user for a positive number
while True:
    x = int(input("Enter a positive number: "))
    if (x > 0):
        break #x is positive, break the loop
    


# ### `continue` statements

# In[6]:


# Print the odd elements in a list
lst = [14, 6, 5, 10, 6, 9, 33, 103, 21, 55]

for num in lst:
    # Skip all even numbers
    if (num % 2 == 0):
        continue
    print(num)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Changing Loop Iterations

# ### Prime numbers
# A prime number is a number greater than 1 that is divisible only by 1 and itself. Prime numbers play an important role in several cryptographic algorithms that we use every day, and it is very useful to build a program to test whether a number is prime.

# In[13]:


# [ ] The following program tests if `num` is prime or not, use a `break` statement to improve its efficiency
# and reduce the number of necessary iterations

# Compare the number of necessary iterations with and without the `break` statement
# Use the following numbers for the comparison: 

num = 45345
num = 11579
num = 948240
num = 128093
num = 519937
num = 694394

prime = True # assume num is prime unless proven otherwise

iteration_count = 0

for i in range(2, num):
    if num % i == 0:
        prime = False;
        break
    iteration_count = iteration_count + 1

# Display results
if prime:
    print(num, "is prime")
else:
    print(num, "is NOT prime")

print("Total number of iterations:", iteration_count)


# ### User input

# In[15]:


# [ ] Write a program to prompt the user for an odd number; use an infinite loop and a `break` statement.
while 1:
    x = int(input())
    if (x % 2) != 0:
        break
print(x)


# ### `continue`

# In[18]:


# [ ] Modify the following program to display numbers that are divisible by 7 along with their square roots.
# HINT: Use a `continue` statement in the loop

from math import sqrt

for x in range(1, 100):
    if x%7 == 0:
        print(x, x**0.5)


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Nested loops
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/85528e5f-0e46-4493-b997-b7b1cf504c6a/DEV330x-2_2c_nested_loops.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/1c4cc361-3603-45d5-9d59-be7ff9846d7b/DEV330x-2_2c_nested_loops.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# You can use a loop inside another loop, this concept is known as nested loops. Nested loops have many applications, but they are especially useful for iterating over the elements of a table. A table can be represented in Python as a 2 dimensional list, which is a list containing other lists. You will need two loops to iterate over all the elements of a table, the outer loop iterates over the rows of the table, while the inner loop iterates over the columns in each row.
# 

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Displaying a table
# In this example, you will print the elements of a 2 dimensional list as a table:
# 
# | 
# |---|---|---|
# | 5 | 2 | 6 |
# | 4 | 6 | 0 |
# | 9 | 1 | 8 |
# | 7 | 3 | 8 |
# 
# NOTE: `print` statements end with a new line character. You can change this behavior by using an optional argument `end`. By default `end` is set to a new line. You can set it to the empty string to suppress the new line behavior. In this example, you will set `end` to `\t`, which replaces the new line with a tab.
# 

# In[19]:


# list of lists
table = [[5, 2, 6], [4, 6, 0], [9, 1, 8], [7, 3, 8]]

for row in table:
    for col in row:
        # print the value col followed by a tab
        print(col, end = "\t")

    # Print a new line
    print()


# ### Character art
# In this example you will see how you can generate an interesting two dimensional character art

# In[20]:


# Generate a staircase character art
# Size controls the number of steps
def char_art(steps):
    for row in range(steps):
        for col in range(steps):
            if(col <= row):
                print("[]", end = "")
        print()

# Generate a staircase with 6 steps                
char_art(6)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Nested Loops

# ### Sum of rows

# In[22]:


# [ ] Write a program to display the sum of each row in table
table = [[5, 2, 6], [4, 6, 0], [9, 1, 8], [7, 3, 8]]
for x in table:
    t = 0
    for y in x:
        t += y
    print(t)


# ### Character art

# In[39]:


# [ ] Complete the function `generate_star` so it displays a star of variable `size` using "*"
# For size = 5 the star should look like:
# *   *
#  * * 
#   *  
#  * * 
# *   *

def generate_star(s):
    for y in range(s):
        for x in range(s):
            if x == y:
                print('*', end='')
            elif x + y == s - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()


# Display star
generate_star(10)


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Loops Containing Compound Conditional Expressions
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/102371db-78c6-4f00-8f6c-06ee99f88a01/DEV330x-2_2d_conditionals_in_loo.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/d295efa9-b1cf-4516-879c-603d2d44251f/DEV330x-2_2d_conditionals_in_loops.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# Compound conditional expressions utilizing Boolean logic can be nested within loops. This will allow you to write versatile and flexible code. You can also use the `break` and `continue` statements within nested compound conditionals.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# In the following examples, you will explore the versatility of using compound conditionals inside loops.

# ### Finding the largest even number in a list

# In[40]:


lst = [102, 34, 55, 166, 20, 67, 305]

# Nesting a compound conditional in a for loop

largest = 0

for num in lst:
    # test if num is even and greater than largest
    if((largest < num) and (num % 2 == 0)):
        largest = num

print("Largest even number in the list is: ", largest)


# ### Counting within ranges
# In this example, you are given a list containing ages of 100 people. The code will count the number of children (younger than 13), the number of teenagers (from 13 through 19), the number of young adults (from 20 through 30), and the number of adults (older than 30).

# In[41]:


# Ages of 100 people
ages = [86, 38, 30, 19, 29, 6, 95, 22, 23, 82, 39, 73, 30, 98, 5, 68, 57, 34, 35, 81, 54, 77, 29, 75, 83, 14, 88, 7, 8, 32, 93, 76, 42, 1, 32, 70, 70, 3, 34, 52, 44, 41, 7, 77, 73, 97, 34, 13, 33, 54, 8, 82, 21, 55, 72, 41, 34, 98, 72, 73, 24, 55, 50, 63, 38, 92, 43, 68, 52, 68, 69, 51, 19, 24, 35, 55, 74, 47, 8, 19, 69, 12, 96, 96, 11, 30, 97, 73, 22, 25, 19, 85, 37, 68, 39, 76, 73, 18, 45, 42]

# Initial count
children = 0
teens = 0
young_adults = 0
adults = 0

# Nesting compound conditionals within a for loop
for age in ages:
    if(age <= 12):
        children = children + 1
    elif((age >= 13) and (age <= 19)):
         teens = teens + 1
    elif((age >= 20) and (age <= 30)):
         young_adults = young_adults + 1
    elif(age > 30):
         adults = adults + 1
            
print("Number of children: ", children)
print("Number of teens: ", teens)
print("Number of young_adults: ", young_adults)
print("Number of adults: ", adults)


# ### Prompting for specific input
# You can use compound conditionals to test whether user input is valid. The compound conditional statement can be nested within a loop to continuously prompt for input until a valid entry is provided.

# In[42]:


# Prompt the user for a number between 50 and 60

# Using infinite loop and break
while True:
    x = int(input("Enter a number between 50 and 60: "))
    if ((x >= 50) and (x <= 60)):
        print("Thank you!")
        break
    


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# 
# ## Loops Containing Compound Conditional Expressions
# 

# ### Counting specific numbers

# In[46]:


# [ ] Complete the following program to count the number of even positive numbers, odd negative numbers, and zeros in `lst`

lst = [9, 0, -2, -4, -5, 2, -15, 6, -65, -7]

ep = 0
on = 0
z = 0

for x in lst:
    if x == 0:
        z += 1    
    elif x%2 == 0 and x > 0:
        ep += 1
    elif x%2 != 0 and x < 0:
        on += 1

#TODO: Count even_positives, odd_negatives, and zeros
            
print("Number of even positives:", ep)
print("Number of odd negatives:", on)
print("Number of zeros:", z)


# ### Counting characters

# In[51]:


# [ ] Write a program to count the number of punctuation marks (. , ? ! ' " : ;) in `s`
s = "Once you eliminate the impossible, whatever remains, no matter how improbable, must be the truth." # Sherlock Holmes (by Sir Arthur Conan Doyle, 1859-1930)
p = 0
for x in s:
    if not(x.isalnum()) and x != ' ':
        p += 1
        
print(p)


# ### User input

# In[53]:


# [ ] Write a program to prompt the user for an odd positive number; use an infinite  loop and a `break` statement.
while 1:
    i = int(input())
    if i > 0 and i%2 != 0:
        break
print(i)

