#!/usr/bin/env python
# coding: utf-8

# # Section 4.4
# ## File .write() and .seek() Methods
# - File `.write()`  with `.seek()`
# - File append
# 
# ----- 
# 
# ### Student will be able to
# - Use `.seek()` to set file read or write location
# - Use file append mode

# ## Concept: Writing to a file opened in write mode
# ### `'w' or 'w+'`
# >```python
# poem_file = open('poem.txt', 'w') 
# poem_file.write("Hello World!\n")
# ```  
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7d6dfbf1-4af7-4324-bc36-67041c62c8f9/Unit2_Section4.4a-Writing_to_File_in_Write_Mode.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7d6dfbf1-4af7-4324-bc36-67041c62c8f9/Unit2_Section4.4a-Writing_to_File_in_Write_Mode.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### write mode:  `'w' `  
# ### write mode plus read: `'w+'`  
# #### **`'w'`** and **`'w+'`** modes will create a new file or overwrite existing files  
# **All previous data will be lost**

# ### Examples

# In[1]:


# [ ] review and run example
# - creates a new local file or overwrites the local file (makes it blank)
new_file = open('new_file.txt', 'w')


# In[2]:


# [ ] review and run example to write some text to the file
new_file.write("This is line #1 with 'w'\nThis is line #2 with 'w'\nThis is line #3 withn 'w'!\n")


# In[3]:


# [ ] review and run example
# - close file and re-open in read mode 
# - head pointer is at start of file
new_file.close()
new_file = open('new_file.txt', 'r')


# In[4]:


# [ ] review and run example to see what was written to the file
new_text = new_file.read()
print(new_text)

new_file.close()


# #### `'w+'` means the file is in write plus read mode  
# - After any write, the pointer is at the end of text that has been written 
# - To read the entire file, the pointer needs to be at the beginning of the file - see **.seek()** below to set the file pointer

# ## Task 1: Create a local file  
# ### Open in 'w' mode  
# - Open inner_planets.txt in write mode **'w'** to create a local file
# - Write the first four planets from the sun in earth's solar system (Mercury, Venus, Earth, Mars) on separate lines
# - Close the file and re-open in read mode **'r'** 
# - Use .read() to read the entire file contents
# - Print the entire file contents

# In[10]:


# [ ] open planets.txt in write mode
inner_planets = open('inner_planets.txt', 'w')


# In[11]:


# [ ] write Mercury, Venus, Earth, Mars on separate lines
inner_planets.write('Mercury\nVenus\nEarth\nMars')


# In[12]:


# [ ] close the file and re-open in read mode
inner_planets.close()
inner_planets = open('inner_planets.txt', 'r')


# In[13]:


# [ ] use .read() to read the entire file contents
inplan = inner_planets.read()


# In[15]:


# [ ] print the entire file contents and close the file
print(inplan)
inner_planets.close()


# ## Concept: Using .seek(0) 
# ### Setting the pointer to beginning of file  
# >```python
# new_file.seek(0)
# new_contents = new_file.read()
# print(new_contents)
# ```  
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/4c62275e-0df8-44f5-91a8-6e16755995aa/Unit2_Section4.4b-Using_Seek.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/4c62275e-0df8-44f5-91a8-6e16755995aa/Unit2_Section4.4b-Using_Seek.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Using .seek() to set the read/write pointer to beginning of file  
# **`new_file.seek(0)`** moves the file read\write pointer to the start of the file. 

# ### Examples: seek() with `'w+'`

# In[17]:


# [ ] review and run example
# creates a new local file or overwrites the local file (makes it blank)
new_file = open('new_file.txt', 'w+')


# write plus read **`'w+'`**  
# **`'w+'`** overwrites existing files of the same name - **rendering the file blank**.  
# The file is writeable and readable.

# In[18]:


# [ ] review and run example to see what was written to the file 
# - 'w+' overwrites, we can read, but the file is ***BLANK***
new_text = new_file.read()
print(new_text)


# In[19]:


# [ ] review and run - write to the blank file
new_file.write("This is line #1 with 'w+'\nThis is line #2 with 'w+'\n")


# In[21]:


# [ ] review and run example - read and print (Note: the pointer is at the end of the file - result = empty string)
new_text = new_file.read()

print(new_text)


# ### Expected: prints empty string above  
# pointer was at end of file where there is nothing to read

