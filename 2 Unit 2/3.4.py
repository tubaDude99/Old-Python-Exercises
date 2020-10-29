#!/usr/bin/env python
# coding: utf-8

# # Section 3.4
# # Between Strings and Lists
# - for in: `for` loop using `in`
# - for range: `for range(start,stop,step)` 
# - More list methods: `.extend()`, `+, .reverse(), .sort()` 
# - **Strings to lists,`.split()`, and list to strings, `.join()`**
# - **List cast & `print("hello", end='')`**
# 
# 
# ----- 
# 
# ### Student will be able to
# - Iterate through lists using `for` with `in`
# - Use `for range()` in looping operations 
# - Use list methods `.extend()`, `+, .reverse(), .sort()` 
# - **Convert between lists and strings using  `.split()` and `.join()`**
# - **Cast strings to lists / direct multiple print outputs to a single line**

# ## Concept: Converting a string to a list with `.split()`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/1a076a9c-842f-455f-91bf-48db837842e8/Unit2_Section3.4a-Split_on_Breaks.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/1a076a9c-842f-455f-91bf-48db837842e8/Unit2_Section3.4a-Split_on_Breaks.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### `.split()`  by default, splits a string at spaces (" ") to create a list
# ```python
# tip = "Notebooks can be exported as .pdf"
# tip_words = tip.split()
# 
# for word in tip_words:
#     print(word)
# ```

# ### Examples

# In[1]:


# [ ] review and run example
tip = "Notebooks can be exported as .pdf"
tip_words = tip.split()

print("STRING:", tip)
print("LIST:", tip_words, "\n")

for word in tip_words:
    print(word)


# In[2]:


# [ ] review and run example
rhyme = "London bridge is falling down"

rhyme_words = rhyme.split()

rhyme_words.reverse()

for word in rhyme_words:
    print(word)


# ## Task 1: Using `.split()`

# In[3]:


# [ ] split the string(rhyme) into a list of words (rhyme_words)
# [ ] print each word on it's own line
rhyme = 'Jack and Jill went up the hill To fetch a pail of water' 
rWords = rhyme.split()
for x in rWords:
    print(x)


# In[4]:


# [ ] split code_tip into a list and print the first and every other word
code_tip = "Python uses spaces for indentation"
cTip = code_tip.split()
for x in cTip[0::2]:
    print(x)


# ## Concept: `.split('-')`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/55d37e65-fb49-4bf5-87f8-fb987d3ce7a4/Unit2_Section3.4b-Split_on_Strings.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/55d37e65-fb49-4bf5-87f8-fb987d3ce7a4/Unit2_Section3.4b-Split_on_Strings.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### To split on characters other than " " (space), provide `.split()` a string argument to use as break points
# ```python 
# code_tip = "Python-uses-spaces-for-indentation"
# tip_words = code_tip.split('-')
# ```

# ### Examples
# #### `.split('-') : split with an argument

# In[5]:


# [ ] review and run example
code_tip = "Python-uses-spaces-for-indentation"
tip_words = code_tip.split('-')

print(tip_words)


# In[6]:


# [ ] review and run example - study the list print output
code_tip = "Python uses spaces for indentation"

# split on "a"
tip_words = code_tip.split('a')
print(code_tip)
print(tip_words)


# In[7]:


# [ ] review and run example
# triple quotes ''' ''' preserve formatting such as spaces and line breaks
big_quote = """Jack and Jill went up the hill
To fetch a pail of water
Jack fell down and broke his crown
And Jill came tumbling after"""

# split on line breaks (\n)
quote_lines = big_quote.split('\n')
print(quote_lines, '\n')

# print the list in reverse with index slicing
for line in quote_lines[::-1]:
    print(line)


# ## Task 2: `.split()`

# In[10]:


