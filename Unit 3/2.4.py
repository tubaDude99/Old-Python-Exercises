#!/usr/bin/env python
# coding: utf-8

# # Section 2.4: Powerful Output Formatting
# * `%d %e %E %f %F %c %s %%`
# * `str.format()`
# 
# ### Students will be able to:
# * Format output, including:
#   * Formatting numbers
#   * Formatting strings
#   * Padding
#   * Alignment
# * Format strings using old-style `printf` formatting
# * Format strings using new style formatting

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Using Old-Style Formatting
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b5ffd9cd-7c3b-4b58-82ae-a2471f673e1e/DEV330x-2_4a_old_style_formattin.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/a6561265-83b4-40e4-8ea6-275d388b5c86/DEV330x-2_4a_old_style_formatting.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# There are many ways to display output in Python. The easiest way is to use the `print` function and pass the items you want to display as comma-separated arguments. For example, say you wrote a program to compute the fuel efficiency of a car using the number of gallons `g` it consumes per `m` miles. You can display the output using the following statement:
# 
# ```python
# In [0]: g = 4 #gallons of gas
# In [1]: m = 127.3 #miles
# In [2]: print('The fuel efficiency of a car consuming', g ,'gallons of gas for every', m, ' miles =', m/g, 'MPG')
# 
# The fuel efficiency of a car consuming 4 gallons of gas for every 127.3 miles = 31.825 MPG
# ```
# 
# This was pretty easy; however, you did not have control over the precision or alignment of the printed numbers. Fortunately, Python supports a number of ways to format strings. In this section, you will learn how to use the old-style formatting that is common among other programming languages such as C.
# 
# Generally speaking, you will use positional format placeholders that will be replaced by the values you want to display. You can rewrite the preceding program as follows:
# 
# ```python
# In [0]: g = 4 #gallons of gas
# In [1]: m = 127.3 #miles
# In [2]: print('The fuel efficiency of a car consuming %d gallons of gas for every %4.2f  miles = %4.2f MPG' % (g, m, m/g))
# 
# The fuel efficiency of a car consuming 4 gallons of gas for every 127.30 miles = 31.82 MPG
# ```
# 
# You can clearly identify three format placeholders in the string; each starts with `%`. The string is followed by the modulo operator `%` and a tuple containing the values that should replace the placeholders in order. The following table shows these placeholders and the values that replaced them.
# 
# |Format placeholder | Replaced by|
# |----|----|
# |`%d`| `g`|
# |`%4.2f`|`m`|
# |`%4.2f`|`m/g`|
# 
# The placeholder syntax might seem cryptic at a first glance; however, it is not that complicated. All of the previous placeholders are replaced by numbers that are displayed with certain precision. Each placeholder has the following pattern:
# 
# `%[flags][width][.precision]type`
# 
# For example, the number of miles `m` is formatted as `%4.2f` which means: 
# * No flags are used
# * The total number of characters (including the `.`) that should be displayed is (width = 4)
# * The number of decimal digits is (precision = 2)
# * The numerical value type is float (f)
# 
# If you use the format placeholder `%08.3f` instead, you will increase the number of `char` displayed to 8, padded with zeros on the left, and the precision to 3 decimal points.
# 
# ```python
# In [0]: g = 4 #gallons of gas
# In [1]: m = 127.3 #miles
# In [2]: print('The fuel efficiency of a car consuming %d gallons of gas for every %08.3f miles = %4.2f MPG' % (g, m, m/g))
# 
# The fuel efficiency of a car consuming 4 gallons of gas for every 0127.300 miles = 31.82 MPG
# ```
# 
# The following tables show commonly used flags and types. The Python Documentation site at https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting has a complete listing.
# 
# |Flag| Meaning|
# |---|---|
# |0| The conversion will be padded by zeros for numeric values|
# |-| The converted value is left adjusted|
# |' '| A blank will be placed in front of positive numbers, `-` will be placed in front of negative numbers|
# |+| A sign (+ or -) will be placed in front of the converted number|
# 
# 
# |Type| Meaning|
# |---|---|
# |d| Signed integer |
# |i| Signed integer |
# |e| Floating point exponential format (lowercase)|
# |E| Floating point exponential format (uppercase)|
# |f| Floating point decimal format|
# |F| Floating point decimal format|
# |c| Single character (accepts integer or single character string)|
# |s| String|
# |%| No argument is converted, results in a % character in the result|

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 

# ### Formatting numbers
# In the following examples, the same sentence is generated using different format placeholders for the same year and price. For each example, compare the generated output to the format placeholders.

# In[1]:


year = 2017
price = 2.42011
print('The national average gas price in %d was $ %f' % (year, price))


# In[13]:


year = 2017
price = 2.42011
print('The national average gas price in %i was $%3.2f' % (year, price))