# ### seek(0)  
# sets the pointer to the beginning of the file, enabling read() to input the entire file contents

# In[22]:


# [ ] review and run example - sets pointer to beginning of file
new_file.seek(0)


# In[23]:


# [ ] review and run example - now read starts from beginning of file
new_text = new_file.read()
print(new_text)


# In[24]:


# # [ ] review and run example - clean up and close file
new_file.close()


# ## Task 2: Using `.seek(0)` on a local file in write plus read mode `'w+'`
# ### Open outer_planets.txt in 'w+' mode (write plus read) 
# - Open **outer_planets.txt** in write plus read mode **'w+'** 
# - Write four outer planets in earth's solar system (Jupiter, Saturn, Uranus, Neptune) on separate lines  
# - Use .seek() to move the pointer to the start of the file
# - Use .read() to read the entire file contents
# - Print the entire file contents and close the file

# In[1]:


# [ ] open outer_planets.txt in write mode 'w+'
outPlan = open('outer_planets.txt', 'w+')


# In[2]:


# [ ] write four outer planets in earth's solar system (Jupiter, Saturn, Uranus, Neptune) on separate lines
print(outPlan.readlines())


# In[3]:


# [ ] use .seek() to move the pointer to the start of the file
# [ ] use .read() to read the entire file contents
outPlan.seek(0)
print(outPlan.read())


# In[4]:


# [ ] print the entire file contents and close the file
outPlan.seek(0)
print(outPlan.read())
outPlan.close()


# ## Concept: Using .seek() *offset* and *whence* 
# ### Setting the pointer in a file with positive *offset* values and *whence* location 
# >```python
# new_file.seek(13)
# new_contents = new_file.read()
# print(new_contents)
# ```  
# ```python
# new_file.seek(0,2)
# ```  
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c2b8a760-a39d-45a2-80e1-a2b79264b120/Unit2_Section4.4c-Seek_Variations-Offset_Whence.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c2b8a760-a39d-45a2-80e1-a2b79264b120/Unit2_Section4.4c-Seek_Variations-Offset_Whence.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Using .seek() to set the read/write pointer in a file   
# #### *offset* values and *whence* arguments
# .seek() can set the pointer to a desired index from the beginning of the file.  
# The example below moves to the character to offset 10 (the 11th character).
# ```python
# new_file.seek(10)
# ```  
# 
# Which is also written with an optional second argument, know as *whence* ("from where"). 
# ```python
# new_file.seek(10,0)
# ```  
# Using 0 for *whence* starts the *offset* from the beginning of the file.
# 
# >**Note:** the offset must be a positive integer in Python 3, so we cannot offset backwards from the end of the file  
# 
# ## `file.seek(offset, whence)`
# | whence mode | description               |  
# |:-----------:|---------------------------|
# | 0 | points to the beginning of the file |   
# | 1 | points to the current location |  
# | 2 | points to the end of the file & offset is always 0|  
# 
# Using ** *whence* ** the index can be offset from either the beginning, current location or to the end of the file (where there is no offset applied).

# ### Examples: seek to a specific location

# In[12]:


# [ ] review and run - create, write, read and print a file
tips_file = open('code_tips.txt', 'w+')
tips_file.write('-use simple function and variable names\n-comment code\n-organize code into functions\n')
tips_file.seek(0)
tips_text = tips_file.read()
print(tips_text)


# In[13]:


# [ ] review and run example - setting a specific seek() index 
tips_file.seek(13)
# now read starts from 14th character of file
tips_text = tips_file.read()
print(tips_text)


# In[14]:


# [ ] review and run example - string slicing on a read of an entire file
# read from the start
tips_file.seek(0)
tips_text = tips_file.read()

# slice from the 14th character to end
print(tips_text[13:])


# ### Examples: seek() with optional *whence* argument 

# In[15]:


# [ ] review and run example - setting pointer to end of file with whence value = 2
tips_file.seek(0,2)
tips_file.write("-use seek(0,2) to set read/write at end of file\n")

# read from beginning of file - .seek(0,0) is same as .seek(0)
tips_file.seek(0,0)
tips_text = tips_file.read()
print(tips_text)


# In[16]:


# [ ] review and run example - point to file beginning and overwrite 1st line
tips_file.seek(0)
tips_file.write('-use simple function and variable names\n'.upper())


