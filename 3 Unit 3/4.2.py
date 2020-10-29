#!/usr/bin/env python
# coding: utf-8

# # Section 4.2: Variable Scope
# * def
# * global
# 
# ### Students will be able to:
# * Define local variables
# * Read and modify the values of local variables
# * Identify the scope of a variable
# * Define global variables
# * Read and modify the values of global variables from local scopes

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Local Variables
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ae748781-911c-47f3-bd06-75d5305379f0/DEV330x-4_2a_local_variables.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/1a74bf33-19f2-4e5e-8448-a42ec8040b47/DEV330x-4_2a_local_variables.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# A variable in Python lives within a scope; the scope determines how the variable is accessed and when it is deleted. A variable scope is determined by the place where it is initially assigned. There are two types of scopes: local and global. Parameters passed to a function and variables assigned within it are within the local scope of the function and are called local variables; variables assigned outside all functions in a module are within the global scope of the module and are called global variables. 
# 
# Local scopes are created when a function is called, and destroyed when the function return to its caller. This means that you might have several local scopes that have different local variables within them. These local variables can be accessed and changed within their own local scopes; however, they cannot interact with variables from other local scopes and they cannot be accessed from the global scope. This is important because it allows you to use the same variable name in different functions without worrying about name conflicts or the collision of variables.
# 
# The concept of a local scope guides you to think about functions as black boxes that can interact with your code only through arguments and returned values. When developing a function, you do not have to worry about a variable name being used in another function because you know that each will be local within its own function and can be accessed only from within that function.
# 
# Generally speaking:
# * Local variables cannot be read or modified from the global scope
# * Local variables cannot be read or modified from other local scopes
# * The same variable name can be used in different functions without causing a conflict

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# In the following examples, functions compute the areas and volumes of different geometric figures. The variable name `area` will be used in all functions to demonstrate the concepts of local scope and global scope. The demonstrated concepts also apply to other data types (such as lists and strings).

# ### Local variables cannot be read or modified from the global scope

# In[1]:


# Compute the area of a square
def square_area (side):
    # area is a local variable in square_area
    area = side ** 2
    return area


# Global scope
square_area(2)

# area is not within scope anymore and cannot be
# accessed from this global scope
print(area)


# ### Local variables cannot be read or modified from other local scopes
# 
# A local variable in one function cannot be accessed from another function.

# In[2]:


# Compute the area of a square
def square_area (side):
    # area is a local variable in square_area
    area = side ** 2
    return area

# Compute the volume of a cube
def cube_volume (side):
    # cube volume = area of base X side
    volume = area * side # area is not defined within this scope
    return volume

# Global scope
s = 2
square_area(s)
# area was deleted when the local scope of square_area was destroyed
cube_volume(s)


# ### The same variable name can be used in different functions without causing a conflict

# In[3]:


# Compute the area of a square
def square_area (side):
    # area is a local variable in square_area
    # area does not conflict with the variable area in rectangle_area
    area = side ** 2
    print("square area =", area)

# Compute the area of a rectangle
def rectangle_area (length, width):
    # area is a local variable in rectangle_area
    # area does not conflict with the variable area in square_area
    area = length * width
    print("rectangle area =", area)

# Global scope
square_area(2)
rectangle_area(2, 3)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Local Variables

# ### Fix the Errors
# 
# Return to the examples that generated errors and fix them so they function as expected.

# In[5]:


# [ ] Fix the program below so it displays the area of a square with a side = 2

# Compute the area of a square
def square_area (side):
    # area is a local variable in square_area
    area = side ** 2
    return area

# Global scope
area = square_area(2)

# area is not within scope anymore and cannot be
# accessed from this global scope
print(area)


# In[7]:


# [ ] Fix the program below so it displays the area of a square with side = 2
# and the volume of a cube with side = 2

# Compute the area of a square
def square_area (side):
    # area is a local variable in square_area
    area = side ** 2
    return area

# Compute the volume of a cube
def cube_volume (side):
    # cube volume = area of base X side
    volume = area * side # area is not defined within this scope
    return volume

# Global scope
s = 2
print(square_area(s))
# area was deleted when the local scope of square_area was destroyed
print(cube_volume(s))


# ### Currency Converter
# 
# The same name for arguments and local variables can be used across different functions.