# In[14]:


year = 2017
price = 2.42011
print('The national average gas price in %i was $ %08.2F' % (year, price))


# In[15]:


year = 2017
price = 2.42011
print('The national average gas price in %d was $ %e' % (year, price))


# In[16]:


year = 2017
price = 2.42011
print('The national average gas price in %d was $ %3.2e' % (year, price))


# In[17]:


year = 2017
price = 2.42011
print('The national average gas price in %d was $ %3.2E' % (year, price))


# ### Formatting strings and characters
# In the following example, names are formatted using different format placeholders. Compare the generated output to the format placeholders.

# In[18]:


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print('The first name starts with: %c' % (first_name[0]))
print('The last name ends with the 2 chars: %s' %(last_name[-2:]))


# ### Alignment
# In the following example, output is formatted using different alignment flags. Compare the generated output to the format placeholders.

# In[20]:


from math import pi

print("Right adjusted: %20.2f" %(pi))
print("Left adjusted: %-20.2f" %(pi))


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Using Old-Style formatting
# 

# ### Number formatting and alignment

# In[22]:


# [ ] Use the variables `F` and `C` to generate the following print outputs
'''
75 Fahrenheit = 23.888900 Celsius
75 Fahrenheit = 23.89 Celsius
75 Fahrenheit = 000023.889 Celsius
75 Fahrenheit = 23.889     Celsius
75 Fahrenheit =     23.889 Celsius
75 Fahrenheit = 2.389E+01 Celsius
75 Fahrenheit = 2.389e+01 Celsius
'''

F = 75
C = 23.8889

print('%d Fahrenheit = %f Celsius' %(F, C))
print('%d Fahrenheit = %4.2f Celsius' %(F, C))
print('%d Fahrenheit = %010.3f Celsius' %(F, C))
print('%d Fahrenheit = %-10.3f Celsius' %(F, C))
print('%d Fahrenheit = %10.3f Celsius' %(F, C))
print('%d Fahrenheit = %.3E Celsius' %(F, C))
print('%d Fahrenheit = %.3e Celsius' %(F, C))


# ### string formatting and alignment

# In[24]:


# [ ] Use the string variables below to generate the following print outputs
# HINT: Set the name formatter width to 10 characters

first_name = 'Tamara'
last_name = 'Babic'

'''
Name: Tamara Babic
Name:     Tamara      Babic
Name: Tamara          Babic
Name:     Tamara Babic     
Name: Tamara     Babic     
Name: Tamara Babic
'''   

print("Name: %s %s" %(first_name, last_name))
print("Name: %10s %10s" %(first_name, last_name))
print("Name: %-10s %10s" %(first_name, last_name))
print("Name: %10s %-10s" %(first_name, last_name))
print("Name: %-10s %-10s" %(first_name, last_name))


# ### Personnel information printout

# In[26]:


# [ ] The list `data` contains personnel information (Name, ID, email)
# Write a program to print out the data as follows:
'''
Name                 ID         Email               
--------------------------------------------------
Suresh Datta         57394      suresh@example.com  
Colette Browning     48539      colette@example.com 
Skye Homsi           58302      skye@example.com    
Hiroto Yamaguchi     48502      hiroto@example.com  
Tobias Ledford       48291      tobias@example.com  
Jin Xu               48293      jin@example.com     
Joana Dias           23945      joana@example.com   
Alton Derosa         85823      alton@example.com 
'''

