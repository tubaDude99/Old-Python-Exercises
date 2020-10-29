#!/usr/bin/env python
# coding: utf-8

# # Section 3.1
# ## The Power of List Iteration
# - **for in: `for` loop using `in`**
# - for range: `for range(start,stop,step)` 
# - More list methods: `.extend()`, `+, .reverse(), .sort()` 
# - Strings to lists,`.split()`, and list to strings, `.join()` 
# ----- 
# 
# ### Student will be able to
# - **Iterate through lists using `for` with `in`**
# - Use `for range()` in looping operations 
# - Use list methods `.extend()`, `+, .reverse(), .sort()` 
# - Convert between lists and strings using `.split()` and `.join()` 

# ## Concept: Iterate through Lists using ` for in`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/3545f443-d2b5-4d77-9a8c-cfe07976c697/Unit2_Section3.1a-Iterate_through_Lists.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/3545f443-d2b5-4d77-9a8c-cfe07976c697/Unit2_Section3.1a-Iterate_through_Lists.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ```python
# cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# 
# for city in cities:
#     print(city)
# ```

# ### Examples

# In[1]:


# [ ] review and run example
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]

for city in cities:
    print(city)


# In[3]:


# [ ] review and run example
sales = [6, 8, 9, 11, 12, 17, 19, 20, 22]
total = 0

for sale in sales:
    total += sale
    
print("total sales:", total)
    


# change the iterator variable name from "sale" to "dollars" or to any valid name

# In[4]:


# [ ] review and run example 
sales = [6, 8, 9, 11, 12, 17, 19, 20, 22]
total = 0

for dollars in sales:
    total += dollars
    
print("total sales:", total)


# ## Task 1: Iterate through Lists using `in`

# In[5]:


# [ ] create a list of 4 to 6 strings: birds
# print each bird in the list
birds = ["chickadee", "cardinal", "robin", "bluejay", "hawk"]
for i in birds:
    print(i)


# In[6]:


# [ ]  create a list of 7 integers: player_points
# [ ] print double the points for each point value
pPnts = [34,1,987,50,21,54,77]
for i in pPnts:
    print(i * 2)


# In[7]:


# [ ] create long_string by concatenating the items in the "birds" list previously created
# print long_string - make sure to put a space betweeen the bird names
lStr = ""
for w in birds:
    lStr += w + " "
print(lStr)


# ## Concept: Sort and Filter
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/32652fe3-7d3e-4b7b-b9fb-7f87a6c0ad59/Unit2_Section3.1b-Sort_and_Filter.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/32652fe3-7d3e-4b7b-b9fb-7f87a6c0ad59/Unit2_Section3.1b-Sort_and_Filter.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### use comparison operators while iterating lists
# 

# ### Examples

# In[8]:


# [ ] review and run example of sorting into strings to display
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
longer_names = ""
shorter_names = ""

for bone_name in foot_bones:
    if len(bone_name) < 10:
        shorter_names += "\n" + bone_name
    else:
        longer_names += "\n" + bone_name

print(shorter_names)
print(longer_names)


# In[9]:


# [ ] review and run example of sorting into lists
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
longer_names = []
shorter_names = []

for bone_name in foot_bones:
    if len(bone_name) < 10:
        shorter_names.append(bone_name)
    else:
        longer_names.append(bone_name)

print(shorter_names)
print(longer_names)


# ## Task 2: Sort and filter

# In[11]:


# [ ] Using cities from the example above iterate throught the list using "for"/"in"
# [ ] Print only cities starting with "m"
for c in cities:
    if c.lower().startswith("m"):
        print(c)


# In[13]:


# [ ] Using cities from the example above iterate throught the list using "for"/"in"
# cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# [ ] sort into lists with "A" in the city name and without "A" in the name: a_city & no_a_city
a = []
noA = []
for c in cities:
    if 'a' in c.lower():
        a += [c]
    else:
        noA += [c]
print(a)
print()
print(noA)


# ## Concept: More List Iteration
# ### - Counting
# ### - Searching
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/72acdbd5-454d-4900-b381-387ad49596f1/Unit2_Section3.1c_count_in_iteration.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/72acdbd5-454d-4900-b381-387ad49596f1/Unit2_Section3.1c_count_in_iteration.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### use string methods while iterating lists

# ### Examples

# In[14]:


# [ ] review and run example
# iterates the "cities" list, count & sum letter "a" in each city name

cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
search_letter = "a"
total = 0

for city_name in cities:
    total += city_name.lower().count(search_letter)

print("The total # of \"" + search_letter + "\" found in the list is", total)


# ### Search function
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/2fa709be-5857-4291-beee-4d893d93468e/Unit2_Section3.1d_city_search_function.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/2fa709be-5857-4291-beee-4d893d93468e/Unit2_Section3.1d_city_search_function.vtt","srclang":"en","kind":"subtitles","label":"english"}])

# In[15]:


# [ ] review and run example
# city_search function has a default list of cities to search
def city_search(search_item, cities = ["New York", "Shanghai", "Munich", "Tokyo"] ):
    for city in cities:
        if city.lower() == search_item.lower():
            return True
        else:
            # go to the next item
            pass
    # no more items in list
    return False

# a list of cities
visited_cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]

search = input("enter a city visited: ")

# Search the default city list
print(search, "in default cities is", city_search(search))

# search the list visited_cities using 2nd argument
print(search, "in visitied_cites list is", city_search(search,visited_cities))


# ## Task 3 (program): Paint Stock  
# Check a list for a paint color request and print status of color "found"/"not found".
# - Create list, paint_colors, with 5+ colors
# - Get user input of string:color_request
# - Iterate through each color in paint_colors to check for a match with color_request

# In[17]:


# [ ] complete paint stock
pCol = ['green','blue','red','yellow','indigo']
if input("What color do you want? ").lower() in pCol:
    print("Color found!")
else:
    print("Color not found.")


# ## Task 4 (program): Foot Bones Quiz
# **Create a function** that will iterate through foot_bones looking for a match of a string argument
# - Call the function 2 times with the name of a footbone 
# - print immediate feedback for each answer (correct - incorrect)
# - print the total # of foot_bones identified
# 
# 
# The program will use the foot_bones list:
# ```python 
# foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
#              "intermediate cuneiform", "medial cuneiform"]
# ```
# Bonus: remove correct response item from list if correct so user cannot answer same item twice

# In[8]:


# [ ] Complete Foot Bones Quiz
# foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
#             "intermediate cuneiform", "medial cuneiform"]
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]
x = 0
def bones(bone):
    if bone in foot_bones:
        print("correct")
        x = 1
    else:
        print("incorrect")
        x = 0
    return(x)
x += bones(input("Name a bone: "))
x += bones(input("Name a bone: "))
print(x)


# In[9]:


# [ ] bonus version
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]
x = 0
def bones(bone):
    if bone in foot_bones:
        print("correct")
        foot_bones.remove(bone)
        x = 1
    else:
        print("incorrect")
        x = 0
    return(x)
x += bones(input("Name a bone: "))
x += bones(input("Name a bone: "))
print(x)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
