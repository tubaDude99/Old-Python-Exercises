#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Period\tClass\tTeacher\n1st\tEnglish\tMann\n2nd\tAPES\tPiper\n3rd\tPython\tNorman\n4th\tBand\tJarvis")


# In[6]:


job = input("What's your dream job? ")
deg = input("Does that require a degree? ")
if deg.lower() == "yes":
    col = input("What college or university do you wish to attend? ")
    print("Profession\tDegree needed?\tCollege Preference\n%s\t%s\t\t%s" %(job,deg,col))
else:
    print("Profession\tDegree needed?\tCollege Preference\n%s\t%s\t\t%s" %(job,deg,"N/A"))

