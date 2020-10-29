#!/usr/bin/env python
# coding: utf-8

# # Section 2.4
# ## List Delete
# - List Creation
# - List Access
# - List Append
# - List Insert
# - **List Delete (`del`, `.pop()` and `.remove()`)**
# 
# ----- 
# 
# ### Student will be able to
# 
# - Create lists
# - Access items in a list
# - Add items to the end of a list
# - Modify and insert items into a list
# - **Delete items from a list with `del`, `.pop()` & `.remove()`**

# ## Concept: Delete a specific list index
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/072d8761-7811-438e-a77f-72c9634c0f8c/Unit2_Section2.4a-Deleting_Specific_Index.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/072d8761-7811-438e-a77f-72c9634c0f8c/Unit2_Section2.4a-Deleting_Specific_Index.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### `del ` statement  
# ```python
# del party_list[2]
# ```

# ### Examples

# In[1]:


# [ ] review and run example
# the list before delete
sample_list = [11, 21, 13, 14, 51, 161, 117, 181]
print("sample_list before: ", sample_list)

del sample_list[1]
# the list after delete
print("sample_list after:  ", sample_list)


# In[2]:


# [ ] review and run example Multiple Times
# [ ] consider how to reset the list values?
print("sample_list before:", sample_list)
del sample_list[0]
print("sample_list after:", sample_list)


# In[3]:


# [ ] review and run example
mixed_types = [1, "cat"]
# append number
mixed_types.append(3)
print("mixed_types list: ", mixed_types)

# append string
mixed_types.append("turtle")
print("mixed_types list: ", mixed_types)


# ## Task 1: `del` statement

# In[5]:


# [ ] print ft_bones list
# [ ] delete "cuboid" from ft_bones
# [ ] reprint list
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
print(ft_bones)
del(ft_bones[2])
print(ft_bones)


# ## Task 2: Multiple `del` statements 

# In[6]:


# [ ] print ft_bones list
# [ ] delete "cuboid" from ft_bones
# [ ] delete "navicular" from list
# [ ] reprint list
# [ ] check for deletion of "cuboid" and "navicular"
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
del(ft_bones[2])
del(ft_bones[2])
print(ft_bones)


# ## Concept: .pop() gets and deletes item in list
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/67b83f30-a92c-4d1f-a7a3-ca257dd4db4e/Unit2_Section2.4b-List_Pop_Method.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/67b83f30-a92c-4d1f-a7a3-ca257dd4db4e/Unit2_Section2.4b-List_Pop_Method.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### `.pop()`  method default is last item in a list
# ```python
# last_item = party_list.pop()
# first_item = party_list.pop(0)
# ```

# ### Examples

# In[7]:


# [ ] review and run example
# pop() gets the last item by default
party_list = ["Joana", "Alton", "Tobias"]
print(party_list)
print("Hello,", party_list.pop())

print("\n", party_list)
print("Hello,", party_list.pop())

print("\n", party_list)
print("Hello,", party_list.pop())

print("\n", party_list)


# In[8]:


# [ ] review and run example
# can pop specific index like pop(3)
number_list = [11, 21, 13, 14, 51, 161, 117, 181]
print("before:", number_list)
number_list.pop(3)
print("after :", number_list)


# In[9]:


# [ ] review and run example
# set a variable to a poped value
number_list = [11, 21, 13, 14, 51, 161, 117, 181]
print("list before:", number_list)
num_1 = number_list.pop()
num_2 = number_list.pop()
print("list after :", number_list)
print("add the popped values:", num_1, "+", num_2, "=", num_1 + num_2)


# ## Task 3: `pop()`

# In[3]:


# [ ] pop() and print the first and last items from the ft_bones list
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
print(ft_bones.pop(0))
print(ft_bones.pop())
# [ ] print the remaining list
print(ft_bones)


# ## Concept: An empty list is False
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/20e00a13-a9d2-4a35-b75d-f6533fa15cbd/Unit2_Section2.4c-Empty_List_is_False.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/20e00a13-a9d2-4a35-b75d-f6533fa15cbd/Unit2_Section2.4c-Empty_List_is_False.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### in a conditional an empty list will evaluate `False`
# This allows creating a while loop that runs until a list is empty
# ```python
# while dog_types: 
# ```

# ### Example

# In[2]:


dog_types = ["Lab", "Pug", "Poodle"]

while dog_types: 
    print(dog_types.pop())


# ## Task 4 (Part 1): Cash Register Input
# - Create a empty list `purchase_amounts`
# - Populate the list with user input for the price of items
# - Continue adding to list with `while` until "done" is entered
#   - Can use `while True:` with `break`
# - Print `purchase_amounts`
# - Continue to Part 2

# In[1]:


#[ ] complete the Register Input task above
pAmt = []
while 1:
    p = input()
    if p == "done":
        break
    else:
        pAmt.append(p)
print(pAmt)


# ## Task 4 (Part 2): Cash Register Total
# - Create a **`subtotal`** variable = 0
# - Create a while loop that runs **`while`** purchase_amount (is not empty)
# - Inside the loop: 
#   - **`pop()`** the last list value cast as a float type
#   - Add the float value to a **`subtotal`** variable
# - After exiting the loop print **`subtotal`**  
#   
#   *Be sure to populate purchase_amounts by running Part 1 above.*

# In[3]:


# [ ] complete the Register Total task above
sT = 0
while pAmt:
    sT += float(pAmt.pop())
print(sT)


# ## Concept: Delete a specific object from a list with `.remove()`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/31fadf38-670c-4ba9-aa68-1934db459c4d/Unit2_Section2.4d-Removing_Object_from_List.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/31fadf38-670c-4ba9-aa68-1934db459c4d/Unit2_Section2.4d-Removing_Object_from_List.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### `.remove(object)` removes the 1st item that matches
# 
# ```python
# dog_types.remove("Pug")
# ```
# >**`ValueError`** occurs if the object is not available to be removed.  

# ### Examples

# In[4]:


# [ ] review and run example
dog_types = ["Lab", "Pug", "Poodle"]

if "Pug" in dog_types:
    dog_types.remove("Pug")
else:
    print("no Pug found")
print(dog_types)


# In[5]:


# [ ] review and run example
dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]

print(dogs)
while "Poodle" in dogs:
    dogs.remove("Poodle")
    print(dogs)


# ### ValueError

# In[7]:


# [ ] review and run example
# Change to "Lab", etc... to fix error
dogs.remove("Lab")
print(dogs)


# ## Task 3: `.remove()`

# In[8]:


# [ ] remove one "Poodle" from the list: dogs , or print "no Poodle found"
# [ ] print list before and after
dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]
print(dogs)
if "Poodle" in dogs:
    dogs.remove("Poodle")
else:
    print("no Poodle found")
print(dogs)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
