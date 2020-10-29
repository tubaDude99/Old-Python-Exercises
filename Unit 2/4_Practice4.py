#!/usr/bin/env python
# coding: utf-8

# # Module 4 Lab
# ## Working with Files Practice
# 
# -----
# 
# ### Student will be able to
#  
# - Import files into Jupyter Notebooks  
# - Open and **`.read()`** local files in memory   
# - **`.read()`** a specific number of characters  
# - Use **`.readlines()`** to read data from file as a **list** of lines  
# - Use **`.readlines()`** to read data from file as a **list** of lines   
# - Use **`.readline()`** to read data from file a line at a time   
# - Use **`.strip()`** to remove new line characters  
# - `.write()` data to a new local file  
# - Use **`.seek()`** to set file read or write location  
# - Use file append mode  

# ## Task 1: Order the Rainbow
# #### Open the rainbow file, then put in a list and print in alphabetical order
# Download and open the file  
# - Download list of rainbow colors, as `rainbow.txt`, using `curl` 
#   https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow. 
# - Open rainbow.txt in read mode using a variable: rainbow_file.
#  

# In[2]:


# [ ] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow as rainbow.txt
get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow -o rainbow.txt')


# 
# - Read rainbow_file as a list variable: rainbow_colors using `.readlines()`.    
# 

# In[3]:


# [ ]  Open rainbow.txt in read mode & read as list with .readlines()
rainbows = open('rainbow.txt', 'r').readlines()


# 1. Sort the rainbow_lines list alphabetically.
# 2. Print each line of rainbow_lines by iterating the sorted list.
# 3. Close rainbow_file.

# In[4]:


# [ ] sort rainbow_colors list, iterate the list to print each color
rainbows.sort()
for x in rainbows:
    print(x)


# ## Task 2: The Weather
# Create a program that reads from a file to display city name and average temperature in Celsius. 
# 
# - Use `!curl` to download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv as `mean_temp.txt`.  
#   
# 

# In[5]:


# [ ] The Weather: import world_mean_team.csv as mean_temp.txt
get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt')


# 1. Open the file in `'r'` mode.  
# 2. Read the first line of text into a variable called: `  headings` and `print()`.    
# 3. Convert `headings` to a list using **`.split(',')`** which splits on each comma, `print()` the list.  

# In[12]:


# [ ] The Weather: open file, read/print first line, convert line to list (splitting on comma)
mTemp = open('mean_temp.txt', 'r')
print(mTemp.readline())
mTemp.seek(0)
print(mTemp.readline().split(','))


# #### Use a while loop to read the remaining lines from the file  
#   1. Assign remainging lines to a **`city_temp`** variable.  
#   2. Convert the city_temp to a list using **`.split(',')`** for each **`.readline()`** in the loop.  
#   3. Print each city & the highest monthly average temperature.   
#   4. Close mean_temps.
# 
# >Tips & Hints:   
# - Use the print output of **`headings`** to determine the city_temp indexes to use.  
# - "month ave: highest high" for Bejing is 30.9 Celsius.
# - Convert `city_temp` to lists with `.split(',')`.
# 

# In[13]:


# [ ] The Weather: use while loop to print city and highest monthly average temp in celsius
cTemp = mTemp.readlines()
for x in cTemp:
    x = x.split(',')
    print(x[0] + ':', x[2] + '° C')


# ## Task 3: Random pi  guessing
# Create random appearing numbers by reading digits of pi.
# *Note: Numbers only "appear" random.*
# 
# - Download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi as pi.txt.

# In[15]:


# [ ] use curl to download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi as pi.txt
get_ipython().system('curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi -o pi.txt')


# #### Set up the project files and intitial values  
# 1. Open pi.tx in read mode, the file has a single line of text "3.14....".  
# 2. Get user name as input and say "hi".
# 3. Use the length of `name` for variable called `seed`.
# 4. Use `.seek()` with the value of `seed` to set the initial pointer location reading the file.
# 5. Create a variable `digit` and assign it the value of reading one character from the file.
# 6. Get `guess` variable value from users `input`  - "enter a single digit guess or "q" to quit".
# 7. Initialize `correct` and `wrong` counter variables to **`0`**  (zero).

# In[16]:


# [ ] Set up the project files and initial values
pi = open('pi.txt', 'r')
name = input('What\'s your name? ')
print('Hi %s!' %name)
seed = len(name)
pi.seek(seed)
digit = pi.read(1)
guess = input('Enter a single-digit guess or "q" to quit: ')
correct = 0
wrong = 0


# #### Create a while loop that tests that `guess` is a *digit* string
# Then in the loop:
# 1. If `digit` ( read from pi file) is "**.**" read the next character for digit.
# 2. Else if `digit` is "\n" increment `seed` and use `seed` to set the pointer uing .`seek()`.
# 3. Else see if `guess` is equal to `digit`.
#   a. If `guess` equals `digit`: print "correct" and increment the varible named `correct`.
#   b. If `guess` not equal `digit`: print "incorrect" and increment the variable named `wrong`.
#   
# **End the while loop** when user enters any non-digit(s) for `guess`, like "q".  
# - Print `correct` and `wrong` values within a message to the user.
# - Close the pi file.

# In[17]:



while guess.isdigit():
    if digit == ".":
        digit = pi.read(1)
    elif digit == "\n":
        seed += 1
        pi.seek(seed)
        digit = pi.read(1)
    else:
        if int(guess) == int(digit):
            print(guess, "is correct")
            correct += 1
        else:
            print("Sorry, number is", digit, "not", guess)
            wrong += 1
    guess = input("enter another digit guess or \"q\": ")
    digit = pi.read(1)
    
print("\nThanks for playing\nNumber Correct:", correct, "\nNumber Incorrect:", wrong)
pi.close()


# In[ ]:





# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