# [ ] split poem into a list of phrases by splitting on "*" a
# [ ] print each phrase on a new line in title case
poem = "Write code frequently*Save code frequently*Comment code frequently*Study code frequently*"
poems = poem.split("*")
for x in poems:
    print(x)


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B></B></font>  
# 
# ## Concept: Build a string from a list
# ### `.join()`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/57decc97-801f-4f7e-8ab6-69a47cf1be7b/Unit2_Section3.4c-Build_using_Join_Sequence.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/57decc97-801f-4f7e-8ab6-69a47cf1be7b/Unit2_Section3.4c-Build_using_Join_Sequence.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### `.join()` is a method applied to a separator string and iterates through its argument
# ```python
# tip_words = ['Notebooks', 'can', 'be', 'exported', 'as', '.pdf'] 
# 
# " ".join(tip_words)
# ```
# A space (" ") is the separator that gets injected between the objects in the argument (the list "tip_words").

# ### Examples: `.join()`

# In[11]:


# [ ] review and run example
tip_words = ['Notebooks', 'can', 'be', 'exported', 'as', '.pdf'] 

# join tip_words objects with spaces
print(" ".join(tip_words))


# In[12]:


# [ ] review and run example
no_space = ""
letters = ["P", "y", "t", "h", "o", "n"]
print(no_space.join(letters))


# In[13]:


# [ ] review and run example - .join() iterates through sequences
dash = "-"
space = " "
word = "Iteration"
ellipises = "..."

dash_join = dash.join(word)
print(dash_join)
print(space.join(word))
print(ellipises.join(word))


# ## Task 3: `.join()`

# In[1]:


# [ ] .join() letters list objects with an Asterisk: "*"
letters = ["A", "s", "t", "e", "r", "i", "s", "k"]
print("*".join(letters))


# ## Task 4 (program): Choose the separator
# - get user input on what to use to join words (" ", *, -, etc...) - store in variable: separator
# - join pharse_words with the separator and print

# In[2]:


# [ ] complete Choose the separator
phrase_words = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill', 'To', 'fetch', 'a', 'pail', 'of', 'water']
s = input('Seperator? ')
print(s.join(phrase_words))


# ## Concept: More Python string tools
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/aa6eaea3-a3cb-41d8-aee3-280d01a9f4f0/Unit2_Section3.4d-Useful_String_Tricks.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/aa6eaea3-a3cb-41d8-aee3-280d01a9f4f0/Unit2_Section3.4d-Useful_String_Tricks.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Cast a string to a list of characters  
# ```python
# hello_letters = list("Hello")
# ```
# ### Print to the same line with multiple print statements (`end=`)
# Or insert any character as an end in print("String", end="+").
# ```python
# print('Hello', end = '')
# print('world')
# ```

# ### Examples

# In[3]:


# [ ] review and run example
hello_letters = list("Hello")
print(hello_letters)


# In[4]:


# [ ] review and run example
# cast sting to list
word_letters = list("concatenates")

# .join() concatenates the list
# print on same line setting the end character
print('~'.join(word_letters))


# In[5]:


# [ ] review and run example
print("Hello ", end = '')
print("world")


# In[6]:


# [ ] review and run example
# This  is the default print end
print("Hello World!", end="\n")
print('still something to learn about print()')


# In[7]:


# [ ] review and run example
# end inserts any valid str character: A-z, 0-9,!,@,*,\n,\t or ''(empty string)...
for letter in "Concatenation":
    print(letter, end='*')


# ## Task 5: `end=" " ` configuration in printing
# `print('The String', end='')`

# In[8]:


# [ ] use 3 print() statements to output text to one line 
# [ ] separate the lines by using "- " (dash space)
print("The first text", end='- ')
print("The second text", end='- ')
print("The third text", end='- ')


# ## Task 6: cast str to list
# `Msg_characters = list("Always test your code")`

# In[10]:


# [ ] create a string (fact) of 20 or more characters and cast to a list (fact_letters)
# [ ] iterate fact, printing each char on one line, except for spaces print a new line
fact = list("stringof20ormorecharacters")
for f in fact:
    print(f)


# ## Task 7 (program): Add the digits
# - Create a 20 digit string, and cast to a list
# - Then add all the digits as integers
# - Print the equation and answer  
# 
# Hint: use cast to sum the digits, and .join() to create the equation (1+2+3+...)

# In[11]:


# [ ] create add the digits
a = list("12345678901234567890")
t = 0
for x in a:
    t += int(x)
print(" + ".join(a), "=", t)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
