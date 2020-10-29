#!/usr/bin/env python
# coding: utf-8

# In[10]:


import random

t = [[" "," "," "],[" "," "," "],[" "," "," "]]
ts = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']

def grid():
    print("\n3 %s | %s | %s" %(t[0][2],t[1][2],t[2][2]))
    print(" ---+---+---")
    print("2 %s | %s | %s" %(t[0][1],t[1][1],t[2][1]))
    print(" ---+---+---")
    print("1 %s | %s | %s" %(t[0][0],t[1][0],t[2][0]))
    print("  A   B   C")

def win(t):
    w = ''
    for x in range(3):
        if t[x][0] == t[x][1] == t[x][2] and t[x][0] != ' ':
            w = t[x][0]
    for x in range(3):
        if t[0][x] == t[1][x] == t[2][x] and t[0][x] != ' ':
            w = t[0][x]
    if t[0][0] == t[1][1] == t[2][2] and t[1][1] != ' ':
        w = t[1][1]
    if t[0][2] == t[1][1] == t[2][0] and t[1][1] != ' ':
        w = t[1][1]
    return(w)

def stale():
    q = 1
    for i in t:
        for x in i:
            if x == " ":
                q = 0
    if q:
        grid()
        print("\nStalemate!\nNo Winner")
        return(True)
    else:
        return(False)

def cpu(g):
    for d in ts:
        a = g
        if d[0].lower() == 'a':
            x = 0
        elif d[0].lower() == 'b':
            x = 1
        elif d[0].lower() == 'c':
            x = 2
        y = int(d[1]) - 1
        a[x][y] = "O"
        w = win(a)
        if w == "O":
            return(d)
        a[x][y] = "X"
        w = win(a)
        if w == "X":
            return(d)
        a[x][y] = " "

l = 1 - random.randint(0,1)
if l:
    print("Player goes first")
else:
    print("Computer goes first")

while 1:
    if l:
        grid()
        print("\n\n[Player]")
        while 1:
            a = input("Move: (x,y) ")
            i = [' ',' ']
            for d in a:
                if d.isdigit():
                    y = int(d) - 1
                    i[1] = d
                if d.isalpha():
                    if d.lower() == 'a':
                        x = 0
                    elif d.lower() == 'b':
                        x = 1
                    elif d.lower() == 'c':
                        x = 2
                    i[0] = d.upper()
            i = i[0] + i[1]
            if type(x) == int and type(y) == int:
                if 0 <= x <= 2 and 0 <= y <= 2 and t[x][y] == " ":
                    break
            else:
                print(x, type(x))
                print(y, type(y))
        ts.remove(i)
        t[x][y] = "X"
        w = win(t)
        if w == 'X':
            grid()
            print('\nPlayer Wins!')
            break
        elif w == 'O':
            grid()
            print('\nComputer Wins!')
            break
        if stale():
            break
    grid()
    print("\n\n[Computer]")
    c = cpu(t)
    if c:
        a = c
    else:
        a = ts[random.randint(0,len(ts)-1)]
    if a[0].lower() == 'a':
        x = 0
    elif a[0].lower() == 'b':
        x = 1
    elif a[0].lower() == 'c':
        x = 2
    y = int(a[1]) - 1
    ts.remove(a)
    t[x][y] = "O"
    w = win(t)
    if w == 'X':
        grid()
        print('\nPlayer Wins!')
        break
    elif w == 'O':
        grid()
        print('\nComputer Wins!')
        break
    if stale():
        break
    l = 1


# In[7]:


t

