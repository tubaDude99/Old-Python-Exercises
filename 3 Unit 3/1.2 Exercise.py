#!/usr/bin/env python
# coding: utf-8

# In[10]:


from datetime import datetime, time, date
d = datetime.today()
print(d)
print(d.year)
print(d.month)
print(d.strftime("%V"))
print(d.strftime("%A"))
print(d.strftime("%j"))
print(d.strftime("%d"))
print(d.strftime("%A (%w)"))


# In[17]:


y = int(input())
if (y % 4 == 0) and not((y % 100 == 0) and not(y % 400 == 0)):
    print("Leap year")
else:
    print("Not leap year")


# In[27]:


from datetime import time, datetime
print(datetime.today().time())


# In[35]:


t = datetime.today().date()
print(t)
t = t.replace(day = (t.day - 5))
print(t)


# In[44]:


y = datetime.today().date().replace(day = (datetime.today().day - 1))
td = datetime.today().date()
tm = datetime.today().date().replace(day = (datetime.today().day + 1))
print("Yesterday:\t", y, "\nToday:\t\t", td, "\nTomorrow:\t", tm)

