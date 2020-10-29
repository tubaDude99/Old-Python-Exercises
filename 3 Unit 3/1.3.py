#!/usr/bin/env python
# coding: utf-8

# # Section 1.3: Date and Time Arithmetic
# * datetime.timedelta
# * datetime operators (+, -, *, /, //, %)
# 
# ### Students will be able to:
# * Create timedelta objects
# * Use timedelta objects to perform date arithmetic
# * Compare two datetime objects
# * Build a useful application using timedelta arithmetic

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## `timedelta` Objects
# 
# 
# Performing time and date calculations can be a tedious task. For example, if you want to know your age in days, you will need to know how many of the years you have lived through were leap years, and how many days were in each additional month that you've lived. Luckily, the `datetime` module has some utilities that will help you perform such calculations with ease. 
# 
# The `time`, `date`, and `datetime` objects all represent points in time. The `datetime` module provides another data type called `timedelta`, which represents a duration of time rather than a point in time. As a programmer, you can define a `timedelta` variable explicitly or by taking the difference between 2 `datetime` variables.
# 
# NOTE: The Greek letter &Delta; (pronounced "delta") is usually used to represent a difference. The name `timedelta` hints that it contains a time difference which is equivalent to a duration of time.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Creating `timedelta` objects
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b9dd8f7d-313e-4fae-855d-e667fa72bc66/DEV330x-1_3a_creating_timedelta_.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/5bc9829e-87aa-4802-a537-1cfb351d0f7b/DEV330x-1_3a_creating_timedelta_objects.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# #### `timedelta(weeks = 0, days = 0, hours = 0, minutes = 0, seconds = 0, milliseconds = 0, microseconds = 0)`
# The attributes of the `timedelta` object are all optional and default to 0 if not specified. `timedelta` does not have year or month attributes because neither of these represent a constant amount of time (leap years are longer than non-leap years and months have from 29 to 31 days).
# 
# #### Explicit definition
# You can define a `timedelta` object in the same way that you define a `time`, `date`, or `datetime` object. 
# 
# ```python
# In [1]: from datetime import timedelta
# In [2]: delta1 = timedelta(days = 7,  hours = 2)
# In [3]: print(detla1)
# 7 days, 2:00:00
# ```
# 
# #### Calculating the difference between two `datetime` objects
# You can define a `timedelta` object as the result of subtracting a `datetime` or `date` object from another.
# 
# ```python
# In [1]: from datetime import datetime
# In [2]: dt1 = datetime(year = 2017, month = 1, day = 1) 
# In [3]: dt2 = datetime(year = 2017, month = 2, day = 1)
# In [4]: delta2 = dt2 - dt1
# In [5]: print(delta2)
# 31 days, 0:00:00
# ```
# 
# ### Getting the `timedelta` attributes
# Though you can use many attributes to explicitly define a `timedelta` object, only the days, seconds, and microseconds are stored in the object. Python will convert all other attributes to these three. The days, seconds, and microseconds attributes can all be accessed in the same way we access a `timedelta` object attributes. 
# 
# In the explicit definition example above, we defined `delta1` using the attributes `days = 7` and `hours = 2`, let's see what was actually stored in `delta1`.
# 
# ```python
# In [5]: delta1.days
# Out[5]: 7
# 
# In [6]: delta1.seconds
# Out[6]: 7200
# 
# In [7]: delta1.microseconds
# Out[7]: 0
# ```
# 
# It's apparent that Python has converted the 2 hours into 2 &times; 60 &times; 60 = 7200 seconds.
# 
# ### Total number of seconds
# Python can also compute the total number of seconds in a `timedelta` object using the `total_seconds()` function. For example, `delta1` has 7 days &times; 24 hours &times; 60 minutes &times; 60 seconds + 7200 seconds = 612000 seconds.
# 
# ```python
# In [8]: delta1.total_seconds()
# Out[8]: 612000.0
# ```

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Explicit definition

# In[1]:


from datetime import timedelta

# Define a timedelta object
delta1 = timedelta(days = 2, seconds = 0, minutes = 15, hours = 1, weeks = 4)
print(delta1, " is stored in delta1")

# Get the stored attributes
d = delta1.days 
s = delta1.seconds 
ms = delta1.microseconds
print("Days = ", d, "| Seconds = ", s, "| Microseconds = ", ms)

# Get total number of seconds
all_seconds = delta1.total_seconds()
print("Total number of seconds = ", all_seconds)


# ### Calculating the difference between two `datetime` points

# In[8]:


from datetime import datetime, timedelta
date1 = datetime(year = 2015, month = 1, day = 19)
date2 = datetime.today()

