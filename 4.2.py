#!/usr/bin/env python
# coding: utf-8

# # Section 4.2
# ## Nested Conditionals
# - Nested conditionals  
# - **Print formatting with the (\) escape sequence** 
# 
# -----
# 
# ### Student will be able to
# - Create nested conditional logic in code  
# - **Print format print using escape sequence (\)**

# ## Concept: Formatting with Escape Sequences
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b64e53fd-eb3b-4383-8b5f-4da51fc881c5/Unit1_Section6.2-Escape-Sequences.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/b64e53fd-eb3b-4383-8b5f-4da51fc881c5/Unit1_Section6.2-Escape-Sequences.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Escape Sequences
# - Escape sequences all start with a backslash (**`\`**) 
# - Escape sequences can be used to display characters in Python reserved for formatting
#   - **`\\`** &nbsp; Backslash (**`\`**)  
#   - **`\'`** &nbsp; Single quote (**'**)  
#   - **`\"`** &nbsp; Double quote (**"**)  
# 
# 
# - Escape sequences are part of special formatting charcters\n    Linefeed 
#   - **`\t`** &nbsp; Tab
#   - **`\n`** &nbsp; return or newline
# 
# We use escape sequences in strings - usually with `print()` statements. 

# ### Examples

# In[1]:


# review and run example using \n (new line)
print('Hello World!\nI am formatting print ')


# In[2]:


# review and run code using \t (tab)
student_age = 17
student_name = "Hiroto Yamaguchi"
print("STUDENT NAME\t\tAGE")
print(student_name,'\t' + str(student_age))


# In[3]:


# review and run code 
# using \" and \' (escaped quotes)
print("\"quotes in quotes\"")
print("I\'ve said \"save your notebook,\" so let\'s do it!")

# using  \\ (escaped backslash)
print("for a newline use \\n")


# ## Task 1: Format using backslash (**`\`**) escape sequences

# In[4]:


# [ ] print "\\\WARNING!///"
print("\\\\\\WARNING!///")


# In[5]:


# [ ] print output that is exactly (with quotes): "What's that?" isn't a specific question.
print("\"What's that?\" isn't a specific question.")


# In[7]:


# [ ] from 1 print statement output the text commented below using no spaces
# One     Two     Three
# Four    Five    Six
print("One\tTwo\tThree\nFour\tFive\tSix")


# ## Task 2: Program: `pre_word()` function
# Function has a single string parameter that it checks is a single word starting with "pre".
# - Check if word starts with "pre"
# - Check if word .isalpha() 
# - If all checks pass: return **`True`**
# - If any checks fail: return **`False`**
# - **Test** 
#   - Get input using the directions: *enter a word that starts with "pre": *
#   - Call pre_word() with the input string
#   - Test **if** return value is **`False`** and print message explaining not a "pre" word 
#   - **else** print message explaining is a valid "pre" word

# In[2]:


# [ ] create and test pre_word()
def preWord(word):
    if word.lower().startswith("pre"):
        if word.isalpha():
            return(True)
        else:
            return(False)
    else:
        return(False)
if not(preWord(input())):
    print("That is not a \"pre\" word")
else:
    print("That is a \"pre\" word")


# ## Task 3: Fix the errors

# In[4]:


# [ ] review, run, fix
print("Hello\nWorld!")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