# In[9]:


# [ ] The program below converts US Dollars to Euros, British Pounds, and Japanese Yen
# Complete the functions USD2EUR, USD2GBP, USD2JPY so they all return the correct value

def USD2EUR(amount):
    """
    Convert amount from US Dollars to Euros.
    
    Use 1 USD = 0.831467 EUR
    
    args:
        amount: US dollar amount (float)
        
    returns:
        value: the equivalent of amount in Euros (float)
    """
    value = amount * 0.831467
    return value

def USD2GBP(amount):
    """
    Convert amount from US Dollars to British Pounds.
    
    Use 1 USD = 0.739472 GBP
    
    args:
        amount: US dollar amount (float)
        
    returns:
        value: the equivalent of amount in British Pounds (float)
    """
    value = amount * 0.739472
    return value

def USD2JPY(amount):
    """
    Convert amount from US Dollars to Japanese Yen.
    
    Use 1 USD = 112.656 JPY
    
    args:
        amount: US dollar amount (float)
        
    returns:
        value: the equivalent of amount in Japanese Yen (float)
    """
    value = amount * 112.656
    return value

def main():
    amount = float(input("Enter amount in USD: $"))
    
    # In Euros
    eur = USD2EUR(amount)
    
    # In British Pounds
    gbp = USD2GBP(amount)
    
    # In Japanese Yen
    jpy = USD2JPY(amount)
    
    print("${:.2f} USD = {:.2f} EUR, {:.2f} GBP, {:.2f} JPY".format(amount, eur, gbp, jpy))
    
if __name__ == '__main__':
    main()


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# ## Isolated Local Scopes
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/32b27ec3-56df-4af4-8e65-8786aba5154c/DEV330x-4_2b_isolated_local_scop.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/5f0345c9-6b18-41d4-b820-3e7afdc4abe9/DEV330x-4_2b_isolated_local_scopes.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# When a function calls a subfunction, the current variables within the function scope are stored in memory, and another temporary local scope is created to accommodate the subfunction variables. The temporary local scope is destroyed when the subfunction returns; at that point, the original local scope becomes active again.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# In this example, the function `area_diff` computes the area difference between a rectangle and a square. The `area_diff` function calls `square_area` and `rectangle_area`. All three functions use a local variable named `area` without any conflict. As you can see, using the same variable name in all three functions does not create an issue.
# 
# When `area_diff` calls `square_area`, the current local variables within `area_diff` are stored in a location in memory called the _stack_, then a new local scope is created with new variables for `square_area`. The local scope of `area_diff` is still alive; however, it's inaccessible until `square_area` returns. Both `area_diff` and `square_area` use the variable `area`; however, the two variables live in two different local scopes and cannot affect each other. After `square_area` returns, the local scope of `area_diff` becomes active again until calling `rectangle_area`, and the cycle repeats.
# 
# In summary, a variable called `area` is used in all three functions without any conflict. The content of the three variables are kept separate because they belong to three different local scopes.

# In[10]:


# Compute the area of a square
def square_area (side):
    # area is a local variable in square_area
    # area does not conflict with the variable area in rectangle_area or area_diff
    area = side ** 2
    return area

# Compute the area of a rectangle
def rectangle_area (length, width):
    # area is a local variable in rectangle_area
    # area does not conflict with the variable area in square_aream or area_diff
    area = length * width
    return area

# Compute the area difference between a square and a rectangle
def area_diff (side, length, width):
    # square area
    area1 = square_area(side) # defines area in its local scope
    
    # rectangle area
    area2 = rectangle_area(length, width) # defines area in its local scope
    
    # area difference 
    area = area2 - area1 # area is local in area_diff local scope
    
    return area

# Call the area_diff function
print("Area difference = ", area_diff(2, 2, 3))


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Isolated Local Scopes
# 

# ### Currency Converter
# The same variable name can be used across different functions, even when the functions call each other.

# In[13]:


# [ ] The program below converts US Dollars to British Pounds. However, the conversion rate is unknown
# Complete the functions USD2EUR, EUR2GBP, and USD2GBP so they all return the correct value
# You should use USD2EUR and EUR2GBP in USD2GBP, do not try to find out the conversion rate