data = [["Suresh Datta", 57394, "suresh@example.com"], ["Colette Browning", 48539, "colette@example.com"], ["Skye Homsi", 58302, "skye@example.com"], ["Hiroto Yamaguchi", 48502, "hiroto@example.com"], ["Tobias Ledford", 48291, "tobias@example.com", "Tamara Babic", 58201, "tamara@example.com"], ["Jin Xu", 48293, "jin@example.com"], ["Joana Dias", 23945, "joana@example.com"], ["Alton Derosa", 85823, "alton@example.com"]]
print('Name                 ID         Email               ')
print(50 * '-')
for x in data:
    print('%-21s%-11s%s' %(x[0],x[1],x[2]))


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Using Python-Style Formatting
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/65b39276-3b54-4880-9cb3-1372b47338aa/DEV330x-2_4b_new_style_formattin.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/127f331b-7abc-41a0-a2d1-4055d66518e5/DEV330x-2_4b_new_style_formatting.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# The old-style formatting you saw has some restrictions. Python comes with a much more flexible string-formatting method: `str.format()`. This method gives you much more control over how to format a print output. The general form of this style is:
# 
# `string_sequence.format(p0, p1, ..., k0=v0, k1=v1, ...)`
# 
# The `string_sequence` variable contains format placeholders and the string you are trying to display. The format placeholders are similar to those used in the old-style formatting; however, you do not need to use the `%` operator in the Python formatting style.
# 
# The following examples demonstrate a few ways to write and replace placeholders:
# 
# #### Without position index, Without formatting string 
# Use `{}` as a placeholder within the string wherever you want a variable value to appear. Then pass the variables you want to display as positional arguments to the `.format()` method; the variables must be passed in order.
# 
# ```python
# In [0]: g = 4 #gallons of gas
# In [1]: m = 127.3 #miles
# In [2]: print('The fuel efficiency of a car consuming {} gallons of gas for every {} miles = {} MPG'.format(g, m, m/g))
# 
# The fuel efficiency of a car consuming 4 gallons of gas for every 127.3 miles = 31.825 MPG
# ```
# 
# #### Without position index, With formatting string
# Use `{:4.2f}` as a placeholder, then pass the variables you want to display as positional arguments to the `.format()` method. Note that the placeholder starts with `:`, followed by a formatting string similar to that of an old-style formatter. This method is the closest to the old-style formatting style.
# 
# ```python
# In [0]: g = 4 #gallons of gas
# In [1]: m = 127.3 #miles
# In [2]: print('The fuel efficiency of a car consuming {:d} gallons of gas for every {:4.2f} miles = {:4.2f} MPG'.format(g, m, m/g))
# 
# The fuel efficiency of a car consuming 4 gallons of gas for every 127.30 miles = 31.82 MPG
# ```
# 
# #### With position index, With formatting string
# Use `{0:4.2f}` as a placeholder, then pass the variables you want to display as positional arguments to the `.format()` method. Note that the placeholder starts with an index, followed by `:`, followed by a formatting string similar to that of an old-style formatter.
# 
# ```python
# In [0]: g = 4 #gallons of gas
# In [1]: m = 127.3 #miles
# In [2]: print('The fuel efficiency of a car consuming {0:d} gallons of gas for every {1:4.2f} miles = {2:4.2f} MPG'.format(g, m, m/g))
# 
# The fuel efficiency of a car consuming 4 gallons of gas for every 127.30 miles = 31.82 MPG
# ```
# 
# The indices `0, 1, 2` refer to the order of the variables passed to the `.format()` method. For example, index `0` refer to the first variable passed, index `1` refer to the second variable passed, and so on. The indices can appear in the `string_sequence` in any order. For example, in the code below you will see the placeholders use variable index `1`, then index `2`, and finally index `0` to refer to `g`, `m`, `m/g` respectively.
# 
# ```python
# In [0]: g = 4 #gallons of gas
# In [1]: m = 127.3 #miles
# In [2]: print('The fuel efficiency of a car consuming {1:d} gallons of gas for every {2:4.2f} miles = {0:4.2f} MPG'.format(m/g, g, m))
# 
# The fuel efficiency of a car consuming 4 gallons of gas for every 127.30 miles = 31.82 MPG
# ```
# 
# ### Using keywords
# You can use a keyword instead of an index in the placeholder `{a:4.2f}`, then pass the variables you want to display as key/value pairs to the `.format()` method.
# 
# ```python
# In [0]: g = 4 #gallons of gas
# In [1]: m = 127.3 #miles
# In [2]: print('The fuel efficiency of a car consuming {a:d} gallons of gas for every {b:4.2f} miles = {c:4.2f} MPG'.format(a = g, b = m, c = m/g))
# 
# The fuel efficiency of a car consuming 4 gallons of gas for every 127.30 miles = 31.82 MPG
# ```
# 
# 
# ### Using flags
# 
# The formatter string in the placeholder follows a similar syntax to that of the old-style formatter.
# 
# `:[flags][width][.precision]type`
# 
# The following table shows commonly used flags for the Python display style
# 
# |Flag| Meaning|
# |---|---|
# |<| Left-align within available space|
# |>| Right-align within available space|
# |^| Center-align within available space|
# |0| The conversion will be padded by zeros for numeric values|
# |,| Use a comma as thousands separator|
# |' '| A blank will be placed in front of positive numbers, `-` will be placed in front of negative numbers|
# |+| A sign (+ or -) will be placed in front of the converted number|

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 

# ### Formatting numbers
# In the following examples, we repeat some of the old-style formatting examples using the new style formatting.

# In[27]:


year = 2017
price = 2.42011
print('The national average gas price in {:d} was $ {:f}'.format(year, price))


# In[28]:


year = 2017
price = 2.42011
print('The national average gas price in {0:d} was $ {1:3.2F}'.format(year, price))


# In[29]:


year = 2017
price = 2.42011
print('The national average gas price in {y:d} was $ {p:1.2e}'.format(y = year, p = price))


# In[30]:


year = 2017
price = 2.42011
print('The national average gas price in {:d} was $ {:010.2f}'.format(year, price))


