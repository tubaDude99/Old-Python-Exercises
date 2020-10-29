#!/usr/bin/env python
# coding: utf-8

# In[5]:


def make_schedule(period1, period2):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title())
    return schedule
student_schedule = make_schedule("mathematics", "history")
print("SCHEDULE:", student_schedule)

