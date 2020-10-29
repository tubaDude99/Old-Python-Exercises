#!/usr/bin/env python
# coding: utf-8

# In[3]:


def movTimes():
    a = input("What movie? ") + ",", input("What times? ")
    b = input("What movie? ") + ",", input("What times? ")
    c = input("What movie? ") + ",", input("What times? ")    
    print(a)
    print(b)
    print(c)
movTimes()


# In[6]:


def stuff(name,place,job):
    print(name + ",", place + ",", job)
stuff("Nathan", "Boston", "engineer.")

