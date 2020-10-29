#!/usr/bin/env python
# coding: utf-8

# # Lab 2
# ## Functions, Arguments, and Parameters Practice
# 
# -----
# 
# ### Student will be able to
# - **Create functions with a parameter**  
# - **Create functions with a `return` value** 
# - **Create functions with multiple parameters**
# - **Use knowledge of sequence in coding tasks**  
# - **Use coding best practices** 

# ## Tasks

# In[1]:


# [ ] define and call a function short_rhyme() that prints a 2 line rhyme
def short_rhyme():
    print("Make a line and make it rhyme")
    print("Make it rhyme all of the time")
short_rhyme()


# In[2]:


# [ ] define (def) a simple function: title_it() and call the function
# - has a string parameter: msg
# - prints msg in Title Case
def title_it(msg):
    print(msg.title())
title_it("title this")


# In[3]:


# [ ] get user input with prompt "what is the title?" 
# [ ] call title_it() using input for the string argument
def title_it(msg):
    print(msg.title())
title_it(input("What to title? "))


# In[4]:


# [ ] define title_it_rtn() which returns a titled string instead of printing
# [ ] call title_it_rtn() using input for the string argument and print the result
def title_it_rtn(msg):
    return(msg.title())
print(title_it_rtn(input("What to title? ")))


# ## Program: bookstore()
# Create and test bookstore().
# - **bookstore() takes 2 string arguments: book & price**
# - **bookstore returns a string in sentence form** 
# - **bookstore() should call title_it_rtn()** with book parameter  
# - **Gather input for book_entry and price_entry to use in calling bookstore()**
# - **Print the return value of bookstore()**
# >Example of output: **`Title: The Adventures Of Sherlock Holmes, costs $12.99`**

# In[5]:


# [ ] create, call and test bookstore() function
def bookstore(book,price):
    return("The book " + book + " costs $" + str(price) + ".")
print(bookstore(input("What book? "),input("How much? ")))


# ## Fix the error

# In[6]:


def make_greeting(name, greeting):
    return (greeting + " " + name + "!")

# get name and greeting, send to make_greeting 

def get_name():
    name_entry = input("enter a name: ")
    return name_entry

def get_greeting():
    greeting_entry = input("enter a greeting: ")
    return greeting_entry

print(make_greeting(get_name(), get_greeting()))



# 
# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
