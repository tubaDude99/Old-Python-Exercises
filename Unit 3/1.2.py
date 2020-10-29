#!/usr/bin/env python
# coding: utf-8

# # Section 1.2: Working with Dates and Times
# * datetime module
# * datetime.time: hour, minute, second, microsecond, replace
# * datetime.date: year, month, day, replace, today
# * datetime.datetime: year, month, day, hour, minute, microsecond, replace, today, date, time, combine
# * strftime
# 
# ### Students will be able to:
# * Assign and modify a time object (variable)
# * Assign and modify a date object (variable)
# * Get the current local date
# * Assign and modify a datetime object (variable)
# * Split a datetime object into separate time and date objects
# * Combine time and date objects into datetime objects
# * Display a datetime object as a formatted string

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## The `datetime` Module
# 
# Certain applications require knowing the current date and/or time. For example, certain websites display a countdown timer to a launch date or an important event. The Python `datetime` module contains a number of useful datatypes (classes) and functions (methods) to define and manipulate time and date variables. In this lesson, we will first explore ways to create variables that contain time and date information; we will then delve into ways to display the content of these variables in a human-readable way. In the next lesson, we will use these time/date variables to build some useful applications.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## `time` Objects
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/2891e03a-9b5a-4255-97b9-56150e8fb87f/DEV330x-1_2a_time_objects.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/41f5a9d4-7cf3-4190-95eb-1a32789acef7/DEV330x-1_2a_time_objects.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# ### `time(hour = 0, minute = 0, second = 0, microsecond = 0)`
# ### Assigning a `time` object
# The `datetime` module contains a `time` datatype (class) that can be used to store and manipulate time information. When assigning a variable (object) of type `time` you can specify the hour, minute, second, and microsecond attributes. Any attribute that you leave unspecified will be set to its default value of 0. When specifying an attribute, you should make sure it is within its valid range:
# * 0 &leq; hour < 24
# * 0 &leq; minute < 60
# * 0 &leq; second < 60
# * 0 &leq; microsecond < 1000000
# 
# If any of the attributes is outside its valid range, you will get a `ValueError` message.
# 
# Note: 1 second is equal to 1 million microseconds or 1 s = 10<sup>6</sup> &mu;s
# 
# ### Getting `time` object attributes (hour, minute... etc.)
# You can access the attributes of any `time` variable by specifying its name. For example, if you have a `time` variable named `StartTime`, you can get the value of the minute attribute from `StartTime.minute`.
# 
# ### Modifying `time` object attributes (hour, minute... etc.)
# You can not only access the attributes of a `time` variable, you can also modify them. For example, if you want to modify the hour of `StartTime`, you can use an expression similar to `StartTime.replace(hour = 5)` to set the hour attribute to 5 regardless of its previous value. You can also modify multiple attributes simultaneously by specifying all values to be changed. For example, if you want to modify the hour and second of `StartTime`, you can use an expression similar to `StartTime.replace(hour = 5, second = 2)`.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Assigning a `time` object by specifying all attributes (hour, minute, second, microsecond) in order
# When assigning a new `time` object, you can specify all of its attributes by writing the numbers in the following order: hour, minute, second, microsecond.

# In[1]:


from datetime import time

# Time is 8:55:20.000500 PM (or 20:55:20.000500)
t = time(20, 55, 20, 500)
print(t)


# ### Assigning a `time` object by specifying all attributes (hour, minute, second, microsecond) by name
# If you specify the attributes by name, they need not be in order.

# In[2]:


from datetime import time

# Time is 9:10:20.900000 AM (or 9:10:20.900000)
t = time(minute = 10, hour = 9, microsecond = 900000, second = 20)
print(t)


# ### Assigning a `time` object by specifying some attributes
# If an attribute is not specified, it will be set to 0.

# In[3]:


from datetime import time

# Time is 1:10 PM (or 13:10:00:000000)
t = time(hour = 1, minute = 10)
print(t)


# ### Specifying a wrong attribute value
# When an attribute is set to an invalid value, a `ValueError` will be raised. This will happen whether you are assigning or changing the value of an existing variable.

# In[4]:


from datetime import time

# Assigning a time variable with an invalid attribute
t = time(hour = 29)
print(t)


# ### Getting an attribute
# You can access a single attribute or all attributes of a `time` variable separately.

# In[5]:


from datetime import time

