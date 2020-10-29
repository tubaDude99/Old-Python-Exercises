#!/usr/bin/env python
# coding: utf-8

# # Section 4.3
# ## `while()` Loops and Incrementing
# - **while `True`  or forever loops**
# - **Incrementing in loops**
# - Boolean operators in while loops
# 
# -----
# 
# ### Student will be able to
# - **Create forever loops using `while` and `break`**
# - **Use incrementing variables in a while loop**
# - Control while loops using Boolean operators

# ## Concept: `while True:` Loop
# ### Using the 'while True:' loop
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/f43862cd-7cdc-45a3-adb1-a07dcbd9ae16/Unit1_Section7.1-while-forever.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/f43862cd-7cdc-45a3-adb1-a07dcbd9ae16/Unit1_Section7.1-while-forever.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# **`while True:`** is known as the **forever loop** because it ...loops forever  
# 
# Using the **`while True:`** statement results in a loop that continues to run forever   
# ...or, until the loop is interrupted, such as with a **`break`** statement.  
# 
# ## `break`
# ### in a `while` loop, causes code flow to exit the loop  
# a **conditional** can implement **`break`** to exit a **`while True`** loop  

# ### Examples
# #### `while True` loops forever unless a `break` statement is used  

# In[1]:


# Review and run code
# this example never loops because the break has no conditions
while True:
    print('write forever, unless there is a "break"')
    break


# In[1]:


# [ ] review the NUMBER GUESS code then run - Q. what cause the break statement to run?
number_guess = "0"
secret_number = "5"

while True:
    number_guess = input("guess the number 1 to 5: ")
    if number_guess == secret_number:
        print("Yes", number_guess,"is correct!\n")
        break
    else:
        print(number_guess,"is incorrect\n")


# In[1]:


# [ ] review WHAT TO WEAR code then run testing different inputs
while True:
    weather = input("Enter weather (sunny, rainy, snowy, or quit): ") 
    print()

    if weather.lower() == "sunny":
        print("Wear a t-shirt and sunscreen")
        break
    elif weather.lower() == "rainy":
        print("Bring an umbrella and boots")
        break
    elif weather.lower() == "snowy":
        print("Wear a warm coat and hat")
        break
    elif weather.lower().startswith("q"):
        print('"quit" detected, exiting')
        break
    else:
        print("Sorry, not sure what to suggest for", weather +"\n")


# ## Task 1: `while True` 
# ### [ ] Program: Get a name forever ...or until done
# - create variable, familar_name, and assign it an empty string (**`""`**)
# - use **`while True:`**
# - ask for user input for familar_name (common name friends/family use) 
# - keep asking until given a non-blank/non-space alphabetical name is received (Hint: Boolean string test)
# - break loop and print a greeting using familar_name

# In[3]:


# [ ] create Get Name program
name = ""
while True:
    name = input("What do your friends call you? ")
    if name.isalpha() and name != " ":
        break
print("Hello " + name)


# ## Concept: Variable Increment
# ### Incrementing a variable
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/188da429-ec3b-4302-8a9b-be513a073bb5/Unit1_Section7.1-increment.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/188da429-ec3b-4302-8a9b-be513a073bb5/Unit1_Section7.1-increment.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Incrementing
# #### `votes = votes + 1` &nbsp; &nbsp; or &nbsp;  `votes += 1`
# 
# ### Decrementing 
# #### `votes = votes - 1` &nbsp; &nbsp; or &nbsp; `votes -= 1`

# ### Examples
#   
# 

# In[4]:


# [ ] review and run example
votes = 3
print(votes)

votes = votes + 1
print(votes)

votes += 2
print(votes)


# In[5]:


print(votes)

votes -= 1
print(votes)


# In[6]:


# [ ] review the SEAT COUNT code then run 

seat_count = 0
while True:
    print("seat count:",seat_count)
    seat_count = seat_count + 1

    if seat_count > 4:
        break


# In[7]:


# [ ] review the SEAT TYPE COUNT code then run entering: hard, soft, medium and exit

# initialize variables
seat_count = 0
soft_seats = 0
hard_seats = 0
num_seats = 4

# loops tallying seats using soft pads vs hard, until seats full or user "exits"
while True:
    seat_type = input('enter seat type of "hard","soft" or "exit" (to finish): ')
    
    if seat_type.lower().startswith("e"):
        print()
        break
    elif seat_type.lower() == "hard":
        hard_seats += 1
    elif seat_type.lower() == "soft":
        soft_seats += 1
    else:
        print("invalid entry: counted as hard")
        hard_seats += 1  
    seat_count += 1
    if seat_count >= num_seats:
        print("\nseats are full")
        break
        
print(seat_count,"Seats Total: ",hard_seats,"hard and",soft_seats,"soft" )


# ## Task 2: Incrementing in a `while()` loop
# ### Program: Shirt Count
# - Enter a sizes (S, M, L)
# - Tally the count of each size
# - Input "exit" when finished
# - Report out the purchase of each shirt size  
# 

# In[9]:


# [ ] Create the Shirt Count program, run tests
shirt = ""
s = 0
m = 0
l = 0
while shirt != "exit":
    if s == 0 and m == 0 and l == 0:
        shirt = input("What's the first shirt? ").lower()
    else:
        shirt = input("What's the next shirt? ").lower()
    if shirt == "s":
        s += 1
    if shirt == "m":
        m += 1
    if shirt == "l":
        l += 1
print("You have %i small shirts, %i medium shirts, and %i large shirts" %(s,m,l))


# ### Challenge: Shirt Register
# Update the **Shirt Count** program to calculate cost
# - Use shirt cost (S = 6, M = 7, L = 8)
# - To calculate and report the subtotal cost for each size 
# - To calculate and report the total cost of all shirts

# In[10]:


# [ ] Create the Shirt Register program, run tests
shirt = ""
s = 0
m = 0
l = 0
while shirt != "exit":
    if s == 0 and m == 0 and l == 0:
        shirt = input("What's the first shirt? ").lower()
    else:
        shirt = input("What's the next shirt? ").lower()
    if shirt == "s":
        s += 1
    if shirt == "m":
        m += 1
    if shirt == "l":
        l += 1
print("You have %i small shirts, %i medium shirts, and %i large shirts" %(s,m,l))
print("That will be $%.2f for small shirts, $%.2f for medium shirts, and $%.2f for large shirts." %(float(6*s),float(7*m),float(8*l)))
print("Your total will be $%.2f." %float(6*s + 7*m + 8*l))


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
