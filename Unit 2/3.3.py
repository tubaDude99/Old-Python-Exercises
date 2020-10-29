#!/usr/bin/env python
# coding: utf-8

# # Section 3.3
# ## .extend(), .reverse(), and .sort() Methods
# - for in: `for` loop using `in`
# - for range: `for range(start,stop,step)` 
# - **More list methods: `.extend()`, `+, .reverse(), .sort()`**
# - Strings to lists,`.split()`, and list to strings, `.join()`
# 
# ----- 
# 
# ### Student will be able to
# - Iterate through lists using `for` with `in`
# - Use `for range()` in looping operations
# - **Use list methods `.extend()`, `+, .reverse(), .sort()`**
# - Convert between lists and strings using `.split()` and `.join()` 

# ## Concept: Combine Lists
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/249a8d33-1e69-47e1-ab59-a8cf93f3fa8b/Unit2_Section3.3a_concatenate_lists.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/249a8d33-1e69-47e1-ab59-a8cf93f3fa8b/Unit2_Section3.3a_concatenate_lists.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### `+`  list addition
# ###  `.extend()` list method   
# 
# #### Combine lists with `+` and `.extend()`
# ```python
# visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# wish_cities = ["Reykjavík", "Moscow", "Beijing", "Lamu"]
# # combine in a new list
# all_cities = visited_cities + wish_cities
# 
# # add a list to an existing list
# visited_cities.extend(wish_cities)
# ```

# ### Examples

# In[1]:


# [ ] review and run example
visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
wish_cities = ["Reykjavík", "Moscow", "Beijing", "Lamu"]

# .extend() 
# extending visited_cities list (IN PLACE) by concatenating wish_cities
visited_cities.extend(wish_cities)
print("ALL CITIES",visited_cities)


# In[2]:


# [ ] review and run example
visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
wish_cities = ["Reykjavík", "Moscow", "Beijing", "Lamu"]

# (+) Addition operator for lists creates a (NEW) combined List
all_cities = visited_cities + wish_cities

print("ALL CITIES")
for city in all_cities:
    print(city)


# In[3]:


# [ ] review and run example
team_a = [0,2,2,2,4,4,4,5,6,6,6]
team_b = [0,0,0,1,1,2,3,3,3,6,8]
print("Team A:", team_a, "\nTeam B:",team_b)

# (+) Addition operator 
team_totals = team_a + team_b
print("Team Totals", team_totals)


# In[4]:


# [ ] review and run example after running cell above
# .extend() 
team_a.extend(team_b)
print("Team_a extended", team_a)

# what happens if you keep running this cell?


# ## Task 1: Combine lists

# In[6]:


# [ ] extend the list common_birds with list birds_seen which you must create
cBirds = ["chicken", "blue jay", "crow", "pigeon"]
bSeen = ["cardinal", "robin", "hawk"]
cBirds += bSeen
print(cBirds)


# In[7]:


# [ ] Create 2 lists zero_nine and ten_onehundred that contain 1-9, and 10 - 100 by 10's.
# [ ] use list addition to concatenate the lists into all_num and print
zN = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tO = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(zN + tO)


# ## Concept: Reverse a list in place
# ### .reverse()
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/cde2807d-9151-4515-aa05-e83640c57712/Unit2_Section3.3b_reverse_lists.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/cde2807d-9151-4515-aa05-e83640c57712/Unit2_Section3.3b_reverse_lists.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# ```python
# cities_1 = ["Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# 
# print("regular", cities_1)
# cities_1.reverse()
# print("reversed", cities_1)
# ```
# 

# ### Examples

# In[11]:


# [ ] review and run example
cities_1 = ["Dubai", "Mexico City", "São Paulo", "Hyderabad"]

print("regular", cities_1)
cities_1.reverse()
print("reversed", cities_1)


# In[12]:


# [ ] review and run example
all_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("regular list",all_num, "\n")
all_num.reverse()
print("reverse list",all_num, "\n")
num_len = len(all_num)

print("Three Multiple")
for num in all_num:
    if num/3 == int(num/3):
        print(num)
    else:
        pass
    


# In[13]:


# [ ] review and run example
# create a list of  numbers by casting a range 
count_list = list(range(21))
print("before list", count_list)

