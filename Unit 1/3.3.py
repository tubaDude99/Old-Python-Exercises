#!/usr/bin/env python
# coding: utf-8

# # Section 3.3
# ## Conditionals: String Comparison
# - **`if`, `else`, `pass`**
#   - Conditionals using Boolean string methods
#   - Comparison operators
#   - **String comparisons**
# 
# ----- 
# 
# ### Student will be able to
# - **Control code flow with `if`... `else` conditional logic**  
#   - Uing Boolean string methods (`.isupper(), .isalpha(), startswith()...`)  
#   - Using comparison (`>, <, >=, <=, ==, !=`)  
#   - **Using strings in comparisons**  

# 
# ## Concept: String Comparisons
# - ### Strings can be equal `==` or unequal `!=`
# - ### Strings can be greater than `>` or less than `<` 
# - ### Alphabetically `"A"` is less than `"B"`
# - ### Lowercase `"a"` is greater than uppercase `"A"`

# ### Examples

# In[1]:


# review and run code
"hello" < "Hello"


# In[2]:


# review and run code
"Aardvark" > "Zebra"


# In[3]:


# review and run code
'student' != 'Student'


# In[4]:


# review and run code
print("'student' >= 'Student' is", 'student' >= 'Student')
print("'student' != 'Student' is", 'student' != 'Student')


# In[5]:


# review and run code
"Hello " + "World!" == "Hello World!"


# ## Task 1: String Comparisons

# In[6]:


msg = "Hello"
# [ ] print the True/False results of testing if msg string equals "Hello" string
print(msg == "Hello")


# In[9]:


greeting = "Hello"
# [ ] get input for variable named msg, and ask user to 'Say "Hello"'
# [ ] print the results of testing if msg string equals greeting string
msg = input('Say "Hello"')
print(msg == greeting)


# ## Concept: String Comparisons with `if`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/d66365b5-03fa-4d0d-a455-5adba8b8fb1b/Unit1_Section4.3-string-compare-if.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/d66365b5-03fa-4d0d-a455-5adba8b8fb1b/Unit1_Section4.3-string-compare-if.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 

# ### Examples

# In[10]:


# [ ] review and run code
msg = "Save the notebook"

if msg.lower() == "save the notebook":
    print("message as expected")
else:
    print("message not as expected")


# In[11]:


# [ ] review and run code
msg = "Save the notebook"
prediction = "save the notebook"

if msg.lower() == prediction.lower():
    print("message as expected")
else:
    print("message not as expected")


# ## Task 2: Using Comparison Operators with `if`
# 

# In[12]:


# [ ] get input for a variable, answer, and ask user 'What is 8 + 13? : '
# [ ] print messages for correct answer "21" or incorrect answer using if/else
# note: input returns a "string"
answer = input('What is 8 + 13? : ')
if answer == '21':
    print("Correct")
else:
    print("Incorrect")


# ## Task 3 (program): True False Quiz Function
# Call the tf_quiz function with two arguments.
# - T/F question string 
# - answer key string like "T"  
# 
# Return a string: "correct" or incorrect"
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/3805cc48-f5c9-4ec8-86ad-1e1db45788e4/Unit1_Section4.3-TF-quiz.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/3805cc48-f5c9-4ec8-86ad-1e1db45788e4/Unit1_Section4.3-TF-quiz.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Define and use `tf_quiz()` function  
# - **`tf_quiz()`** has **2 parameters** which are both string arguments  
#   - **`question`**: a string containg a T/F question like "Should save your notebook after edit?(T/F): "  
#   - **`correct_ans`**: a string indicating the *correct answer*, either **"T"** or **"F"** 
# - **`tf_quiz()`** returns a string:  "correct" or "incorrect"
# - Test tf_quiz(): **create a T/F question** (*or several!*) to **call tf_quiz()**  
# 

# In[3]:


# [ ] Create the program, run tests
def tfQuiz(ques,ans):
    if input(ques) == ans:
        print("Correct!")
    else:
        print("Incorrect!")
tfQuiz(input("What question? "),input("Correct Answer? "))


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