# Define a time delta
delta2 = date2 - date1

print(delta2, " is stored in delta2")
print("Total number of seconds = ", delta2.total_seconds())


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Creating `timedelta` objects
# 

# In[11]:


# [ ] Create a `timedelta` object that contains: 2 hours, 3 minutes, and 1 week
d = timedelta(hours = 2, minutes = 3, weeks = 1)
print(d)
# --Completed--
from datetime import timedelta
td = timedelta(hours = 2, minutes = 3, weeks = 1)
print(td)


# In[12]:


# [ ] Use a `timedelta` object to calculate the total number of seconds in: 1 hour and 15 minutes
print(timedelta(hours = 1, minutes = 15).total_seconds())
# --Completed--
from datetime import timedelta
td = timedelta(hours = 1, minutes = 15)
total_seconds = td.total_seconds()
print("Total number of seconds = ", total_seconds)


# In[15]:


# Use a `timedelta` object to find out how many days are left until your upcoming birthday
d = datetime(month = 5, day = 19, year = 2020) - datetime.today()
print(d.days)


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Performing Date Arithmetic
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/8fcd87ce-ed40-4552-8583-4c93c70da1bc/DEV330x-1_3b_date_arithmetic.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/5a5fdbea-0252-4663-87a6-a8047107cf9d/DEV330x-1_3b_date_arithmetic.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# ### Arithmetic involving `datetime` and `timedelta` objects
# The `timedelta` objects can be used to perform date arithmetic on `datetime` and `date` objects. For examples, if you want to know the date 100 days from today, you can define a `timedelta` object with 100 days and add it to today's date. In general, a `timedelta` object can be added to or subtracted from a `datetime` object.
# 
# ### Arithmetic on `timedelta` objects
# You can perform basic arithmetic operations on `timedelta` objects. For example, you can add 2 `timedelta` objects, subtract them, or divide them. The following table lists some of the available operations; a complete listing is available on the Python Documentation site at https://docs.python.org/3/library/datetime.html#timedelta-objects.
# 
# Assume: t1, t2, t3 are all `timedelta` objects
# 
# |Operation|Result|
# |---------|------|
# |t1 = t2 + t3| sum of objects|
# |t1 = t2 - t3| different between objects|
# |t1 = t2 * i | multiply by an integer i|
# |f = t2 / t3 | division, return `float`|
# |t1 = t2 // i| integer division, return `int`|
# |t1 = t2 % t3| modulo or remainder|
# 

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Arithmetic using `datetime` and `timedelta` objects
# #### Finding the date 100 days from today. 

# In[17]:


from datetime import datetime, timedelta

# Define a timedelta object
one_hundred_days = timedelta(days = 100)

# Get today's date
current_date = datetime.today()

# Compute the new date
new_date = current_date + one_hundred_days

# Print formatted new date
print("After 100 days:", new_date.strftime("%b/%d/%Y"))


# #### Finding the dates 200 and 300 days from today

# In[18]:


from datetime import datetime, timedelta

# Define the timedelta objects
one_hundred_days = timedelta(days = 100)
two_hundred_days = one_hundred_days * 2
three_hundred_days = one_hundred_days * 3

# Get today's date
current_date = datetime.today()

# Compute the new dates
new_date1 = current_date + two_hundred_days
new_date2 = current_date + three_hundred_days

# Print formatted new dates
print("After 200 days:", new_date1.strftime("%b/%d/%Y"))
print("After 300 days:", new_date2.strftime("%b/%d/%Y"))


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Performing Date Arithmetic

# In[22]:


# [ ] Write a program to compute the date 3 weeks before your birthday 
# to help you remember when to send the invitations
print((datetime(month = 5, day = 19, year = 2020)-timedelta(weeks = 3)).strftime("Send invitations on %m/%d/%y"))
# --Completed--
from datetime import timedelta, datetime

# Modify upcoming_birthday to a specific birthday
upcoming_birthday = datetime(month = 6, day = 28, year = 2018)

# Assign a 3-week timedelta object
three_weeks = timedelta(weeks = 3)

# Compute the reminder date
reminder = upcoming_birthday - three_weeks

print("Send invitations on:", reminder.strftime("%b/%d/%Y"))


# In[27]:


# [ ] Write a program that computes the number of days from the current date till the 3 weeks reminder
# 1) Create a `timedelta` object (td1) for the period between the current date and your upcoming birthday
# 2) Create a `timedelta` object (td2) containing 3 weeks
# 3) Use the `timedelta` objects (td) from 1 and 2 to compute the required number of days
print("Reminder in",((datetime(month = 5, day = 19, year = 2020) - timedelta(weeks = 3)) - datetime.today()).days,"days")
# --Completed--
from datetime import timedelta, datetime

