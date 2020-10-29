#!/usr/bin/env python
# coding: utf-8

# # Section 2.3
# ## List Insert 
# 
# - List Creation
# - List Access
# - List Append
# - **List Modify and Insert**
# - List Delete
# ----- 
# 
# ### Student will be able to
# - Create lists
# - Access items in a list
# - Add items to the end of a list
# - **Modify and insert items into a list**
# - Delete items from a list

# ## Concept: Insert a new value for an index
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/219b35cf-03b5-4b57-8fbc-f5864281312d/Unit2_Section2.3a-Overwriting_an_Index.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/219b35cf-03b5-4b57-8fbc-f5864281312d/Unit2_Section2.3a-Overwriting_an_Index.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Overwrite a specific index in a list
# ```python
# party_list[2] = "Tobias"
# ```
# - **Overwrites** existing index
# - **Cannot** use to **Append** a new index to the list
# 

# ### Examples

# In[1]:


# [ ] review and run example
# the list before Insert
party_list = ["Joana", "Alton", "Tobias"]
print("party_list before: ", party_list)

# the list after Insert
party_list[1] = "Colette"
print("party_list after:  ", party_list)


# In[2]:


# [ ] review and run example
party_list = ["Joana", "Alton", "Tobias"]
print("before:",party_list)

# modify index value
party_list[1] = party_list[1] + " Derosa"
print("\nafter:", party_list)


# ### Example: **IndexError**  

# In[3]:


# IndexError Example
# [ ] review and run example which results in an IndexError
# if result is NameError run cell above before running this cell

# IndexError trying to append to end of list
party_list[3] = "Alton"
print(party_list)


# In[4]:


# [ ] review and run example changes the data type of an element
# replace a string with a number (int)
single_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
print("single_digits: ", single_digits)
print("single_digits[3]: ", single_digits[3], type(single_digits[3]),"\n")

# replace string with an int
single_digits[3] = 3
print("single_digits: ", single_digits)
print("single_digits[3]: ", single_digits[3], type(single_digits[3]))


# ## Task 1: Replace items in a list
# - Create a list, **`three_num`**, containing 3 single digit integers
# - Print three_num
# - Check if index 0 value is < 5
#   - if < 5 , replace index 0 with a string: "small"
#   - else, replace index 0 with a string: "large"
# - Print three_num

# In[6]:


# [ ] complete "replace items in a list" task
threeNum = [1,2,3]
print(threeNum)
if threeNum[0] < 5:
    threeNum[0] = "small"
else:
    threeNum[0] = "large"
print(threeNum)


# ## Function Challenge: Create replacement function
# - Create a function, **str_replace**, that takes 2 arguments: int_list and index 
#   - int_list is a list of single digit integers
#   - index is the index that will be checked - such as with int_list[index]
# - Function replicates purpose of task "replace items in a list" above and replaces an integer with a string "small" or "large"
# - Return str_list
# 
# Test the function!

# In[7]:


# [ ]  create challenge function
def strReplace(intL,indx):
    if intL[indx] < 5:
        intL[indx] = "small"
    else:
        intL[indx] = "large"
    return(intL)
print(strReplace([3,5,8,2,6],2))


# ## Task 2: Modify items in a list
# - Create a list, **`three_words`**, containing 3 different capitalized word strings
# - Print three_words
# - Modify the first item in three_words to uppercase
# - Modify the third item to swapcase
# - Print three_words

# In[10]:


# [ ] complete coding task described above
threeW = ["Laurel","Board","Table"]
print(threeW)
threeW[0] = threeW[0].upper()
threeW[2] = threeW[2].swapcase()
print(threeW)


# ## Concept: Insert items into a list
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/659b9cd2-1e84-4ead-8a69-015c737577cd/Unit2_Section2.3b-Inserting_Items_into_Lists.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/659b9cd2-1e84-4ead-8a69-015c737577cd/Unit2_Section2.3b-Inserting_Items_into_Lists.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Use `.insert()` to define an index to insert an item
# ```python
# party_list.insert(2,"Tobias")
# ```
# - Inserts, **doesn't overwrite**
# - **Increases index by 1**, at and above the insertion point
# - **Can** use to **Append** a new index to the end of the list
# 

# ### Examples

# In[11]:


# [ ] review and run example
# the list before Insert
party_list = ["Joana", "Alton", "Tobias"]
print("party_list before: ", party_list)
print("index 1 is", party_list[1], "\nindex 2 is", party_list[2], "\n")

# the list after Insert
party_list.insert(1,"Colette")
print("party_list after:  ", party_list)
print("index 1 is", party_list[1], "\nindex 2 is", party_list[2], "\nindex 3 is", party_list[3])


# ## Task 3: `insert()` input into a list 

# In[12]:


# [ ] insert a name from user input into the party_list in the second position (index 1)
party_list = ["Joana", "Alton", "Tobias"]
party_list.insert(1,input())
# [ ] print the updated list
print(party_list)


# ## Task 4: Fix the error
# 

# In[14]:


# [ ] Fix the Error
tree_list = ["oak"]
print("tree_list before =", tree_list)
tree_list.insert(1,"pine")
print("tree_list after  =", tree_list)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