# ### Formatting strings
# The character conversion type `c` is not supported in the new formatting style. Use the string conversion type `s` as in the following example:

# In[31]:


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print('The first name starts with: {:s}'.format(first_name[0]))
print('The last name ends with the 2 chars: {:s}'.format(last_name[-2:]))


# ### Setting alignment
# The old-style formatting allows you to right-align and left-align output. The new formatting style also allows you to center-align output.

# In[35]:


from math import pi

print('Right adjusted : {:<20.2f}'.format(pi))
print('Center adjusted: {:^20.2f}'.format(pi))
print('Left adjusted  : {:>20.2f}'.format(pi))


# ### Setting padding and alignment

# In[33]:


from math import pi

# Padding with zeros

print('Right adjusted : {:0<20.2f}'.format(pi))
print('Center adjusted: {:0^20.2f}'.format(pi))
print('Left adjusted  : {:0>20.2f}'.format(pi))


# In[36]:


from math import pi

# Padding with underscore characters

print('Right adjusted : {:_<20.2f}'.format(pi))
print('Center adjusted: {:_^20.2f}'.format(pi))
print('Left adjusted  : {:_>20.2f}'.format(pi))


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Using Python-Style Formatting

# ### Number formatting and alignment

# In[48]:


# [ ] Use Python-style formatting and the variables `F` and `C` to generate the following print outputs
'''
75 Fahrenheit = 23.888900 Celsius
75 Fahrenheit = 23.89 Celsius
75 Fahrenheit = 0000023.89 Celsius
75 Fahrenheit = 23.889     Celsius
75 Fahrenheit =   23.889   Celsius
75 Fahrenheit =     23.889 Celsius
75 Fahrenheit = 2.389E+01 Celsius
'''

F = 75
C = 23.8889
print('{:d} Fahrenheit = {:2.6f} Celsius'.format(F,C))
print('{:d} Fahrenheit = {:2.2f} Celsius'.format(F,C))
print('{:d} Fahrenheit = {:010.2f} Celsius'.format(F,C))
print('{:d} Fahrenheit = {:<10.3f} Celsius'.format(F,C))
print('{:d} Fahrenheit = {:^10.3f} Celsius'.format(F,C))
print('{:d} Fahrenheit = {:>10.3f} Celsius'.format(F,C))
print('{:d} Fahrenheit = {:2.3E} Celsius'.format(F,C))


# ### String formatting and alignment

# In[52]:


# [ ] Use Python-style formatting and the string variables below to generate the following print outputs
# HINT: Set the name formatter width to 10 characters

first_name = 'Tamara'
last_name = 'Babic'

'''
Name: Tamara Babic
Name: Tamara          Babic
Name: Tamara____ _____Babic
Name: __Tamara__ __Babic___
Name: ____Tamara Babic_____
Name:     Tamara Babic     
'''   
print('Name: {:s} {:s}'.format(first_name,last_name))
print('Name: {:<10s} {:>10s}'.format(first_name,last_name))
print('Name: {:_<10s} {:_>10s}'.format(first_name,last_name))
print('Name: {:_^10s} {:_^10s}'.format(first_name,last_name))
print('Name: {:_>10s} {:_<10s}'.format(first_name,last_name))
print('Name: {:>10s} {:<10s}'.format(first_name,last_name))


# ### Personnel information printout

# In[55]:


# [ ] The list `data` contains personnel information (Name, ID, email)
# Write a program using Python-style formatting to print out the data as follows:
'''
        Name         |     ID     |        Email        
________________________________________________________
    Suresh Datta     |   57394    |   suresh@example.com
  Colette Browning   |   48539    |  colette@example.com
     Skye Homsi      |   58302    |     skye@example.com
  Hiroto Yamaguchi   |   48502    |   hiroto@example.com
   Tobias Ledford    |   48291    |   tobias@example.com
       Jin Xu        |   48293    |      jin@example.com
     Joana Dias      |   23945    |    joana@example.com
    Alton Derosa     |   85823    |    alton@example.com
'''

data = [["Suresh Datta", 57394, "suresh@example.com"], ["Colette Browning", 48539, "colette@example.com"], ["Skye Homsi", 58302, "skye@example.com"], ["Hiroto Yamaguchi", 48502, "hiroto@example.com"], ["Tobias Ledford", 48291, "tobias@example.com", "Tamara Babic", 58201, "tamara@example.com"], ["Jin Xu", 48293, "jin@example.com"], ["Joana Dias", 23945, "joana@example.com"], ["Alton Derosa", 85823, "alton@example.com"]]
print('        Name         |     ID     |        Email        ')
for x in data:
    print("{:^20s} | {:^10d} | {:>20s}".format(x[0], x[1], x[2]))