# assign a time variable t
t = time(hour = 9, minute = 10, second = 43, microsecond = 100)

# access each of the attributes separately
h = t.hour # will be 9
m = t.minute # will be 10 
s = t.second # will be 43
ms = t.microsecond # will be 100

print("The time is: ", h," hours ", m, " minutes", s, " seconds and ", ms, " microseconds" )


# ### Modifying attributes of an assigned `time` variable
# You might think that an attribute can be changed by specifying it directly as `t.hour = 8`; however, this will result in an error message saying that the attribute is not writable. The solution is to use the `replace` function.
# 
# `replace` copies the information of a `time` variable into a new `time` variable while modifying the specified  attributes, you can then reassign the new variable to the original variable `t`, which modifies `t` to reflect the desired changes. The following example illustrates this idea:

# In[6]:


from datetime import time

# assign t as 9:10:43:0000100
t = time(hour = 9, minute = 10, second = 43, microsecond = 100)
print("Old time: ", t)

# modify hour and minute
t = t.replace(hour = 8, minute = 8)

print("New time: ", t)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## `time` Objects

# In[12]:


# [ ] Create a `time` variable containing the time: 8:45 AM
from datetime import time
t1 = time(minute = 45, hour = 8)
print(t1)
# --Completed--
from datetime import time
t1 = time(minute = 45, hour = 8)
print(t1)


# In[13]:


# [ ] Create a `time` variable containing the time: 8:45:01:000150 PM
from datetime import time
t2 = time(20, 4, 1, 150)
print(t2)
# --Completed--
from datetime import time
t2 = time(20, 4, 1, 150)
print(t2)


# In[14]:


# [ ] Print the hour (only) contained in t3

from datetime import time
t3 = time(hour = 15, minute = 10, second = 0)
print(t3.hour)
# --Completed--
from datetime import time
t3 = time(hour = 15, minute = 10, second = 0)
print(t3.hour)


# In[15]:


# [ ] Modify t3 to: 4:10 PM
t3 = time(hour = 15, minute = 10, second =0)
t3 = t3.replace(hour = 16)
print(t3)
# --Completed--
from datetime import time
t3 = t3.replace(hour = 16)
print(t3)


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## `date` Objects
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/2551ab55-8a84-44d6-9500-438806c95915/DEV330x-1_2b_date_objects.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/6ea0e67e-a2cc-4378-946b-0f111bc961a6/DEV330x-1_2b_date_objects.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# ### `date(year, month, day)`
# The `datetime` module contains a `date` datatype (class) that has the attributes year, month, and day. Assigning, modifying, and accessing a `date` object is similar to that of a `time` object. However, all of the `date` attributes are required because it doesn't make sense to set a month or a day to 0 by default. Therefore, all attributes of a `date` object should be specified and these attributes should be within their valid ranges:
# * 1 &leq; year &leq; 9999
# * 1 &leq; month &leq; 12
# * 1 &leq; day &leq; number of days in the given month and year
# 
# The attributes of a `date` object can be accessed individually, in the same way you access the attributes of a `time` object. For example, to access the month of a variable `StartDate`, you should use the expression `StartDate.month`. 
# 
# ### Current local date
# In most practical applications involving dates, it is very important to know the current local date of the machine executing the code. For example, if you want to build a counter to display how many days has passed since an important event, you will need to know the current date. This can be easily achieved by using the function `today()` as shown in the following examples.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Assigning a `date` object

# In[16]:


from datetime import date

# using all attributes in order (year, month, day) w/o names
# date1 is May 7 2013
date1 = date(2013, 5, 7)
print("date1 is: ", date1)

# using all attributes with names and not necessarily in order
# date2 is April 23 1999
date2 = date(day = 23, month = 4, year = 1999)
print("date2 is: ", date2) 


# ### Getting a `date` attribute

# In[17]:


from datetime import date

# assign a date variable
SpecialDate = date(year = 2017, month = 11, day = 15)

y = SpecialDate.year # will be 2017
m = SpecialDate.month # will be 11
d = SpecialDate.day # will be 15

print("The Special Date is: / month: ", m, "/ day: ", d, "/ year: ", y)


# ### Modifying the attributes of an assigned `date` object
# The `replace` function can be used to modify the attributes of a `date` object in the same way it is used to modify attributes of an assigned `time` object.

# In[18]:


from datetime import date

# assign a date
SomeDate = date(year = 2015, day = 28, month = 2)
print("Old date: ", SomeDate)

