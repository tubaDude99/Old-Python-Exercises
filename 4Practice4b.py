#!/usr/bin/env python
# coding: utf-8

# # Lab 4b
# ## `while()` Loops and Increments
# 
# -----
# 
# ### Student will be able to
# - Create forever loops using `while` and `break`
# - Use incrementing variables in a while loop
# - Control while loops using Boolean operators

# ## Tasks

# In[1]:


# [ ] use a "forever" while loop to get user input of integers to add to sum, 
# until a non-digit is entered, then break the loop and print sum
sum = 0
while True:
    i = input()
    if i.isdigit():
        sum = sum + int(i)
    else:
        break
print(sum)


# In[6]:


# [ ] use a while True loop (forever loop) to give 4 chances for input of a correct color in a rainbow
# rainbow = "red orange yellow green blue indigo violet"
i = 0
rainbow = "red orange yellow green blue indigo violet"
while i < 4:
    if input("name a color: ").lower() in rainbow:
        print("Congratulations!")
        break
    else:
        i += 1
if i == 4:
    print("Sorry")


# In[8]:


# [ ] Get input for a book title, keep looping while input is Not in title format (title is every word capitalized)
while 0<1:
    title = input("")
    if title.istitle():
        break
print(title)


# In[10]:


# [ ] create a math quiz question and ask for the solution until the input is correct
while 1>0:
    if input("What's 9 + 10? ") == "19":
        break
    else:
        print("You stupid")
print("Correct!")


# ## Fix the Error

# In[2]:


# [ ] review the code, run, fix the error
tickets = int(input("enter tickets remaining (0 to quit): "))

while tickets > 0:
        # if tickets are multiple of 3 then "winner"
    if int(tickets/3) == tickets/3:
        print("you win!")
    else:
        print("sorry, not a winner.")
    tickets = int(input("enter tickets remaining (0 to quit): "))

print("Game ended")
    


# ## Create a function: quiz_item()  that asks a question and tests if input is correct  
# - quiz_item()has 2 parameter **strings**: question and solution  
# - shows question, gets answer input  
# - returns True if `answer == solution` or continues to ask question until correct answer is provided  
# - use a while loop
# 
# create 2 or more quiz questions that call quiz_item()  
# **Hint**: provide multiple choice or T/F answers

# In[6]:


# Create quiz_item() and 2 or more quiz questions that call quiz_item()
def quizItem(q,s):
    while 1<2:
        a = input(q)
        if a == s:
            return True
            print("Correct!")
            break
        else:
            print("Try again")
quizItem("Frogs are amphibians. \tTrue or False?\n","True")
quizItem("Frogs are which of the following?\na. Reptiles\nb. Fish\nc. Amphibians\nd. Mammals\n","c")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