def USD2EUR(amount):
    """
    Convert amount from US Dollars to Euros.
    
    Use 1 USD = 0.831467 EUR
    
    args:
        amount: US dollar amount (float)
        
    returns:
        value: the equivalent of amount in Euros (float)
    """
    #TODO: Your code goes here
    return(amount * 0.831467)

def EUR2GBP(amount):
    """
    Convert amount from Euros to British Pounds.
    
    Use 1 EUR = 0.889358 GBP
    
    args:
        amount: Euros amount (float)
        
    returns:
        value: the equivalent of amount in GBP (float)
    """
    #TODO: Your code goes here
    return(amount * 0.889358)

def USD2GBP(amount):
    """
    Convert amount from US Dollars to British Pounds.
    
    The conversion rate is unknown, you have to use USD2EUR and EUR2GBP
    
    args:
        amount: US dollar amount (float)
        
    returns:
        value: the equivalent of amount in British Pounds (float)
    """
    #TODO: Your code goes here
 
    return(EUR2GBP(USD2EUR(amount)))

def main():
    amount = float(input("Enter amount in USD: $"))
    
    # In British Pounds
    gbp = USD2GBP(amount)
    
    print("${:.2f} USD = {:.2f} GBP".format(amount, gbp))
    
if __name__ == '__main__':
    main()


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Global Variables
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7047d23a-65ea-4be5-a25f-fab1c8aff51b/DEV330x-4_2c_global_variables.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/01cb5523-3b31-4eb7-9e95-09f51f7f464b/DEV330x-4_2c_global_variables.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# A global variable is assigned outside all functions and lives within the global scope of the module. It exists from the time of its assignment until the program ends. Global variables are visible to all functions within the module and can be used within their different local scopes. Additionally, global variables can be used by expressions in the global scope. The value of a global variable can be changed from the global scope, and can also be modified from a local scope using the `global` statement (i.e. `global x = 4`). If (`global`) was not used, a local variable would be defined instead, and any changes to this new variable will not affect the global variable that bears the same name.
# 
# Global variables are highly discouraged because they make your code hard to understand and follow. Imagine that 20 functions written by different developers all change one global variable; tracking the functionality of the program will be very challenging. Global variables are covered in this lesson because some developers use them for very specialized applications when there are no alternatives. You can write very complicated Python scripts without using global variables. It is OK, however, to use constant global variables that are accessible from all functions but will not (and cannot) be changed.
# 
# Generally speaking:
# * Global variables are accessible from local scopes
# * Global variables can be changed from the global scope 
# * Global variables can be changed  from a local scope using the `global` statement
# * If a local variable shares the same name with a global variable, changes in the local will not affect the global

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# In the following examples, you will see how to define, read, and modify global variables.

# ## Global Variables
# 
# ### Global variables are accessible from local scopes

# #### Numeric variables

# In[14]:


# Global variable
pi = 3.14

# Compute the area of a circle
def circle_area (radius):
    # pi is accessible from this local scope
    area = pi * radius ** 2
    return area

# Global scope
a = circle_area(4)
print("circle area =", a)


# #### String variables

# In[15]:


# Global variable
vowels = 'AaEeIiOoUiYy'

# Count the number of vowels in a sentence
def count_vowels(sentence):
    # vowels is accessible from this local scope
    count = 0
    for c in sentence:
        if c in vowels:
            count = count + 1
    return count

# Global scope
s = 'Monty Python'
print('Number of vowels in "{:s}" = {:d}'.format(s, count_vowels(s)))


# ### Global variables can be changed from a local scope
# When the value of a global variable is changed from a local scope, it stays changed even after the local scope has been destroyed.

# #### Numeric variables

# In[16]:


# Global variable
pi = 3.14

# Compute the area of a circle
def circle_area (radius):
    # Define pi as a global variable in this scope
    global pi 
    pi = 3.14159265359 # More accurate pi
    area = pi * radius ** 2
    return area

# Global scope
print("pi =", pi)
a = circle_area(4)
print("More accurate circle area =", a)
print("Updated pi =", pi) # Global variable pi changed in circle_area


# #### String variables

# In[18]:


# String global variable
planet = 'Mercury'

# function to change the current planet
def planet_change(new_planet):
    # Define planet as a global variable in this scope
    global planet
    planet = new_planet
   
