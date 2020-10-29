#!/usr/bin/env python
# coding: utf-8

# # Section 1.4
# ## String Methods
# - Accessing string characters with index
# - Accessing substrings with index slicing
# - Iterating through characters of a string
# - **More string methods**
# 
# ----- 
# 
# ### Student will be able to
# - Work with string characters
# - Slice strings into substrings
# - Iterate through string characters
# - **Use string methods**
#   - `len()`
#   - `.count()`
#   - `.find()`

# ## Concept: Methods of Returning String Information
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c300e46e-b3c7-4bbf-8117-e72b33998cd3/Unit2_Section1.4a-String_Methods-Length.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c300e46e-b3c7-4bbf-8117-e72b33998cd3/Unit2_Section1.4a-String_Methods-Length.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### len()  
# Returns a string's length. 
# ### .count()  
# Returns the number of times a character or substring occurs.
# ### .find()   
# Returns index of first character or substring match.
# Returns **-1** if no match found.
# 
# ```python
# work_tip = "save your code"
# 
# # number of characters
# len(work_tip)
# 
# # letter "e" occurrences
# work_tip.count("e")
# 
# # find the index of the first space
# work_tip.find(" ")
# 
# # find the index of "u" searching a slice work_tip[3:6]
# work_tip.find("u",3,6)
# ```  
# These methods **return** information that we can use to sort or manipulate strings.

# ### Examples  
# Run each example cell in order.

# In[2]:


# [ ] review and run example
work_tip = "save your code"

print("number of characters in string")
print(len(work_tip),"\n")

print('letter "e" occurrences')
print(work_tip.count("e"),"\n")

print("find the index of the first space")
print(work_tip.find(" "),"\n")

print('find the index of "u" searching a slice work_tip[3:9] -', work_tip[3:9])
print(work_tip.find("u",3,9),"\n")

print('find the index of "e" searching a slice work_tip[4:] -', work_tip[4:])
print(work_tip.find("e",4))


# ### len()  
# Returns a string's length.

# In[3]:


# [ ] review and run example
work_tip = "good code is commented code"

print("The sentence: \"" + work_tip + "\" has character length = ", len(work_tip) )


# In[4]:


# [ ] review and run example
# find the middle index
work_tip = "good code is commented code"
mid_pt = int(len(work_tip)/2)

# print 1st half of sentence
print(work_tip[:mid_pt])

# print the 2nd half of sentence
print(work_tip[mid_pt:])


# ### .count()  
# Returns the number of times a character or substring occurs.

# In[5]:


# [ ] review and run example
print(work_tip)
print("how many w's? ", work_tip.count("w"))
print("how many o's? ", work_tip.count("o"))
print("uses 'code', how many times? ", work_tip.count("code"))


# In[6]:


# [ ] review and run example 
print(work_tip[:mid_pt])
print("# o's in first half")
print(work_tip[:mid_pt].count("o"))

print()
print(work_tip[mid_pt:])
print("# o's in second half")
print(work_tip[mid_pt:].count("o"))


# ### .find(*string*) 
# Returns index of first character or substring match  .
# Returns **-1** if no match found.
# #### .find(*string*, *start index*, *end index*)
# Same as above .find() but searches from optional start and to optional end index.

# In[7]:


# [ ] review and run example 
work_tip = "good code has meaningful variable names"
print(work_tip)
# index where first instance of "code" starts
code_here = work_tip.find("code")
print(code_here, '= starting index for "code"')


# In[8]:


# [ ] review and run example 
# set start index = 13 and end index = 33
print('search for "meaning" in the sub-string:', work_tip[13:33],"\n")
meaning_here = work_tip.find("meaning",13,33)
print('"meaning" found in work_tip[13:33] sub-string search at index', meaning_here)


# In[9]:


# [ ] review and run example 
# if .find("o") has No Match, -1 is returned
print ("work_tip:" , work_tip)
location = work_tip.find("o")

# keeps looping until location = -1 (no "o" found)
while location >= 0:
    print("'o' at index =", location)
    # find("o", location + 1) looks for a "o" after index the first "o" was found
    location = work_tip.find("o", location + 1)
print("no more o's")


# ## Task 1: `len()`

# In[14]:


# [ ] use len() to find the midpoint of the string 
# [ ] print the halves on separate lines
random_tip = "wear a hat when it rains"
midPt = int(len(random_tip)/2)
print(random_tip[:midPt]+"\n"+random_tip[midPt:])


# ## Task 2: `.count()`

# In[15]:


# for letters: "e" and "a" in random_tip
# [ ] print letter counts 
# [ ] BONUS: print which letter is most frequent
random_tip = "wear a hat when it rains"
print(random_tip.count('e'))
print(random_tip.count('a'))


# ## Task 3: `.find()`

# In[17]:


# [ ] print long_word from the location of the first and second "t"
long_word = "juxtaposition"
print(long_word[long_word.find("t"):])
print(long_word[long_word.find("t",long_word.find("t") + 1):])


# ## Task 4 (program): Print each word in a quote
# ```python
# start = 0
# space_index = quote.find(" ")
# while space_index != -1:
#     # code to print word (index slice start:space_index)
# ```

# In[19]:


quote = "they stumble who run fast"
while " " in quote:
    s = quote.find(" ")
    print(quote[:s])
    quote = quote[s+1:]
print(quote)


# In[9]:


quote = "they stumble who run fast"
start = 0
space = 0
while space != -1:
    space = quote.find(" ",start)
    if len(quote[start:]) > 4:
        print(quote[start:space])
    if space != -1:
        start = space + 1
print(quote[start:])


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
