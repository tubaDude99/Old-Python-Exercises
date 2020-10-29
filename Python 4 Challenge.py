#!/usr/bin/env python
# coding: utf-8

# In[5]:


t = 0
for x in range(0,101):
    if x%2 == 0:
        t = t + x
print(t)


# In[10]:


t = 1
for x in range(0,51):
    if x%2 == 1:
        t = t * x
print(t)