# In[17]:


# [ ] review and run example - show new file contents
tips_file.seek(0,0)
tips_text = tips_file.read()
print(tips_text)


# ## Task 3: seek() with optional whence argument
# - Open a new file **days.txt** in write plus read mode **'w+'** 
# - Write week days (Monday - Friday) on separate lines  
# - Use .seek() to move the pointer to the start of the file
# - Use .read() to read the entire file contents
# - Print the entire file contents and close the file
# - Use .seek() to move the pointer to the end of the file and write the weekend days (Saturday & Sunday)
# - Use .seek() to move the pointer to the start of the file
# - Use .read() to read the entire file contents
# - Print the entire file contents and close the file

# In[21]:


# [ ] open a new file days.txt in write plus read mode 'w+' 
# [ ] write week days (Monday - Friday) on separate lines to the file
days = open('days.txt', 'w+')
days.write('Monday\nTuesday\nWednesday\nThursday\nFriday')


# In[22]:


# [ ] use .seek() to move the pointer to the start of the file
# [ ] use .read() to read the entire file contents
# [ ] print the entire file contents and close the file
days.seek(0)
print(days.read())


# In[23]:


# [ ] use .seek() to move the pointer to the end of the file
# [ ] write the weekend days (Saturday & Sunday)
days.seek(0,2)
days.write('\nSaturday\nSunday')


# In[24]:


# [ ] use .seek() to move the pointer to the start of the file
# [ ] use .read() to read the entire file contents
# [ ] print the entire file contents and close the file
days.seek(0)
print(days.read())
days.close()


# ## Concept: Open a file in a writeable mode
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/35b90424-34b0-4c9b-aef6-50966636f0b8/Unit2_Section4.4d-Write_Modes.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/35b90424-34b0-4c9b-aef6-50966636f0b8/Unit2_Section4.4d-Write_Modes.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Open a file in a writing mode, with: `'w', 'w+', 'r+', 'a', 'a+'` 
# | MODE    |  Description  |  
# |:-------:|:--------------|  
# | 'r'  | read only mode |  
# | **'w'** | write - **overwrites** file with same name |  
# | **'w+'** | write and read mode - **overwrites** file with same name|  
# | **'r+'** | read and write mode (**no** overwrite) |  
# | **'a'**  | opens for appending to end of file (**no** overwrite) |  
# | **'a+'** | opens for appending to end of file (**no** overwrite) plus read |  
# 
# **Warning: `'w'`** and **`'w+'`** modes will create a new file or **overwrite** existing files (deleting all file contents)

# ## Concept: Writing to a file opened in additional write modes
# ### `'r+', 'a', 'a+'` 
# Writing is the same - pointers are different.
# >```python
# poem_file = open('poem.txt', 'r+') 
# poem_file.write("Hello World!\n")
# ```  
# ```python
# poem_file = open('poem.txt', 'a+') 
# poem_file.write("Goodbye, this is the end of the file\n")
# ```  
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/64698d6f-d193-485a-be39-0e9286aca1dc/Unit2_Section4.4e-Read_Write_Append.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/64698d6f-d193-485a-be39-0e9286aca1dc/Unit2_Section4.4e-Read_Write_Append.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### read mode plus write `'r+'` and append modes `'a', 'a+'`
# #### read plus mode `'r+'` differs from write modes `'w', 'w+'`  
# - read plus doesn't blank out the file contents with an overwrite  
#  
# #### append modes `'a', 'a+'` differ from write modes `'w', 'w+'`   
# - append doesn't blank out the file contents with an overwrite  
# - append pointer is set to the end of the file for every write
# - append plus (a+) is append mode, **plus** read mode
# 
# |   `'r+', 'a', 'a+'`                        |  
# |:------------------------------------------:|  
# |will **not overwrite** existing file content creating a blank file|   

# ### Examples
# #### append plus mode `a+`

# In[25]:


# [ ] review and run example - function writes to the open log argument
# loads funtion into memory but the funtion is not called
def logger(log):
    log_entry = input("enter log item (enter to quit): ")
    count = 0

    while log_entry:
        count += 1
        log.write(str(count) + ": " + log_entry + "\n")
        log_entry = input("enter log item (enter to quit): ")
        
    return count
    


# In[26]:


# [ ] review and run example: makes a blank file  (initialize/reset)