# modify year and day
# 2016 is a leap year, so we can set the date to Feb 29 2016
SomeDate = SomeDate.replace(year = 2016, day = 29)
print("New date: ", SomeDate)


# ### Getting the current local date

# In[19]:


from datetime import date

# get today's date
d = date.today()

print(d)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## `date` Objects

# In[20]:


# [ ] Create a `date` variable containing: (March 28 2012)
from datetime import date
d = date(month = 3, day = 28, year = 2012)
print(d)
# --Completed--
from datetime import date
d = date(month = 3, day = 28, year = 2012)
print(d)


# In[21]:


# [ ] Prompt the user to enter a month and a day, get the current year, then create a date object with the information collected
m = int(input("Enter a month number: "))
d = int(input("Enter a day number: "))
y = date.today().year
d = date(month = m, day = d, year = y)
print(d)
# --Completed--
from datetime import date

# prompting the user for month/day
m = int(input("Enter a month number: "))
d = int(input("Enter a day number: "))

# get the current year
current_date = date.today()
y = current_date.year

# creating a new date object
d = date(month = m, day = d, year = y)
print(d)


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## `datetime` Objects
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/908cd4fe-9dcb-40f8-9bce-2707385cf09a/DEV330x-1_2c_datetime.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ad05a56d-9b9f-4a10-b769-c281a30b4644/DEV330x-1_2c_datetime.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# ### `datetime(year, month, day, hour = 0, minute = 0, second = 0, microsecond = 0)`
# Some applications require knowing and/or manipulating both time and date information. The `datetime` module has a datatype (class) that combines both time and date information into the same variable. This general datatype has the same name as the `datetime` module. The `datetime` datatype combines the attributes of a `date` object and a `time` object, and can be assigned, modified, and accessed in a similar way. When assigning a new variable of type `datetime`, all the date attributes are required; the time attributes are optional and have default values of 0. The attributes have the same ranges as those of the individual `time` and `date` objects:
# * 1 &leq; year &leq; 9999
# * 1 &leq; month &leq; 12
# * 1 &leq; day &leq; number of days in the given month and year
# * 0 &leq; hour < 24
# * 0 &leq; minute < 60
# * 0 &leq; second < 60
# * 0 &leq; microsecond < 1000000
# 
# The attributes of a `datetime` variable can be modified using the `replace` function. The new attribute values should be within the valid limits.
# 
# ### Setting a `datetime` object to the current local date and time
# The attributes of a `datetime` object can be set to the current local date and time using the `today` function. The function behaves in the same way it does with a `date` object, except that it also captures the current local time.
# 
# ```python
# # set dt to the current local date and time
# In [1]: dt = datetime.today()
# ```
# 
# ### Splitting a `datetime` object into separate `date` and `time` objects
# A `datetime` object can be split into separate `date` and `time` objects, this can be achieved using the functions `date()` and `time()` as follows:
# 
# ```python
# # set dt to some date/time
# In [1]: dt = datetime(year = 2014, month = 1, day = 3, hour = 15, minute = 1)
# In [2]: t = dt.time() # set time t to 15:1:0.0
# In [3]: d = dt.date() # set date d to January 3 2014
# ```
# 
# ### Combining separate `date` and `time` objects into a single `datetime` object
# Separate `date` and `time` variables can be combined into a single `datetime` variable using the `combine(date, time)` function.
# 
# ```python
# In [1]: t = time(hour = 15, minute = 1) # set time t to 15:1:0.0
# In [2]: d = date(year = 2014, month = 1, day = 3) # set date d to January 3 2014
# In [3]: dt = datetime.combine(d ,t) # or equivalently dt = datetime.combine(date = d, time = t)
# ```

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Assigning a `datetime` object

# In[22]:


from datetime import datetime

# July 4th 2022, at 4:30 PM

# Method 1
dt = datetime(2022, 7, 4, 16, 30)
print("Method 1: ", dt)

# Method 2
dt = datetime(day = 4, month = 7, year = 2022, minute = 30, hour = 16)
print("Method 2: ", dt)


# ### Getting a `datetime` attribute

# In[23]:


from datetime import datetime

# July 4th 2022, at 4:30 PM
dt = datetime(2022, 7, 4, 16, 30)

# access year
print("Year is: ", dt.year)

# access minute
print("Minute is: ", dt.minute)


