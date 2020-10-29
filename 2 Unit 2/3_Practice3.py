#!/usr/bin/env python
# coding: utf-8

# # 2-3 Intro Python Practice  
# ## power iteration of sequences
# 
# <font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>  
# - Iterate through Lists using **`for`** and **`in`**
# - Use **`for` *`count`* `in range()`** in looping operations  
# - Use list methods **`.extend()`, `+, .reverse(), .sort()`**  
# - convert between lists and strings using  **`.split()`** and **`.join()`**
# - cast strings to lists **/** direct multiple print outputs to a single line.  ** `print("hi", end='')`**

# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# ##  list iteration: `for in`
# ### `for item in list:`

# In[4]:


# [ ] print out the "physical states of matter" (matter_states) in 4 sentences using list iteration
# each sentence should be of the format: "Solid - is state of matter #1" 
matter_states = ['solid', 'liquid', 'gas', 'plasma']
for x in matter_states:
    print(x,"- is state of matter #%i" %(matter_states.index(x) + 1))


# In[7]:


# [ ] iterate the list (birds) to see any bird names start with "c" and remove that item from the list
# print the birds list before and after removals
birds = ["turkey", "hawk", "chicken", "dove", "crow"]
print(birds)
for b in birds:
    if b.startswith("c"):
        print(birds.pop(birds.index(b)))
print(birds)


# In[9]:


# the team makes 1pt, 2pt or 3pt baskets
# [ ] print the occurace of each type of basket(1pt, 2pt, 3pt) & total points using the list baskets
baskets = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]
t = 0
p = [0,0,0]
for b in baskets:
    t+=b
    p[b-1] += 1
print("There were %i 1-point baskets, %i 2-point baskets, and %i 3-point basket, for a total of %i points" %(p[0],p[1],p[2],t))


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# ##  iteration with `range(start)` & `range(start,stop)`
# 

# In[10]:


# [ ] using range() print "hello" 4 times
for x in range(4):
    print('hello')


# In[16]:


# [ ] find spell_list length
# [ ] use range() to iterate each half of spell_list  
# [ ] label & print the first and second halves
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
len(spell_list)
for x in spell_list[:int(len(spell_list)/2)]:
    print(x, end=', ')
print("\n")
for x in spell_list[int(len(spell_list)/2):]:
    print(x, end=', ')


# In[18]:


# [ ] build a list of numbers from 20 to 29: twenties 
# append each number to twenties list using range(start,stop) iteration
# [ ] print twenties
twenties = []
for x in range(20,30):
    twenties += [x]
print(twenties)


# In[19]:


# [ ] iterate through the numbers populated in the list twenties and add each number to a variable: total
# [ ] print total
t = 0
for x in twenties:
    t += x
print(t)


# In[20]:


# check your answer above using range(start,stop)
# [ ] iterate each number from 20 to 29 using range()
# [ ] add each number to a variable (total) to calculate the sum
# should match earlier task 
t = 0
for x in range(20,30):
    t += x
print(t)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# ##  iteration with `range(start:stop:skip)`
# 

# In[21]:


# [ ] create a list of odd numbers (odd_nums) from 1 to 25 using range(start,stop,skip)
# [ ] print odd_nums
# hint: odd numbers are 2 digits apart
o = []
for x in range(1,26,2):
    o += [x]
print(o)


# In[23]:


# [ ] create a Decending list of odd numbers (odd_nums) from 25 to 1 using range(start,stop,skip)
# [ ] print odd_nums,  output should resemble [25, 23, ...]
d = []
for x in range(25,0,-1):
    d += [x]
print(d)


# In[24]:


# the list, elements, contains the names of the first 20 elements in atomic number order
# [ ] print the even number elements "2 - Helium, 4 - Beryllium,.." in the list with the atomic number
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine',  'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon',  'Potassium', 'Calcium']
for x in range(1,20,2):
    print(elements[x])


# In[25]:


# [ ] # the list, elements_60, contains the names of the first 60 elements in atomic number order
# [ ] print the odd number elements "1 - Hydrogen, 3 - Lithium,.." in the list with the atomic number elements_60
elements_60 = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen',  'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon',  'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Hydrogen',  'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine',  'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine',  'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese',  'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium',  'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium']
for x in range(0,60,2):
    print(elements_60[x])


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4</B></font>
# ## combine lists with `+` and `.extend()`

# In[26]:


# [ ] print the combined lists (numbers_1 & numbers_2) using "+" operator
numbers_1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# pythonic casting of a range into a list
numbers_2 = list(range(30,50,2))

