#!/usr/bin/env python
# coding: utf-8

# #  Module 1 Project  
# Course 40460: Introduction to Python, Unit 1
# 
# The activity is based on Module 1 and is similar to the Jupyter Notebook for Module 1 practice, which you may have completed.
# 
# > **NOTE:** This program requires print output and code syntax used in Module 1.
# 
# | Some Assignment Requirements |  
# |:-------------------------------|  
# | **NOTE:** This program requires `print` output and using code syntax used in Module 1 such as variable assignment, `input`, `in` keyword, `.lower()` or `.upper()` method.  |  
# 
# 
# ## Program: Allergy Check  
# 
# 1. **[ ]** Get user **`input`** for categories of food eaten in the last 24 hours  
#  save in a variable called **input_test**.  
#  *Example input*
#  [![01 02 practice Allergy-input](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/eaten_input.gif) ](https://1drv.ms/i/s!Am_KPRosgtaij65qzFD5CGvv95-ijg)
# &nbsp;  
# 2. **[ ]** Print **`True`** if "dairy" is in the **input_test** string.  
# **[ ]** Test the code so far.  
# &nbsp;
# 3. **[ ]** Modify the print statement to output similar to below.  
# *Example output*
# [![01 02 Allergy output](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/eaten_output.gif) ](https://1drv.ms/i/s!Am_KPRosgtaij65rET-wmlpCdMX7CQ)  
# Test the code so far trying input including and without the string "dairy".  
# &nbsp;  
# 
# 4. **[ ]** Repeat the process checking the input for "nuts", **challenge** add "Seafood" and "chocolate".  
# **[ ]** Test your code.  
# &nbsp;  
#   
# 5. **[ ] Challenge:** Make your code work for input regardless of case, e.g. - print **`True`** for "Nuts", "NuTs", "NUTS" or "nuts".  
# 

# In[6]:


# Create Allergy check code

# [ ] get input for input_test variable
input_test = input("enter somethings eaten in last 24 hrs: ").lower()

# [ ] print "True" message if "dairy" is in the input or False message if not
dairy = 'dairy' in input_test
print('It is', dairy, 'that "' + input_test + '" contains "dairy"')

# [ ] print True message if "nuts" is in the input or False if not
nuts = 'nuts' in input_test
print('It is', nuts, 'that "' + input_test + '" contains "nuts"')
# [ ] Challenge: Check if "seafood" is in the input - print message
seafood = 'seafood' in input_test
print('It is', seafood, 'that "' + input_test + '" contains "seafood"')
# [ ] Challenge: Check if "chocolate" is in the input - print message
chocolate = 'chocolate' in input_test
print('It is', chocolate, 'that "' + input_test + '" contains "chocolate"')


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
