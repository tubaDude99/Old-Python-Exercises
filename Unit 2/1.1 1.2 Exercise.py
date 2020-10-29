#!/usr/bin/env python
# coding: utf-8

# In[3]:


while True:
    fName = input("What is your first name? ")
    if fName == "exit":
        break
    lName = input("What is your last name? ")
    if lName == "exit":
        break
    print(fName[0] + ". " + lName[0] + ".")


# In[5]:


costu = input("What is your Halloween costume? ")
g = ""
while g != costu[0]:
    g = input("What's the first letter of the costume? ")
    if g != costu[0]:
        print("Try again.")
print("Correct!")

