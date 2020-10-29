#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

p1 = 0
p2 = 0
sm = 0

for dooby in range(100):
    while 1:
        grid()
        print("\n\n[Player One]")
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
        t[x][y] = "X"
        w = win(t)
        if w == 'X':
            p1 += 1
            grid()
            print('\nPlayer One Wins!')
            break
        elif w == 'O':
            p2 += 1
            grid()
            print('\nPlayer Two Wins!')
            break
        if stale():
            sm += 1
            break
        grid()
        print("\n\n[Player Two]")
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
            p1 += 1
            grid()
            print('\nPlayer One Wins!')
            break
        elif w == 'O':
            p2 += 1
            grid()
            print('\nPlayer Two Wins!')
            break
        if stale():
            sm += 1
            break
    t = [[" "," "," "],[" "," "," "],[" "," "," "]]
    ts = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
print("%i Player One Wins" %p1)
print("%i Player Two Wins" %p2)
print("%i Stalemates" %sm)