# ### Modifying the attributes of an assigned `datetime` object

# In[24]:


from datetime import datetime

# July 4th 2022, at 4:30 PM
dt = datetime(2022, 7, 4, 16, 30)

# change year to 2020 and second to 30
dt = dt.replace(year = 2020, second = 30)
print(dt)


# ### Getting the current local date and time

# In[25]:


from datetime import datetime

# get today's date and current local time
dt = datetime.today()
print(dt)


# ### Splitting a `datetime` object into separate `date` and `time` objects

# In[26]:


from datetime import datetime, time, date

# get today's date and current local time
dt = datetime.today()

# split into time t and date d
t = dt.time()
print("Time is: ", t)

d = dt.date()
print("Date is: ", d)


# ### Combining separate `date` and `time` objects into a `datetime` object

# In[27]:


from datetime import datetime, time, date

# assign a time object
t = time(hour = 6, minute = 45, second = 0)

# assign a date object
d = date.today()

# combine t and d into a datetime object
dt = datetime.combine(date = d, time = t)

print(dt)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# 
# ## `datetime` Objects

# In[30]:


# [ ] Create a `datetime` variable containing: (March 28 2012 @ 12:55:10:30 AM)
from datetime import datetime
dt = datetime(2012, 3, 28, 12, 55, 10, 300000)
print(dt)
# --Completed--
from datetime import datetime
dt = datetime(year = 2012, month = 3, day = 28, hour = 0, minute = 55, second = 10, microsecond = 30)
print(dt)


# In[31]:


# [ ] Write code that prints the current hour
from datetime import datetime
print("Current hour:", datetime.today().hour)
# --Completed--
from datetime import datetime
dt = datetime.today()
print("Current hour:", dt.hour)


# In[34]:


# [ ] Write a program that prints the current date on one line and the current time on another line

# --Completed--
from datetime import datetime
dt = datetime.today()

# Splitting the datetime into time/date
t = dt.time()
d = dt.date()

print("Current date is:", d)
print("Current time is:", t)


# In[36]:


# [ ] Write a program that:
# 1) prompts the user for a time (hours and minutes only)
# 2) gets the current date
# 3) combines the collected information into a `datetime` variable
from datetime import date, time, datetime
t = time(hour = int(input("Enter an hour number: ")), minute = int(input("Enter a minute number: ")))
dt = datetime.combine(date = date.today(), time = t)
print(dt)

# --Completed--

#---------------------------------------------
# Method 1: using date, time, today, and combine
from datetime import date, time, datetime

# getting time from user
h = int(input("Enter an hour number: "))
m = int(input("Enter a minute number: "))
t = time(hour = h, minute =m)

# getting the current date
d = date.today()

# combining date and time into a datetime variable
dt = datetime.combine(date = d, time = t)

print(dt)

#---------------------------------------------
# Method 2: using datetime, today, and replace
from datetime import datetime

# getting time from user
h = int(input("Enter an hour number: "))
m = int(input("Enter a minute number: "))

# getting the current date and time
dt = datetime.today()

# replacing the user inputs into dt
dt = dt.replace(hour = h, minute = m)

print(dt)


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Formatting Dates and Times
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7848fa00-5d0d-4dd2-91e3-6eb954b9672c/DEV330x-1_2d_datetime_objects.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ef346d73-c978-4a73-b064-042736ba5a85/DEV330x-1_2d_datetime_objects.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# The date and time information is often shown to us humans; therefore, it is useful to display it in a human-friendly way. For example, you might want to show a date as Nov, 03, 1999, or display the time as 10:15 AM. The `strftime()` function will make this task easier. 
# 
# `strftime()` applies to `time`, `date`, and `datetime` objects. It reads the attributes of the object, applies a formatting directive, and returns a formatted string. There are different date and time directives; however, `time` directives shouldn't be used with `date` objects because they don't have such attributes; similarly, `date` directives shouldn't be used with `time` objects.
# 
# The `strftime()` is passed a string containing all necessary formatting directives along with any necessary slashes, commas, colons, and so on. The following tables show a short list of commonly used directives. The Python Documentation site has more information on the `strftime()` function at https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior.
# 
# #### Date formatting directives
# 
# |Directive| Meaning| Example|
# |---------|--------|--------|
# |%a| Abbreviated weekday name| Sun, Mon, ..., Fri|
# |%A| Full weekday name| Sunday, Monday, ..., Friday|
# |%d| Day of the month as a zero-padded decimal| 01, 02, 03, ... 31|
# |%b| Abbreviated month name| Jan, Feb, ..., Dec|
# |%B| Full month name| January, February, ..., December|
# |%m| Month as a zero-padded decimal| 01, 02,..., 12|
# |%y| 2 decimal year number (without century) | 00, 01, ..., 99|
# |%Y| 4 decimal year number (with century) | 1900, 1989, ..., 2015|
# 
# #### Time formatting directives
# |Directive| Meaning| Example|
# |---------|--------|--------|
# |%H| Hour in 24-hour clock (zero-padded)| 00, 01, ..., 23|
# |%I| Hour in 12-hour clock (zero-padded)| 00, 01, ..., 12|
# |%p| AM or PM| AM, PM|
# |%M| Minutes as zero-padded decimal| 00, 01, ..., 59|
# |%S| Seconds as zero-padded decimal| 00, 01, ...,59|
# 
# 

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Formatting `time` objects

