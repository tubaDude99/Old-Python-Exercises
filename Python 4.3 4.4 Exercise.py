#!/usr/bin/env python
# coding: utf-8

# In[1]:


color = input("Pick a color: ").lower()
i = 0
while 1==1:
    i += 1
    if input("Guess the color: ").lower() == color:
        break
print("Congratulations! It only took you %i chances." %i)


# In[3]:


sent = ""
g = 0
while 2<3:
    q = input()
    if q == "STOP":
        break
    else:
        if g == 0:
            sent = sent + q
            g = 1
        else:
            sent = sent + " " + q
print(sent + ".")


# In[1]:


q1 = "What's your favorite color? "
a1 = input(q1).lower()
q2 = "Why is " + a1 + " your favorite color? "
a2 = input(q2)
if a1 == "red":
    q3 = "Are you a Republican? "
    a3 = input(q3).lower()
    if a3.startswith("y"):
        p = "r"
    else:
        p = "d"
elif a1 == "blue":
    q3 = "Are you a Democrat? "
    a3 = input(q3).lower()
    if a3.startswith("y"):
        p = "d"
    else:
        p = "r"
else:
    p = ""
    q3 = "What is your favorite political party? "
    a3 = input(q3)
    q4 = "Who is your favorite 2020 candidate? "
    a4 = input(q4)
    q5 = "What is the airspeed velocity of an unladen swallow? "
    a5 = input(q5)
if p == "r":
    q4 = "Do you support Trump? "
    a4 = input(q4).lower()
    if a4.startswith("y"):
        q5 = "Do you want to build the wall? "
        a5 = input(q5)
    else:
        q5 = "Why not? "
        a5 = input(q5)
if p == "d":
    q4 = "Do you hate Trump? "
    a4 = input(q4)
    if a4.startswith("y"):
        q5 = "Do you want to impeach him? "
        a5 = input(q5)
    else:
        q5 = "Do you want to build the wall? "
        a5 = input(q5)
print(q1, a1)
print(q2, a2)
print(q3, a3)
print(q4, a4)
print(q5, a5)


# In[2]:


t = 0
c = 0
max = int(input("What's the highest possible grade? "))
while 1:
    g = input().lower()
    if g.isdigit() and int(g) <= max:
        t = t + int(g)
        c += 1
    if g == "break" or g == "stop":
        break
print(t/c)

