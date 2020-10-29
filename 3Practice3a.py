#!/usr/bin/env python
# coding: utf-8

# # Lab 3a
# ## Conditionals Practice
# 
# -----
# 
# ### Student will be able to
# - **Control code flow with `if`... `else` conditional logic**  
#   - Using Boolean string methods (`.isupper(), .isalpha(), startswith()...`)  
#   - Using comparision (`>, <, >=, <=, ==, !=`)  
#   - Using Strings in comparisons  

# ## `if else`
# 

# In[3]:


# [ ] input a variable: age as digit and cast to int
# if age greater than or equal to 12 then print message on age in 10 years 
# or else print message "It is good to be" age
age = int(input("How old are you? "))
if age >= 12:
    print("In 10 years you will be " + str(age + 10))
else:
    print("It is good to be " + str(age))


# In[7]:


# [ ] input a number 
# - if number is NOT a digit cast to int
# - print number "greater than 100 is" True/False
x = input()
if type(x) != int:
    x = int(x)
print(str(x) + " greater than 100 is " + str(x>100))


# ### Guessing a letter A-Z  
# **check_guess()** takes two string arguments: **letter and guess** (both expect single alphabetical character)   
#     - If guess is not an alpha character print invalid and return False
#     - Test and print if guess is "high" or "low" and return False
#     - Test and print if guess is "correct" and return True

# In[12]:


# [ ] create check_guess()
# call with test
def check_guess(letter,guess):
    if guess.isalpha() == False:
        print("invalid")
        return(False)
    elif guess == letter:
        print("correct")
        return(True)
    elif guess > letter:
        print("high")
        return(False)
    elif guess < letter:
        print("low")
        return(False)


# In[13]:


# [ ] call check_guess with user input
def check_guess(letter,guess):
    if guess.isalpha() == False:
        print("invalid")
        return(False)
    elif guess == letter:
        print("correct")
        return(True)
    elif guess > letter:
        print("high")
        return(False)
    elif guess < letter:
        print("low")
        return(False)
print(check_guess("b",input("What's your guess? ")))


# ### Letter Guess
# **Create letter_guess() function that gives the user three guesses**
# - Take a letter character argument for the answer letter
# - Get user input for letter guess  
# - Call check_guess() with answer and guess
# - End letter_guess if 
#     - check_guess() equals True, return True  
#     - or after 3 failed attempts, return False

# In[5]:


# [ ] create letter_guess() function, call the function to test
def check_guess(letter,guess):
    if guess.isalpha() == False:
        print("invalid")
        return(False)
    elif guess == letter:
        print("correct")
        return(True)
    elif guess > letter:
        print("high")
        return(False)
    elif guess < letter:
        print("low")
        return(False)
    
def letter_guess(answer):
    i = 0
    check = "b"
    while check != True and i < 3:
        check = check_guess(answer,input("What is your guess? "))
        i = i + 1
letter_guess("b")


# ### Pet Conversation
# **Ask the user for a sentence about a pet and then reply**  
# - Get user input in variable: about_pet
# - Using a series of **if** statements, respond with appropriate conversation
#   - Check if "dog" is in the string about_pet (sample reply "Ah, a dog")
#   - Check if "cat" is in the string about_pet
#   - Check if 1 or more animal is in string about_pet
# - No need for **else**'s
# - Finish by thanking for the story

# In[9]:


# [ ] complete pet conversation
about_pet = input("What kind of pet do you have? ").lower()
if "dog" in about_pet:
    print("Ah, a dog")
if "cat" in about_pet:
    print("Ah, a cat")
if "cat" in about_pet or "dog" in about_pet or "fish" in about_pet or "bird" in about_pet or "lizard" in about_pet:
    print("Ah, one or more animals")
print("Thank you for the story")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
