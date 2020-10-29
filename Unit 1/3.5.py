#!/usr/bin/env python
# coding: utf-8

# # Section 3.5  
# ## Conditionals, Type, and Mathematics Extended
# - Conditionals: `elif`  
# - Casting   
# - **Basic math operators**  
# 
# -----
# 
# ### Student will be able to
# - Code more than two choices using `elif`  
# - Gather numeric input using type casting   
# - **Perform subtraction, multiplication and division operations in code** 
# 

# ## Concept: Basic Math Operators
# ### `+` addition
# ### `-` subtraction
# ### `*` multiplication
# ### `/` division  
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/5bc97f7e-3015-4178-ac20-371a5302def1/Unit1_Section5.2-Math-operators.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/5bc97f7e-3015-4178-ac20-371a5302def1/Unit1_Section5.2-Math-operators.vtt","srclang":"en","kind":"subtitles","label":"english"}])

# ### Examples

# In[1]:


# [ ] review and run example
print("3 + 5 =",3 + 5)
print("3 + 5 - 9 =", 3 + 5 - 9)
print("48/9 =", 48/9)
print("5*5 =", 5*5)
print("(14 - 8)*(19/4) =", (14 - 8)*(19/4))


# In[3]:


# [ ] review and run example - 'million_maker'
def million_maker():
    make_big = input("enter a non-decimal number you wish were bigger: ")
    return int(make_big)*1000000

print("Now you have", million_maker())


# ## Task 1: Use math operators to solve the set of tasks below

# In[5]:


# [ ] print the result of subtracting 15 from 43
print(43-15)


# In[6]:


# [ ] print the result of multiplying 15 and 43
print(15*43)


# In[8]:


# [ ] print the result of dividing 156 by 12
print(156/12)


# In[10]:


# [ ] print the result of dividing 21 by 0.5
print(21/0.5)


# In[11]:


# [ ] print the result of adding 111 plus 84 and then subtracting 45
print(111+84-45)


# In[13]:


# [ ] print the result of adding 21 and 4 and then multiplying that sum by 4
print((21+4)*4)


# ## Task 2: Multiplying calculator function
# - Define function **`multiply()`**, and within the function:
#   - Get user input() of two *strings* made of whole numbers
#   - Cast the input to **`int()`**
#   - Multiply the integers and **return** the equation with result as a **`str()`**
#     - **return** example 
#      ```python
#      9 * 13 = 117
#      ```

# In[16]:


# [ ] create and test multiply() function
def multiply():
    x = int(input())
    y = int(input())
    return(str(x) + " * " + str(y) + " = " + str(x*y))
print(multiply())


# ## Task 3: Improved multiplying calculator function
# ### Putting together conditionals, input casting and math
# - #### Update the multiply() function to multiply or divide 
#   - Single parameter is **`operator`** with arguments of **`*`** or **`/`** operator
#   - Default operator is "*" (multiply)
#   - **Return** the result of multiplication or division
#   - If operator other than **`"*"`** or **`"/"`**  then **` return "Invalid Operator"`**

# In[21]:


# [ ] create improved multiply() function and test with /, no argument, and an invalid operator ($)
def math(op):
    x = int(input())
    y = int(input())
    if op == "*":
        return(str(x) + " * " + str(y) + " = " + str(x*y))
    elif op == "/":
        return(str(x) + " / " + str(y) + " = " + str(x/y))
    else:
        return("Invalid Operator")
print(math(input()))


# ## Task 4: Fix the errors

# In[25]:


# Review, run, fix 
student_name = input("enter name: ").capitalize()
if student_name.startswith("F"):
    print(student_name,"Congratulations, names starting with 'F' get to go first today!")
elif student_name.startswith("G"):
    print(student_name,"Congratulations, names starting with 'G' get to go second today!")
else:
    print(student_name, "please wait for students with names staring with 'F' and 'G' to go first today.")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
