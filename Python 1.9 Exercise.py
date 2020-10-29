#!/usr/bin/env python
# coding: utf-8

# In[11]:


menu = "Hamburger, Jambalaya, Gumbo, Alfredo, Ribs"
print("hamburger".lower() in menu.lower())
print("Jambalaya".lower() in menu.lower())
print("gumbo".lower() in menu.lower())
print("Alfredo".lower() in menu.lower())
print("RIBS".lower() in menu.lower())
print()
menu = ["hamburger", "jaMBAlaya", "guMBo", "aLFrEdo", "ribs"]
print(menu[0].capitalize())
print(menu[1].lower())
print(menu[2].upper())
print(menu[3].swapcase())
print(menu[4].title())

