#!/usr/bin/env python
# coding: utf-8

# # Section 3.4  
# ## Conditionals, elif, and Casting  
# - **Conditionals: `elif`**
# - **Casting**  
# - Basic math operators  
# 
# -----
# 
# ### Student will be able to
# - **Code more than two choices using `elif`** 
# - **Gather numeric input using type casting**  
# - Perform subtraction, multiplication and division operations in code 
# 

# ## Concept: Conditional `elif`
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/a2ac5f4b-0400-4a60-91d5-d350c3cc0515/Unit1_Section5.1-elif.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/a2ac5f4b-0400-4a60-91d5-d350c3cc0515/Unit1_Section5.1-elif.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### A little review  
# - **`if`** means "**if** a condition exists then do some task." **`if`** is usually followed by **`else`**.  
# - **`else`** means "**or else** after we have tested **if**, then do an alternative task".  
# 
# When there  is a need to test for multiple conditions there is&nbsp; **`elif`**.
# - **`elif`**&nbsp; statement follows &nbsp;**`if`**, and means **"else, if "** another condition exists do something else
# - **`elif`**&nbsp; can be used many times
# - **`else`**&nbsp; is used after the last test condition (**`if`** or **`elif`**)
# 
# #### In pseudo code  
# **If** it is raining bring an umbrella  
# or **Else If** &nbsp;(`elif`) it is snowing bring a warm coat  
# or **Else** go as usual  
# 
# Like **`else`**, the **`elif`** only executes when the previous conditional is False.

# ### Examples

# In[1]:


# [ ] review the code then run testing different inputs
# WHAT TO WEAR
weather = input("Enter weather (sunny, rainy, snowy): ") 

if weather.lower() == "sunny":
    print("Wear a t-shirt")
elif weather.lower() == "rainy":
    print("Bring an umbrella and boots")
elif weather.lower() == "snowy":
    print("Wear a warm coat and hat")
else:
    print("Sorry, not sure what to suggest for", weather)


# In[2]:


# [ ] review the code then run testing different inputs
# SECRET NUMBER GUESS
secret_num = "2"

guess = input("Enter a guess for the secret number (1-3): ")

if guess.isdigit() == False:
    print("Invalid: guess should only use digits")
elif guess == "1":
    print("Guess is too low")
elif guess == secret_num:
    print("Guess is right")
elif guess == "3":
    print("Guess is too high")
else:
    print(guess, "is not a valid guess (1-3)")


# ## Task 1 (program): Shirt Sale
# ### Complete the program using `if, elif, else`
# - Get user input for variable size (S, M, L)
# - Reply with each shirt size and price (Small = \$ 6, Medium = \$ 7, Large = \$ 8)
# - If the reply is other than S, M, L, give a message for not available
# - *Optional*: Add additional sizes

# In[3]:


# [ ] code and test SHIRT SALE
size = input("What size shirt? (S, M, L) ")
if size == "S":
    print("$6")
elif size == "M":
    print("$7")
elif size == "L":
    print("$8")


# ## Concept: Casting
# Casting is the conversion from one data type to another, such as converting from **`str`** to **`int`**.
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/4cbf7f96-9ddd-4962-88a8-71081d7d5ef6/Unit1_Section5.1-casting-input.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/4cbf7f96-9ddd-4962-88a8-71081d7d5ef6/Unit1_Section5.1-casting-input.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### `int()`
# The **`int()`** function can convert strings that represent whole counting numbers into integers and strip decimals to convert float numbers to integers.
# - `int("1") = 1` &nbsp; the string representing the integer character `"1"`, cast to a number 
# - `int(5.1) = 5` &nbsp; the decimal (float), `5.1`, truncated into a non-decimal (integer)  
# - `int("5.1") = ValueError` &nbsp; `"5.1"` isn't a string representation of integer, `int()` can cast only strings representing integer values   
# 

# ### Example

# In[4]:


weight1 = '60' # a string
weight2 = 170 # an integer
# add 2 integers
total_weight = int(weight1) + weight2
print(total_weight)


# ## Task 2: Casting with `int()` & `str()`

# In[8]:


str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# [ ] Add the 3 numbers as integers and print the result
print(int(str_num_1) + int(str_num_2) + int_num_3)


# In[10]:


str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# [ ] Add the 3 numbers as test strings and print the result
print(str_num_1 + str_num_2 + str(int_num_3))


# ### Task 2 continued...
# ## Program: Adding using `int` casting
# - **[ ]** initialize **`str_integer`** variable to a **string containing characters of an integer** (quotes)   
# - **[ ]** initialize **`int_number`** variable with an **integer value** (no quotes)
# - **[ ]** initialize **`number_total`** variable and **add int_number + str_integer** using **`int`** casting
# - **[ ]** print the sum (**`number_total`**)

# In[13]:


# [ ] code and test: adding using int casting
str_integer = "2"
int_number = 10
number_total = int(str_integer) + int_number
print(number_total)


# ## Concept: Casting Numeric Input

# ### Example

# In[14]:


# [ ] review and run code
student_age = input('enter student age (integer): ')
age_next_year = int(student_age) + 1
print('Next year student will be',age_next_year)


# In[1]:


# [ ] review and run code
# cast to int at input
student_age = int(input('enter student age (integer): '))

age_in_decade = student_age + 10

print('In a decade the student will be', age_in_decade)


# ## Task 3 (program): Adding calculator
# - Get input of 2 **integer** numbers 
# - Cast the input and print the input followed by the result
#   - Output Example: **`9 + 13 = 22`**  
# 
# Optional: Check if input .isdigit() before trying integer addition to avoid errors in casting invalid inputs.

# In[1]:


# [ ] code and test the adding calculator
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
total = num1 + num2
print(num1, "+", num2, "=", total)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
