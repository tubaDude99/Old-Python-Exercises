#!/usr/bin/env python
# coding: utf-8

# # Module 3 Required code  
#   
# 
# ## Note: Students of Dev330x on edX
# 
# > ### It is required to submit your required code for Module 3 within the edX course   
# > The completed code must be copied from the cell below and pasted in to the edX required code page at the end of Module 3 in the course "Introduction to Python: Creating Scalable, Robust, Interactive Code" on edX.  
# >  
# > **REQUIREMENTS**  
# > Submit all of the code in working order, you will only be graded on correct completion tasks below:
# - Use the inventory dictionary in a program that asks the user for a UPC number, description, unit price, quantity in stock.  
# - If the item already exists in the inventory, the information is updated, and your program should display a message that it is updating the entry.  
# - If the item does NOT exists in the inventory, a new dictionary entry is created, and your program should display a message that it is creating a new entry.  
# - Use try/except in the program. 
# - **use the following required keywords & functions:** `try`, `except`, `int`, `input`,`.format`

# <font size="6" color="#B24C00"  face="verdana"> <B>Required Code Module 3</B></font>  
# 
# ### Complete the Required Code in the Jupyter Notebook Required_Code_Mod03 and then paste into edX code submission page   
# 
# This is the same code assignment located as **Task 7,  Dictionary: Updating/adding an item** in 3-3.5_Mod03_Practice.ipynb
# 
# ## Dictionary: Updating/adding an item  
# 

# In[ ]:


# [ ] Use the `inventory` dictionary in a program that asks the user for a 
#     UPC number, description, unit price, quantity in stock.
# If the item already exists in the inventory, the information is updated, 
#     and your program should display a message that it is updating the entry.
# If the item does NOT exists in the inventory, a new dictionary entry is created, 
#     and your program should display a message that it is creating a new entry.
# Use try/except in the program.


# test cases

# For an existing item
'''
Enter UPC number: 839529
Enter item description: TOMATOS 1LB
Enter unit price: 1.55
Enter item quantity: 21
Existing item, updating: ['TOMATOS 1LB', 1.29, 25]

  UPC   | Description       |  Unit Price  |  Quantity 
-------------------------------------------------------
839529  | TOMATOS 1LB       |         1.55 |      21.00
'''

# For a new item
'''
Enter UPC number: 29430
Enter item description: ORANGE 1LB
Enter unit price: 0.99
Enter item quantity: 40
New item, creating ORANGE 1LB

  UPC   | Description       |  Unit Price  |  Quantity 
-------------------------------------------------------
29430   | ORANGE 1LB        |         0.99 |      40.00
'''

inventory = {847502: ['APPLES 1LB', 1.99, 50], 847283: ['OLIVE OIL', 10.99, 100], 839529: ['TOMATOS 1LB', 1.29, 25], 483946: ['MILK 1/2G', 3.45, 35], 493402: ['FLOUR 5LB', 2.99, 40], 485034: ['BELL PEPPERS 1LB', 1.35, 28], 828391: ['WHITE TUNA', 1.69, 100], 449023: ['CHEESE 1/2LB', 4.99, 15]}


# get UPC from user, handling cases where the input is invalid with try/except
#TODO: Your code goes here

# display message, either "updating" or creating" and then item is being updated display the `value` being updated
#TODO: Your code goes here

# update dictionary entry
#TODO: Your code goes here

# print header including 
# HINT: look at the testing samples shown in comments above for new item and for existing item
#TODO: Your code goes here

# print actual data from the dictionary (See Hint above)
#TODO: Your code goes here


# --Completed--

inventory = {847502: ['APPLES 1LB', 1.99, 50], 847283: ['OLIVE OIL', 10.99, 100], 839529: ['TOMATOS 1LB', 1.29, 25], 483946: ['MILK 1/2G', 3.45, 35], 493402: ['FLOUR 5LB', 2.99, 40], 485034: ['BELL PEPPERS 1LB', 1.35, 28], 828391: ['WHITE TUNA', 1.69, 100], 449023: ['CHEESE 1/2LB', 4.99, 15]}

# get UPC from user, handling cases where the input is invalid (i.e. "word")
try:
    UPC = int(input("Enter UPC number: "))
    description = input("Enter item description: ")
    price = float(input("Enter unit price: "))
    quantity = float(input("Enter item quantity: "))
except ValueError:
    print("Cannot convert {} to int".format(type(UPC)))


# display updating/creating message
if UPC in inventory:
    print("Existing item, updating: {:}".format(inventory[UPC]))
else:
    print("New item, creating {:}".format(description))

# update dictionary entry
inventory[UPC] = [description, price, quantity]

# print the new updated/created info:

# print header
print()
print("{:^7s} | {:<17s} | {:^12s} | {:^10s}".format("UPC", "Description", "Unit Price", "Quantity"))
print(55 * '-')

# print actual info
print("{:<7d} | {:<17s} | {:>12.2f} | {:>10.2f}".format(UPC, inventory[UPC][0], inventory[UPC][1], inventory[UPC][2]))


# ### Test your graded code  
# Use the supplied data and make sure the output running code above looks the same
# 
# Complete the Required Code in the Jupyter Notebook Required_Code_Mod03 and then paste into edX code submission page
# #### Test 1  
# ```  
# Enter UPC number: 839529
# Enter item description: TOMATOS 1LB
# Enter unit price: 1.55
# Enter item quantity: 21
#  
# ```  
# #### Expected Result Test 1  
# ```  
# Existing item, updating: ['TOMATOS 1LB', 1.29, 25]
# 
#   UPC   | Description       |  Unit Price  |  Quantity 
# -------------------------------------------------------
# 839529  | TOMATOS 1LB       |         1.55 |      21.00
# ```  
# 
# #### Test 2   
# ```  
# Enter UPC number: 29430
# Enter item description: ORANGE 1LB
# Enter unit price: 0.99
# Enter item quantity: 40
# ```  
# #### Expected Result Test 2  
# ```  
# New item, creating ORANGE 1LB
# 
#   UPC   | Description       |  Unit Price  |  Quantity 
# -------------------------------------------------------
# 29430   | ORANGE 1LB        |         0.99 |      40.00
# ```  