# In[37]:


from datetime import time
t = time(hour = 10, minute = 15)

# display as 10:15 AM
# string passed to strftim includes all necessary spaces and semicolons
formatted_string = t.strftime("%I:%M %p")
print("First format: ", formatted_string)

# display as 10:15:00 (24 hour clock, no AM/PM)
formatted_string = t.strftime("%H:%M:%S")
print("Second format: ",formatted_string)


# ### Formatting `date` objects

# In[38]:


from datetime import date
d = date(year = 1999, month = 11, day =3)

# display as November, 03, 1999
# string passed to strftime includes all necessary spaces and commas
formatted_string = d.strftime("%B, %d, %Y")
print("First format: ", formatted_string)

# display as Nov 03 99
formatted_string = d.strftime("%b %d %y")
print("Second format: ", formatted_string)


# ### Formatting `datetime` objects

# In[39]:


from datetime import datetime 
dt = datetime(year = 1999, month = 11, day = 3, hour = 10, minute = 15)

# display as November, 03, 1999 @ 10:15 AM
formatted_string = dt.strftime("%B, %d, %Y @ %I:%M %p")
print("First format: ", formatted_string)

# display as Nov 03 99 / 10:15:00
formatted_string = dt.strftime("%b %d %y / %H:%M:%S")
print("Second format: ", formatted_string)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4</B></font>
# 
# ## Formatting Dates and Times

# In[44]:


# [ ] Write a program that displays the time: (17:39:10) as:
# 1) 05:39:10 PM
# 2) 17:39:10
t = time(17, 39, 10)
print(t.strftime("%I:%M:%S %p"))
print(t.strftime("%H:%M:%S"))
# --Completed--
from datetime import time
t = time(17, 39, 10, 43)

# 1) 05:39:10 PM
print(t.strftime("%I:%M:%S %p"))

# 2) 17:39:10
print(t.strftime("%H:%M:%S"))


# In[45]:


# [ ] Write a program that displays the date: (October 23rd 2018) as:
# 1) Oct 23, 2018
# 2) 10/23/18
# 3) 23/October/2018
# 4) Tuesday October 23
d = date(2018, 10, 23)
print(d.strftime("%b %d, %Y"))
print(d.strftime("%m/%d/%y"))
print(d.strftime("%d/%B/%Y"))
print(d.strftime("%A %B %d"))
# --Completed--
from datetime import date
dt = date(month = 10, day = 23, year = 2018)

# 1) Oct 23, 2018
print(dt.strftime("%b %d, %Y"))

# 2) 10/23/18
print(dt.strftime("%m/%d/%y"))

# 3) 23/October/2018
print(dt.strftime("%d/%B/%Y"))

# 4) Tuesday October 23
print(dt.strftime("%A %B %d"))


# In[1]:


# [ ] Complete the function `weekday` to return the weekday name of `some_date`
# Use the function to find the weekday on which you were born

from datetime import date

def weekday(some_date):
    return some_date.strftime("%A")
    
# Modify to your birthdate
bd = date(day = 19, month = 5, year = 1901)

# Display the day on which you were born
day = weekday(bd)
print(day)


# --Completed--
from datetime import date

def weekday(some_date):
    return some_date.strftime("%A")

# Modify to your birthdate
bd = date(day = 8, month = 3, year = 1974)

# Display the day on which you were born
day = weekday(bd)
print(day)