print("numbers_1:",numbers_1)
print("numbers_2",numbers_2)
print(numbers_1 + numbers_2)


# In[28]:


# [ ] print the combined element lists (first_row & second_row) using ".extend()" method
first_row = ['Hydrogen', 'Helium']
second_row = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']

print("1st Row:", first_row)
print("2nd Row:", second_row)
first_row.extend(second_row)
print(first_row)


# ## Project: Combine 3 element rows
# Choose to use **"+" or ".extend()" **to build output similar to   
# 
# ```
# The 1st three rows of the Period Table of Elements contain:
# ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']
# 
# The row breakdown is
# Row 1: Hydrogen, Helium
# Row 2: Lithium, Beryllium, Boron, Carbon, Nitrogen, Oxygen, Fluorine, Neon
# Row 3: Sodium, Magnesium, Aluminum, Silicon, Phosphorus, Sulfur, Chlorine, Argon
# ```

# In[30]:


# [ ] create the program: combined 3 element rows 

elem_1 = ['Hydrogen', 'Helium'] 
elem_2 = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
elem_3 = ['Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']
print(elem_1+elem_2+elem_3)


# In[31]:


# [ ] .extend() jack_jill with "next_line" string - print the result
jack_jill = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill']
next_line = ['To', 'fetch', 'a', 'pail', 'of', 'water']
jack_jill.extend(next_line)
print(jack_jill)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 5</B></font>
# ## .reverse() : reverse a list in place

# In[32]:


# [ ] use .reverse() to print elements starting with "Calcium", "Chlorine",... in reverse order
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine',  'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon',  'Potassium', 'Calcium']
elements.reverse()
print(elements)


# In[36]:


# [ ] print words in spell_list that 8 or more characters in length in reverse order
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
for x in spell_list:
    if len(x) >= 8:
        print(x[::-1])


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 6</B></font>
# ## .sort() and sorted()

# In[37]:


# [ ] sort the list element, so names are in alphabetical order and print elements
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine',  'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon',  'Potassium', 'Calcium']
elements.sort()
print(elements)


# In[38]:


# [ ] print the list, numbers, sorted and then below print the original numbers list 
numbers = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]
print(sorted(numbers))
print(numbers)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 7</B></font>
# ## Converting a string to a list with `.split()`

# In[40]:


# [ ] split the string, daily_fact, into a list of word strings: fact_words
# [ ] print each string in fact_words in upper case on it's own line
dF = "Did you know that there are 1.4 billion students in the world?"
fW = dF.split()
for x in fW:
    print(x.upper())


# In[41]:


# [ ] convert the string, code_tip, into a list made from splitting on the letter "o"
cT = 'isdrubhasero frfiowehjofbsdfowejlozdihf oseih asdiof haseo aebf ae adc asdo foasfh oascfh sdfouiae fhsdocvsdhohasvobsda'
print(cT.split('o'))


# In[42]:


# [ ] split poem on "b" to create a list: poem_words
# [ ] print poem_words by iterating the list
poem = "The bright brain, has bran!"
pW = poem.split("b")
for x in pW:
    print(x)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 8</B></font>
# ## `.join()`
# ### build a string from a list

# In[45]:


# [ ] print a comma separated string output from the list of Halogen elements using ".join()"
halogens = ['Chlorine', 'Fluorine', 'Bromine', 'Iodine']
print(", ".join(halogens))


# In[46]:


# [ ] split the sentence, code_tip, into a words list
# [ ] print the joined words in the list with no spaces in-between
# [ ] Bonus: capitalize each word in the list before .join()
code_tip ="Read code aloud or explain the code step by step to a peer".title()
wL = code_tip.split()
print("".join(wL))


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 8</B></font>  
# ## `list(string)` & `print("hello",end=' ')`
# 
# - **Cast a string to a list** 
# - **print to the same line**   

# In[1]:


# [ ] cast the long_word into individual letters list 
# [ ] print each letter on a line
long_word = 'decelerating'
l = list(long_word)
for x in l:
    print(x)


# In[2]:


# [ ] use use end= in print to output each string in questions with a "?" and on new lines
questions = ["What's the closest planet to the Sun", "How deep do Dolphins swim", "What time is it"]
for x in questions:
    print(x, end = '?\n')


# In[3]:


# [ ] print each item in foot bones 
#    - capitalized, both words if two word name
#    - separated by a comma and space
#    - and keeping on a single print line
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
for x in foot_bones:
    print(x.title(), end = ', ')


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