# Modify upcoming_birthday to a specific birthday
upcoming_birthday = datetime(month = 12, day = 28, year = 2018)

# Get today's date
todays_date = datetime.today()

# 1) Compute `timedelta` between current date and upcoming birthday
td1 = upcoming_birthday - todays_date

# 2) Define a 3-week timedelta object
td2 = timedelta(weeks = 3)

# 3) Find out the required number of days
td = td1 - td2
days = td.days

if (days > 0):
    print("Reminder is in", days, "days")
else:
    print("Reminder was", abs(days), "days ago")
    


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Comparing `datetime` objects
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/f2055f1b-ac48-48ae-8a1b-403a33eeab04/DEV330x-1_3c_comparing_datetime_.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/531a0994-58c3-4760-88d6-7329e89f2fba/DEV330x-1_3c_comparing_datetime_objects.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# You can compare `datetime` objects to find out which date precedes the other. The result of the comparison can be used in a conditional or loop structure to control the flow of your program. You can use any of the operators in the following table to perform a comparison.
# 
# |Operator|Description|
# |--------|-----------|
# | < | less than|
# | <= | less than or equal to|
# | > | greater than|
# | >= | greater than or equal to|
# | == | equal to|

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Comparing two birthdays
# In this example, a comparison operator is used to find out which person is older:

# In[28]:


from datetime import date

# Birthday of person 1
birthday1 = date(year = 1993, month = 3, day = 5)

# Birthday of person 2
birthday2 = date(year = 2003, month = 3, day = 20)

# Compare birthdays
if (birthday1 > birthday2):
    print("Person 2 is older")
elif (birthday1 < birthday2):
    print("Person 1 is older")
else:
    print("Person 1 and Person 2 are of the same age")


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# 
# ## Comparing `datetime` objects

# In[31]:


# [ ] Write a program to find out if 4th of July of this year has passed or not
if date(2019,7,4) > datetime.today().date():
    print("July 4th has not passed")
else:
    print("July 4th has passed")
# --Completed--
from datetime import datetime

# Get today's date
todays_date = datetime.today()

# 4th of July of current year
july_4th = datetime(month = 7, day = 4, year = todays_date.year)

if(july_4th < todays_date):
    print("July 4th has passed")
else:
    print("July 4th has not passed yet")


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Creating Useful Applications
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/be9ce05c-0d34-473f-adc8-7909b26cfe64/DEV330x-1_3d_days_till_december_.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b8882593-1bab-42a6-a4ea-5d2daa62dca4/DEV330x-1_3d_days_till_december_solstice.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# The `datetime` module allows you to perform tedious date calculations and display the result in a human-friendly way. The simplicity and versatile functionality of the module will let you design very useful applications involving date and/or time.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ### Creating a December Solstice Countdown application
# In this section, you will see how easy it is to design a December Solstice Countdown application using the `datetime`, `replace`, and `timedelta` functions you have already seen.

# In[32]:


from datetime import datetime

# Define today's date
now = datetime.today()

# December solstice of year 1, it can be any year, it will be changed later
solstice = datetime(month = 12, day = 21, year = 1)

# Change solstice's year to current year
solstice = solstice.replace(year = (datetime.today().year))

# Get the timedelta
count = solstice - now

# Display the solstice countdown
print("There are", count.days, "days until the December solstice!" )


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4</B></font>
# 
# ## Creating Useful Applications
# 

# In[46]:


# [ ] Complete the following program to find out if you are closer to the current year's June or December solstice

# Define today's date
now = datetime.today()

# Define the December solstice
decS = datetime(month = 12, day = 21, year = now.year)

# Define the June solstice
junS = datetime(month = 6, day = 21, year = now.year)

# Find out which solstice is closer
if abs(now - decS) < abs(now - junS):
    print("The december solstice is closer")
elif abs(now - decS) > abs(now - junS):
    print("The june solsitce is closer")
# --Completed--

# Define today's date
now = datetime.today()

# Define the December solstice
december_solstice = datetime(month = 12, day = 21, year = now.year)

# Define the June solstice
june_solstice = datetime(month = 6, day = 21, year = now.year)

# Find out which solstice is closer

# Calculate number of days till each solstice
till_june_solstice = abs(june_solstice - now)
till_december_solstice = abs(december_solstice - now)

# Print the appropriate message
if (till_june_solstice > till_december_solstice):
    print("We are closer to the December solstice")
elif (till_june_solstice < till_december_solstice):
    print("We are closer to the June solstice")
else:
    print("We are halfway between the June and December solstices")

