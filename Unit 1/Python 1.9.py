#!/usr/bin/env python
# coding: utf-8

# # Section 1.9
# ## String Formatting and the 'in' Keyword
# - input() - gathering user input  
# - print() formatting   
# - Quotes inside strings 
# - Boolean string tests methods   
# - **String formatting methods**  
# - **Formatting string input()**  
# - **Boolean `in` keyword**  
# 
# -----
# 
# ### Student will be able to
# - Gather, store and use string `input()`  
# - Format `print()` output  
# - Test string characteristics  
# - **Format string output**  
# - **Search for a string in a string**  

# ## Concept: String Formatting Methods
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/693e416c-ab73-4387-a0d2-5a47668ae4de/Unit1_Section2-4-String-Format_Methods.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/693e416c-ab73-4387-a0d2-5a47668ae4de/Unit1_Section2-4-String-Format_Methods.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# The following methods are applied to string objects:
# - **.capitalize()** - capitalizes the first character of a string
# - **.lower()** - all characters of a string are made lowercase
# - **.upper()** - all characters of a string are made uppercase
# - **.swapcase()** - all characters of a string are made to switch case upper becomes lower and vice versa  
# - **.title()** - each 'word' separated by a space is capitalized

# ### Examples

# In[5]:


print("ms. Browning is in her office.".capitalize())


# In[3]:


fav_color = "green"
print(fav_color.capitalize(), fav_color, fav_color,"and", fav_color.upper()+"!")


# ## Task 1 (multi-part)
# - [ ] Format with `.capitalize(), .lower(), .upper(), .swapcase()`
# > **Note:** Use **print()**

# In[4]:


# [ ] get input for a variable, fav_food, that describes a favorite food
fav_food = input("What is favorite food?")
# [ ] display fav_food as ALL CAPS, used in a sentence
print(fav_food.upper(),"is a food.")
# [ ] dispaly fav_food as all lower case, used in a sentence
print(fav_food.lower(),"is a food.")
# [] display fav_food with swapped case, used in a sentence
print(fav_food.swapcase(),"is a food.")
# [] display fav_food with capitalization, used in a sentence
print(fav_food.capitalize(),"is not a food.")


# In[5]:


fav_color = "Forest Green"
# [] display the fav_color variable as upper, lower, swapcase, and capitalize formatting in a single print() statement
print(fav_color.upper(),fav_color.lower(),fav_color.swapcase(),fav_color.capitalize())


# ## Concept: Formatting String Input()
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/460107d8-5d62-432e-924b-a3c779b2e5c5/Unit1_Section2-4-Input-String_Formatting.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/460107d8-5d62-432e-924b-a3c779b2e5c5/Unit1_Section2-4-Input-String_Formatting.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# When storing input, sometimes a specific format is needed and formatting is applied to the **`input()`** function.
# > **Note:** this technique overwrites the original user input in the variable with the formatted value 

# ### Example

# In[ ]:


# review and run code - test a capitalized color input
fav_color = input('What is your favorite color?: ').lower()
print(fav_color)


# ## Task 2  
# ### [ ] format &nbsp; ` input()` with ` .upper()`

# In[6]:


# [] input variable fav_color as upper
fav_color = input("What is fav color?").upper()
# [] print fav_color
print(fav_color)


# ## Concept: Boolean `in` Keyword 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ef7e8587-8ce6-48a4-9a2f-fb0a09db287f/Unit1_Section2-4-Boolean-in.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ef7e8587-8ce6-48a4-9a2f-fb0a09db287f/Unit1_Section2-4-Boolean-in.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# The **`in`** keyword can be used as a simple search returning **`True`** or **`False`** indication if a string is included in a target sequence.  
# ### Comparing strings is case sensitive
# `'Hello'` is not the same as `'hello'`  

# ### Examples

# In[8]:


# review and run code to test if a string is to be found in another string
menu = "salad, pasta, sandwich, pizza, drinks, dessert"
print('pizza' in menu)


# In[9]:


# review and run code to test case sensitive examples 
greeting = "Hello World!"
print("'hello' in greeting = ",'hello' in greeting)
print("'Hello' in greeting = ", 'Hello' in greeting)


# Example below: **Remove case sensitivity from a string comparison**

# In[7]:


# review and run code to test removing case sensitivity from a string comparison
greeting = "Hello World!"
print("'hello' in greeting = ",'hello' in greeting)
print("'Hello' in greeting = ", 'Hello' in greeting)
print("'hello' in greeting if lower used = ", 'hello'.lower() in greeting.lower())


# ## Task 3: multi-part
# **[ ] Add code below** testing the **`menu`** string variable for `'pizza'`, `'soup'`, and `'dessert'` using keyword **`in`**
# - Print each test on a separate line
# - Print a description for each test (e.g. - "`Pizza in menu = True`")

# In[11]:


# [] print 3 tests, with description text, testing the menu variable for 'pizza', 'soup' and 'dessert'
menu = "salad, pasta, sandwich, pizza, drinks, dessert"
print("Pizza in menu =","pizza" in menu)
print("Soup in menu =","soup" in menu)
print("Dessert in menu =","dessert" in menu)


# ## Program: What is on the menu?
# ### [ ] Create a program where a user can check if an item is on the menu
# - store the user response in a variable menu_ask
# - use the menu from above and add some additional items
# - the program should be able to ignore case mismatch so that "hello" is found in "Hello World!"

# In[12]:


# Create a program where the user supplies input to search the menu
menu = "salad, pasta, sandwich, pizza, drinks, dessert, edible substance, soup, food".lower()
menu_ask = input("What do you want?").lower()
if menu_ask in menu:
    print("That is on our menu.")
else:
    print("Sorry, that is not on our menu.")


# ### [ ] Challenge: Add to the menu
# - print the current menu
# - get user input for add_item variable
# - new_menu use string addition to add add_item to menu
# - print the new_menu
# testing
# - add a cell below add menu
# - check if an item is on the menu, check for previous items and the item you added

# In[3]:


# add to menu
print("Our menu contains:", menu + ".")
newItem = input("What would you like to add? ").lower()
menu = menu + ", " + newItem
print("Our menu contains:", menu + ".")


# In[7]:


# Testing Add to Menu - create user input to search for an item on the new menu
menu_ask = " "
while menu_ask != "end":
    menu_ask = input("What do you want? ").lower()
    if menu_ask in menu:
        print("That is on our menu.")
    else:
        print("Sorry, that is not on our menu.")


# ## Task 4: Fix the error

# In[9]:


# [ ] fix the error
paint_colors = "red, blue, green, black, orange, pink"
print('Red in paint colors = ', "red" in paint_colors)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