# Global scope
print("Planet =", planet)
planet_change('Mars')
print("Planet =", planet)


# ### Assigning a value to a global variable in a local scope without `global`
# Changes to a local variable sharing the same name as a global variable are not reflected in the global variable.

# #### Numeric variables

# In[19]:


# Global variable
pi = 3.14

# Compute the area of a circle
def circle_area (radius):
    # Assigning a value to pi without (global) makes it a local variable
    pi = 3.14159265359 # more accurate pi
    area = pi * radius ** 2
    return area

# Global scope
print("pi =", pi)
a = circle_area(4)
print("More accurate circle area =", a)
print("Unchanged pi =", pi) # Global pi didn't change


# #### String variables

# In[20]:


# String global variable
planet = 'Mercury'

# Function to change the current planet
def planet_change(new_planet):
    planet = new_planet # planet is a local variable
   
# Global scope
print("Planet = ", planet)
planet_change('Mars')
print("Planet = ", planet)


# ### Global variables can be changed from the global scope

# #### Numeric variables

# In[21]:


# Global variable
pi = 3.14

# Compute the area of a circle
def circle_area (radius):
    # pi is accessible from this local scope
    area = pi * radius ** 2
    return area

# Global scope
# pi is changed before it is used in circle_area
pi = 0
a = circle_area(4)
print("pi =", pi)
print("Wrong circle area =", a)


# #### String variables

# In[22]:


# String global variable
planet = 'Mercury'

# Function to change the current planet
def planet_change(new_planet):
    planet = new_planet # planet is a local variable
   
print("Planet = ", planet)
planet_change('Mars')
print("Planet = ", planet) # Global variable (planet) did not change
planet = "Earth" # Changing global variable (planet)
print("Planet = ", planet)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# 
# ## Global Variables

# ### Currency Converter

# In[25]:


# [ ] The following program converts an amount from US Dollars to Indian Rupees using the XCHANGE_RATE variable
# Complete the function USD2INR so it performs the conversion

XCR = 63.6856 # = 1 USD

def USD2INR(amount):
    """
    Convert amount from US Dollars to Indian Rupees.
    
    Use XCHANGE_RATE
    
    args:
        amount: US dollar amount (float)
        
    returns:
        value: the equivalent of amount in Indian Rupees (float)
    """
    value = amount * XCR
    return value

print("Current exchange rate $1 USD = {} INR".format(XCR))
amount = 220 #USD
inr = USD2INR(amount)
print("${} = {}".format(amount, inr))


# In[27]:


# [ ] The following program calculates the equivalent of $220 USD in Indian Rupees, 
# then updates the exchange rate and performs the conversion again
# Complete the functions USD2INR and change_rate so they function according to the specifications below

XCHANGE_RATE = 63.6856 # = 1 USD

def USD2INR(amount):
    """
    Convert amount from US Dollars to Indian Rupees.
    
    Use XCHANGE_RATE
    
    args:
        amount: US dollar amount (float)
        
    returns:
        value: the equivalent of amount in Indian Rupees (float)
    """
    value = amount * XCHANGE_RATE
    return value

def change_rate():
    """
    Change the exchange rate to 63.6782
    
    args:
        None
    
    returns:
        None
    """
    global XCHANGE_RATE
    XCHANGE_RATE = 63.6782
    
print("Current exchange rate $1 USD = {} INR".format(XCHANGE_RATE))
amount = 220 #USD
inr = USD2INR(amount)
print("${} = {}".format(amount, inr))

print()
change_rate()
print("After changing the exchange rate $1 USD = {} INR".format(XCHANGE_RATE))
inr = USD2INR(amount)
print("${} = {}".format(amount, inr))


# ### Flip

# In[29]:


# [ ] In the following program, the function `flip()` is designed to reverse the order of the elements in NUMBERS
# Fix the `UnboundLocalError` exception without changing the expression (NUMBERS = NUMBERS[-1:0:-1])

NUMBERS = [1, 2, 3, 4, 5, 6]

def flip():
    global NUMBERS
    NUMBERS = NUMBERS[-1::-1]

print("Before flipping, NUMBERS =", NUMBERS)
flip()
print("After flipping, NUMBERS =", NUMBERS)

