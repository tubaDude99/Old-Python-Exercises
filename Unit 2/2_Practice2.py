#!/usr/bin/env python
# coding: utf-8

# # Module 2 Lab
# ## Sequence Manipulation Practice
# 
# -----
# 
# ### Student will be able to
# - Create lists
# - Access items in a list
# - Add items to the end of a list
# - Insert items into a list
# - Delete items from a list

# ## Create Lists

# In[1]:


# [ ] create and populate list called days_of_week then print it
dW = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(dW)


# In[3]:


# [ ] after days_of_week is run above, print the days in the list at odd indexes 1,3,5

print(dW[1])
print(dW[3])
print(dW[5])


# ## Phone Letters
# ![phone keys: number and letters](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/phone_letters.JPG)
# Create a list, **`phone_letters`**, where the index 0 - 9 contains the letters for keys 0 - 9.  
# 
# - 0 = ' ' (a space)
# - 1 = '' (empty)
# - 2 = 'ABC'
# - 3 = 'DEF'
# - etc...
# 

# In[4]:


# [ ] create and populate list called phone_letters then print it
pLet = [' ', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']


# ## Access Lists
# ### for the 2 cells below
# - Use days_of_week list created above
# - Run the cell above to make the list available

# In[7]:


# [ ] create a variable: day, assign day to "Tuesday" using days_of_week[]
# [ ] print day variable
dW = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
day = dW[dW.index("Tuesday")]
print(day)


# In[30]:


# PART 2
# [ ] assign day to days_of_week index = 5
# [ ] print day
dW = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
day = dW[5]
print(day)


# ## Append and Insert Items into a List
# 
# ### Endsday, Midsday, Resterday
# #### for the exercises below
# - Use days_of_week list created above
# - Run the cell defining days_of_week above to make the list available

# In[31]:


# [ ] Make up a new day! - append an 8th day of the week to days_of_week 
# [ ] print days_of_week
dW.append("Endsday")
print(dW)


# ### Question  
# - What happens if you keep running the cell above?  
# - How can you return to the initial state with the regular 7 days in days_of_week? 

# In[32]:


# [ ] Make up another new day - insert a new day into the middle of days_of_week between Wed - Thurs
# [ ] print days_of_week
dW.insert(dW.index('Thursday'), "Midsday")

print(dW)


# In[33]:


# [ ]  Extend the weekend - insert a day between Fri & Sat in the days_of_week list
# [ ] print days_of_week
dW.insert(dW.index('Saturday'),"Endsday")

print(dW)


# ## Delete Items from a List
# ### `del` & `.pop()` some bad ideas
# #### Exercises below assume days_of_week appended/inserted 3 extra days in previous exercises

# In[34]:


# [ ] print days_of_week 
# [ ] modified week is too long - pop() the last index of days_of_week & print .pop() value
# [ ] print days_of_week
print(dW)
print(dW.pop())
print(dW)


# In[35]:


# [ ] print days_of_week 
# [ ] delete (del) the new day added to the middle of the week 
# [ ] print days_of_week
print(dW)
del(dW[dW.index("Midsday")])
print(dW)


# In[36]:


# [ ] print days_of_week 
# [ ] programmers choice - pop() any day in days_of week & print .pop() value
# [ ] print days_of_week
print(dW)
print(dW.pop(-2))
print(dW)


# ## Program:  Letter to Number Function
# ### For the exercise below
# - Use phone_letters list created above
# - Run the cell above to make the list available 
# 
# #### Recall unit 1 using **`in`** to search for a string in a string
# ```python
# if "e" in "open":
#     print("e found")
# else:
#    print("e not found")
# ```
# 
# ![phone keys: number and letters](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/phone_letters.JPG)
# 
# ### Create funtion let_to_num()
# - let_to_num() takes input of a single letter, space or empty string stored in an argument variable: letter
#   - use `while key < 10:` to try numbers 0 - 9 as index for `phone_letters` ("key" = phone dial pad key)
#   - check if `letter` variable is in the index of `phone_letters[key]` 
# ```python
# key = 0
# while key < 10:
#     if # Create Code: determine if letter is **`in`** any of the phone_letters[key] where key is the index 0 -9:
#         return key
#     else:
#         key = key + 1
# return "Not Found"
# ```
# - return the number or "Not Found"
# - **call** let_to_num() to test the function so it prints the argument and return value with:
#   - space
#   - lowercase letter
#   - different letter, uppercase
#   - a number
#   
# **Bonus**: create a special case to check if empty string (`""`) was submitted   
# the problem is that an empty string will be found in all strings as  
# ```python
# if "" in "ABC": 
# ```  
# is True, and is true for any phone_letters, but should `return 1`

# In[45]:


# [ ] create let_to_num()
pLet = [' ', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
def letToNum(l):
    if l:
        k = 0
        while k < 10:
            if l in pLet[k] and k != 1:
                return(k)
            k += 1
    else:
        return(1)
print(letToNum(input().upper()))


# ## Challenge: Reverse a string 
# ### Using 
# - while
# - .pop()
# - insert()  
# 
# **`pop()`** the **first item** in the list and add to the beginning of a new string.

# In[46]:


# [ ] Challenge: write the code for "reverse a string"

    
some_numbers =[1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77]
rev_list = []
print(some_numbers)
while some_numbers:
    last = some_numbers.pop(0)
    rev_list.insert(0,last)
    #print("new list:", rev_list)
    
print("\nnew list:", rev_list)  


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
