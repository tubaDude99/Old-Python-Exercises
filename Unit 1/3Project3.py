#!/usr/bin/env python
# coding: utf-8

# #  Module 3 Project  
# Course 40460: Introduction to Python, Unit 1 
# 
# The activity is based on Modules 1 - 3 and is similar to the Jupyter Notebook for Module 3 practice, which you may have completed.
# 
# > **NOTE:** This program requires the use of **`if, elif, else`**, and casting between strings and numbers. The program should use the various code syntax covered in Module 3.  
# >  
# >The program must result in print output using numeric input similar to that shown in the sample below.
# 
# ## Program: Cheese Order    
# 
# - Set values for maximum and minimum order variables  
# - Set value for price variable
# - Get order_amount input and cast to a number  
# - Check order_amount and give message checking against  
#   - over maximum
#   - under minimum
# - Else within maximum and minimum give message with calculated price 
# 
# 
# Sample input and output:
# ```
# Enter cheese order weight (numeric value): 113
# 113.0 is more than currently available stock
# ```
# 
# ```
# Enter cheese order weight (numeric value): .15
# 0.15 is below minimum order amount
# ```  
# 
# ```
# Enter cheese order weight (numeric value): 2
# 2.0 costs $15.98
# ```  

# In[2]:


# [ ] create, call and test Cheese Order
maxOrder = 30.0
minOrder = 0.5
price = 4.68
i = 0
while i == 0:
    order = float(input("How many pounds of cheese do you want to order? "))
    if order > maxOrder:
        print(str(order) + " lbs. is more than currently available stock")
    elif order < minOrder:
        print(str(order) + " lbs. is below the minimum order amount")
    else:
        i = 1
        print(str(order) + " lbs. costs " + str(order * price))


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
