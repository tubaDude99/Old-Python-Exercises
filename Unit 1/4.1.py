#!/usr/bin/env python
# coding: utf-8

# # Section 4.1
# ## Nested Conditionals
# - Nested Conditionals  
# - Escape Sequence print formatting "\\"
# 
# -----
# 
# ### Student will be able to
# - Create nested conditional logic in code  
# - Format print output using escape "\\" sequence 

# ## Concept: Nested Conditionals
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/16ef1670-d6ca-4104-a923-9bdfd9c3a217/Unit1_Section6.1-nested-conditionals.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/16ef1670-d6ca-4104-a923-9bdfd9c3a217/Unit1_Section6.1-nested-conditionals.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Nested Conditionals
# **if**  
# **&nbsp;&nbsp;&nbsp;&nbsp;if**  
# **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if**  
# **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else**  
# **&nbsp;&nbsp;&nbsp;&nbsp;else**  
# **else**  
# 
# ### Making a sandwich
# Taking a sandwich order starts with sandwich choices:
# > **Cheese or Veggie special?**  
# If the response is **"Cheese"** "nest" a subquery:  
# >> **Manchego or Cheddar?**  
#   
#   
# |Nested &nbsp;**`if`**&nbsp; statement  flowchart  |
# | ------ | 
# | ![Image of sandwich order flowchart](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/flowchart_sandwich.png)   | 
# 

# ### Examples
# > ***TIP:*** click in input box before typing input 

# In[ ]:


# simplified example
# [ ] review the code then run and following the flowchart paths

# ***TIP:*** click in input box before typing

sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')

if sandwich_type.lower() == "c":
    # select cheese type
    cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
    
    if cheese_type.lower() == "c":
        print("Here is your Cheddar Cheese sandwich")
    else:
        print("Here is your Manchego Cheese sandwich") 

else:
    print("Here is your Veggie Special")


# In[1]:


# full example: handling some invalid input and elif statement
# [ ] review the code then run following the flowchart paths including **invalid responses** like "xyz123"

# ***TIP:*** click in input box before typing

print("Hi, welcome to the sandwich shop.  Please select a sandwich.")
sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
# select sandwich type sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
print()
    
if sandwich_type.lower() == "c":
    # select cheese type
    print("Please select a cheese.")
    cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
    print()
    
    if cheese_type.lower() == "c":
        print("Here is your Cheddar Cheese sandwich.  Thank you.")
    elif cheese_type.lower() == "m":
        print("Here is your Manchego Cheese sandwich.  Thank you.") 
    else:
        print("Sorry, we don't have", cheese_type, "choice today.")

elif sandwich_type.lower() == "v":
    print("Here is your Veggie Special. Thank you.")
        
else:
    print("Sorry, we don't have", sandwich_type, "choice today.")
print()
print("Goodbye!")


# ## Task 1: Nested `if` 
# ### [ ] Program: Say "Hello"
# - using nested **`if`**
#   
# |Say "Hello" flowchart  |
# | ------ | 
# |  ![Image: Say "Hello" flowchart](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/flowchart_say_hello.png) | 

# In[2]:


# [ ] Say "Hello" with nested if
# [ ] Challenge: handle input other than y/n
if input("Say Hello? ") == "T":
    if input("Full Hello ?") == "T":
        print("Hello")
    else:
        print("Hi")
else:
    print("{friendly nod}")


# ## Task 2: Nested `if` - testing for `False`
# ### Program:  [ ] 3 Guesses
# - Use nested if statements complete the flowchart code
# - Create a **`birds`** string variable with the names of 1, 2, 3 or more birds to make it easier
# - Get **`bird_guess`** input and use **`bird_guess in bird_names`** to generate Boolean True/False
# - If the the guess is wrong (**`False`**) create a subtest until the user has had 3 guesses
#   
# |3 Guesses ("Guess the Bird") flowchart  |
# | ------ | 
# | ![Image of Guess the Bird flowchart](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/flowchart_guess_the_bird.png)   | 

# In[7]:


# [ ] Create the "Guess the bird" program 
bird = "crow"
i = 1
while i <= 3:
    if input("What's your guess? ").lower() == bird:
        if i == 1:
            print("Yes, 1st try!")
        else:
            print("Yes, " + str(i) + "nd try!")
        i = 5
    else:
        if i == 2:
            print("Wrong, " + str(3 - i) + " guess left")
        else:
            print("Wrong, " + str(3 - i) + " guesses left")
        i += 1
if i == 4:
    print("Sorry, out of tries.")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