# and reverse
count_list.reverse()
print("after list", count_list)


# ## Task 2: .reverse()

# In[15]:


# [ ] create and  print a list of multiples of 5 from 5 to 100
# { ] reverse the list and print
m = []
for x in range(5,101,5):
    m += [x]
print(m)
m.reverse()
print(m)


# In[23]:


# [ ] Create two lists: fours & more_fours containing multiples of four from 4 to 44
# [ ] combine and print so that the output is mirrored [44, 40,...8, 4, 4, 8, ...40, 44]
f = []
for x in range(4,45,4):
    f += [x]
mF = f
f.reverse()
print(f + mF)


# ## Concept: .sort() and sorted()
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/375c6bd9-9f91-4a3c-9a67-c01c35ea64ff/Unit2_Section3.3c_sort_sorted.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/375c6bd9-9f91-4a3c-9a67-c01c35ea64ff/Unit2_Section3.3c_Sort_Sorted.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
#  
# 
# ### .sort() in place  
# **.sort()** - orders a list in place 
# ```python
# quiz_scores = [20, 19, 20, 15, 20, 20, 20, 18, 18, 18, 19]
# quiz_scores.sort()
# ```  
# 
# ### sorted() copy
# **sorted()** - creates an ordered list copy 
# ```python
# game_points = [3, 14, 0, 8, 21, 1, 3, 8]
# sorted_points = sorted(game_points)
# ```

# ### Examples: .sort() and sorted()

# In[24]:


# [ ] review and run example
quiz_scores = [20, 19, 20, 15, 20, 20, 20, 18, 18, 18, 19]

# use .sort()
quiz_scores.sort()

print("quiz_scores:", quiz_scores)


# In[25]:


# [ ] review and run example
game_points = [3, 14, 0, 8, 21, 1, 3, 8]

# use sorted()
sorted_points = sorted(game_points)

print("game_points:", game_points)
print("sorted_points:", sorted_points)


# In[26]:


# [ ] review and run example
cities_1 = ["Dubai", "Mexico City", "São Paulo", "Hyderabad"]

print("Unsorted", cities_1)
cities_1.sort()
print("Sorted", cities_1)


# ## Task 3: .sort() & sorted()

# In[29]:


# [ ] print cites from visited_cities list in alphbetical order using .sort()
# [ ] only print cities that names start "Q" or earlier
visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
visited_cities.sort()
print(visited_cities)
for x in visited_cities:
    if x[0] < "Q":
        print(x)
    else:
        break


# In[31]:


# [ ] make a sorted copy (sorted_cities) of visited_cities list
# [ ] remove city names 5 characters or less from sorted_cities 
# [ ] print visitied cites and sorted cities
vC = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
sC = sorted(vC)
for x in sC:
    if len(x) <= 5:
        sC.remove(x)
print(vC)
print(sC)


# ## Task 3 (program): Merge & Sort Animals
# Create a program that 
# - takes user to build a list: add_animals 
# - merges add_anmials with exisiting list: anmimals
# - provides a sorted list to view in alpa or reverse alpha order

# 
# <font size="4" color="#B24C00"  face="verdana"> <B>step 1 </B></font> get user input to build add_animals list
# 

# In[1]:


# [ ] build a list (add_animals) using a while loop, stop adding when an empty string is entered
add_animals = []
while 1:
    i = input()
    if i:
        add_animals += [i]
    else:
        break
print(add_animals)


# 
# <font size="4" color="#B24C00"  face="verdana"> <B>step 2 </B></font> Merge the lists: add_animals into animals
# 

# In[8]:


# [ ] extend the lists into animals, then sort 
animals = ["Chimpanzee", "Panther", "Wolf", "Armadillo"]
animals.extend(add_animals)
animals.sort()
print(animals)


# 
# <font size="4" color="#B24C00"  face="verdana"> <B>step 3 </B></font> Allow animals list to be viewed alpha or reverse alpha order
# 

# In[14]:


# [ ] get input if list should be viewed alpha or reverse alpha and display list
if input("reverse alpha?").lower().startswith("y"):
    print(sorted(animals,reverse = True))
else:
    print(sorted(animals))


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
