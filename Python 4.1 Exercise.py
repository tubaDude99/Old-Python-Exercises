#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Five Guys
fChoice = input("Hamburger, cheeseburger, or hot dog? ").lower()
if fChoice == "hamburger":
    fPrice = 4.00
elif fChoice == "cheeseburger":
    fPrice = 5.00
elif fChoice == "hot dog":
    fPrice = 3.50
dChoice = input("Do you want a drink? (y/n) ").lower()
if dChoice == "y":
    dChoice = input("Soda, milkshake, or water? ")
    if dChoice == "soda":
        dPrice = 1.50
    elif dChoice == "milkshake":
        dPrice = 2.50
    elif dChoice == "water":
        dPrice = 0.00
else:
    dPrice = 0.00
print("Your food will be $%.2f and your drink will be $%.2f, for a total of $%.2f" %(fPrice, dPrice, fPrice + dPrice))

