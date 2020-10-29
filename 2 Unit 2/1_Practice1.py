#!/usr/bin/env python
# coding: utf-8

# # Module 1 Lab
# ## Sequence Index Practice
# 
# -----
# 
# ### Student will be able to
# - Work with string characters
# - Slice strings into substrings
# - Iterate through string characters
# - Use string methods

# ## Task 1: Access String Characters 
# ### `working_string[index]`
# 

# In[4]:


# [ ] access and print the second character from planet_name: "u"
planet_name = "Jupiter"
print(planet_name[1])


# In[5]:


# [ ] access and print the first character from planet_name: "J"
planet_name = "Jupiter"
print(planet_name[0])


# In[7]:


# [ ] access and print the first and last characters from planet_name
planet_name = "Jupiter"
print(planet_name[0] + planet_name[-1])


# In[8]:


# [ ] using a negative index access and print the first character from planet_name: "J"
planet_name = "Jupiter"
print(planet_name[-1*len(planet_name)])


# ## Task 2: Slice
# ### `working_string[start:stop]`
# ### `working_string[start:stop:step]`

# In[1]:


# [ ] print planet_name sliced into the first 3 characters and remaining characters
planet_name = "Neptune"
print(planet_name[0:3],planet_name[3:])


# In[4]:


# [ ] print 1st char and then every 3rd char of wise_words
# use string slice with a step
wise_words = 'Play it who opens'
print(wise_words[::3])


# In[5]:


# [ ] print planet_name in reverse
print(planet_name[::-1])


# In[7]:


work_tip = "Good code is commented code"
# [ ] find the number of 0's in the first half (slice) of work_tip
print(work_tip[:int(len(work_tip)/2)].count("0"))


# In[8]:


# [ ] print a substring of code_tip set start index = 13 and end index = 25
code_tip = "code a conditional decision like you would say it"
print(code_tip[13:25])


# ## Task 3: Iterate a String
# ### `for letter in sentence:`

# In[9]:


# [ ] Get user input for 1 fav_food
# [ ] iterate through letters in fav_food 
#    - print each letter on a new line
fFood = input()
for l in fFood:
    print(l)


# In[10]:


# [ ] iterate work_tip string concatenate each letter to variable: new_string 
# [ ] concatenate the letter or a "-" instead of a space " "
# tip: concatenate string example: word = word + "a"
work_tip = "Good code is commented code"
nStr = ""
for l in work_tip:
    if l == " ":
        nStr += "-"
    else:
        nStr += l
print(nStr)


# In[11]:


# [ ] Print the first 4 letters of name on new line
name = "Hiroto"
for l in name[0:4]:
    print(l)


# In[ ]:


# [ ] Print every other letter from 2nd to last letter of name 
name = "Hiroto"
for l in name[-1:0:-2]:
    print(l)


# 

# ## Task 4 (program): Mystery Name
# - Get user input for first_name
# - Create an empty string variable: new_name
# - Iterate through letters in first_name Backwards 
#   - Add each letter to new_name as you iterate
#   - Replace the letter if "e", "t" or "a" with "?" *(hint: if, elif, elif, else)*
# - Print new_name  
# 
# **example: "Alton" = "no?l?"**

# In[1]:


# [ ] Create Mystery Name
fName = input()
nName = ""
for l in fName[::-1]:
    if l in "eta":
        nName += "?"
    else:
        nName += l
print(nName)


# ## Task 5: `len(), .find(), .count()`   
# 
# ```  
# - len(working_string)
# - .find("i")
# - .find("i",start)
# - .find("i", start, end)
# - .count("i")
# - .count("i", start)
# - .count("i", start, end)
# ```   

# In[2]:


# [ ] find and display the length of the string: topic
topic = ".find() returns the length of a string"
print(len(topic))


# In[3]:


# [ ] use len() to find and display the mid_pt (middle) index (+/- 1) of the string: topic
# note: index values are whole numbers
topic = "len() can take a sequence, like a string, as an argument"
print(int(len(topic)/2))


# In[4]:


# [ ] print index where first instance of the word  "code" starts using .find()
work_tip = "Good code is commented code"
print(work_tip.find("code"))


# In[5]:


# [ ] search for "code" in code_tip using .find() 
# [ ] search substring with substring index start= 13,end = last char 
# [ ] save result in varible: code_index
# [ ] display index of where "code" is found, or print "not found" if code_index == -1
work_tip = "Good code is commented code"
work_tip.find("code")
cIndx = work_tip.find("code",13)
if cIndx == -1:
    print("not found")
else:
    print(cIndx)


# ## Task 6

# In[6]:


# [ ] find and report (print) number of w's, o's + use of word "code"
work_tip = "Good code is commented code"
print(work_tip.count("w"))
print(work_tip.count("o"))
print(work_tip.count("code"))


# In[7]:


# [ ]  count times letter "i" appears in code_tip string
# [ ] find and display the index of all the letter i's in code_tip
# Remember: if .find("i") has No Match, -1 is returned
code_tip = "code a conditional decision like you would say it"
print ("code_tip:" , code_tip)
print(code_tip.count("i"))
while code_tip.find("i") != -1:
    print(code_tip.find("i"))
    code_tip = code_tip.replace("i","1",1)
    


# ## Task 7 (program): Words after "G"/"g"
# Create a program that inputs a quote (a sentence without punctuation) and prints all of the words that start with h-z.
# - Split the words by building a placeholder variable: word, and adding a letter each loop until a non-alpha char is encountered
# - **if** non-alpha detected (space, punctuation, digit,...) defines the end of a word
# - **else, check if** word is greater than "g" alphabetically, print word and set word = empty string
# - or **else** set word = empty string and build the next word  
# 
# Hint: use `.lower()`.

# In[11]:


# [] create words after "G"
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
words = ['']
quote = input("Quote: ")
i = 0
for l in quote:
    if l == ' ':
        i += 1
        words += ['']
    elif l.isalpha():
        words[i] += l
for w in words:
    if w.lower() > "g":
        print(w)


# In[14]:


quote = input("Quote: ")
word = ""
for l in quote:
    if not(l.isalpha()):
        if word.lower() > "g":
            print(word)
        word = ""
    else:
        word += l  
print(word)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