log_file = open('log_file.txt', 'w+')
log_file.close()


# In[27]:


# [ ] review and run example - opens the log_file before passing to logger() function call, below
# allows for calls below to run several times appending to the end of log_file

log_file = open('log_file.txt', 'a+')


# In[28]:


# [ ] review and run example - calls the above logger() function
# what happens running the cell above (a+) again before running this cell again? 
# what happens if log_file.seek(0) is run before an append?

logger(log_file)    

log_file.seek(0)
log_text = log_file.read()

print()
print(log_text)
log_file.close()


# #### read plus mode `r+`  
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/64adc0f6-c26b-439f-94f5-e011daded3cf/Unit2_Section4.4f_read_plus.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/64adc0f6-c26b-439f-94f5-e011daded3cf/Unit2_Section4.4f_read_plus.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# Create a file that has one line: "Count is: x".
# Overwrite with new count at the x location (x is an integer).

# In[1]:


# [ ] review and run example - create a file with initial count of 0
count_file = open("count_file.txt", "w+")

count_file.write("Count is: 0")
count_file.seek(0)
print(count_file.readline().strip())

count_file.close()


# In[2]:


# [ ] review and run example - can rerun this cell
count_file = open("count_file.txt", "r+")

count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)

# get the int character(s) after the colon and space, cast and increment
count = int(count_line[10:])+1

# write the incremented value to the file - overwrite before value
count_file.seek(10)
count_file.write(str(count))

count_file.seek(0)
print("\nAFTER\n" + count_file.readline().strip())

count_file.close()


# In[3]:


# [ ]  review funtion code for inc_count() funtion that reads file and updates the count
# the file always has 1 line that is The count is: N, where N is an integer
def inc_count(cnt_file):
    cnt_file.seek(0,0)
    cnt_line = cnt_file.readline().strip()
    cnt = int(cnt_line[10:])+1
    cnt_file.seek(10,0)
    cnt_file.write(str(cnt))
    return cnt


# In[4]:


# [ ] review and run example with call to function: inc_count() - **Run cell multiple times**
# opens file/prints initial value
count_file = open("count_file.txt", "r+")

count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)

# call inc_count() to increase the count 5 times
for i in range(5):
    count = inc_count(count_file)
    count_file.seek(0)
    print("\nAFTER inc_count() call", i+1, "\n" + count_file.readline().strip())

count_file.close()


# ## Task 4: append
# - Open task4_file.txt in append plus mode ("a+")  
# - Create a `for item in range(5):` loop, for each loop:  
#   - Write to the file: "append #"+ str(item)+"\n"  
#   - Use seek() to set the pointer to the beginning of the file  
# - Print the file contents using file .read() method after eiting the loop
# 
# In append mode, the file should write only to the end of the file regardless of setting seek() location.

# In[5]:


# [ ] complete the task
task4_file = open('task4_file.txt', 'w+')
task4_file.write("Line1\nLine2\nLine3\n")
task4_file.close()
# [ ] code here
task4 = open('task4_file.txt', 'a+')
for x in range(5):
    task4.write('append #' + str(x) + '\n')
    task4.seek(0)
print(task4.read())


# ## Task 5: read plus (`r+`) mode  
# Read the provided code and complete the code as follows:  
# - Open task4_file.txt in append plus mode ("r+")  
# - Create a `for item in range(1,6):` loop, for each loop:  
#   - Write to the file: "write (r+) #"+ str(item)+"\n"  
#   - Use **seek(item*11)** to set the pointer to 11x's the loop count  
#   Note: First loop is 1 if using range(1,6), seek will be set to 11, 22, 33, 44
# - Print the file contents using file .read() method after exiting the loop
# 
# **"r+"** mode will write wherever the pointer is set - such as after a read or from using .seek()

# In[19]:


# [ ] complete the task
task5_file = open('task5_file.txt', 'w+')
task5_file.write("Line\nLine2\nLine3\nLine4\nLine5\nLine6\nLine7\nLine8\nLine9\nLine10\n")
task5_file.seek(0)
print(task5_file.read(),"\n")
task5_file.close()
# [ ] code here
task5 = open('task5_file.txt', 'r+')
for x in range(1,6):
    task5.write('write (r+)#' + str(x) + '\n')
    task5.seek(x * 13)
task5.seek(0)
print(task5.read())


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
