#!/usr/bin/env python
# coding: utf-8

# # Section 3.4: Dictionaries
# * {}, .pop(), .clear
# * .keys(), .values() .items(), sorted()
# * in, not in, is, ==, len()
# 
# ### Students will be able to:
# * Create dictionaries
# * Access dictionary values
# * Add, change, and delete dictionary items
# * Delete a whole dictionary variable
# * Iterate over the keys, values, and items of a dictionary 
# * Use dictionary operations and functions (i.e. containment and sorting)

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# ## Dictionary Basics
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/56a734b0-1c5e-4973-b1b2-ce1cedd07dec/DEV330x-3_4a_dictionary_basics.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/109b6489-c449-4a6a-a9f9-4cc8ebb26cd8/DEV330x-3_4a_dictionary_basics.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# A Python dictionary is yet another data structure to store a collection of data. However, unlike lists and tuples, a dictionary does not store a sequence of data but rather an association of (_key, value_) pairs. All keys in a dictionary are unique, while a value can be associated with multiple keys. Dictionaries provide a very useful utility to represent real-world data, such as that stored in contact lists and birthday lists. 
# 
# The power of Python's dictionary is in the way it can be searched. If you are searching for a specific element in an unordered list (or tuple) you will have to traverse the whole list until you find the element; on the other hand, when you search a Python dictionary, there is no need to traverse all of its elements. A Python dictionary uses a mathematical process called _hashing_ that optimizes the search capability by using the keys of a dictionary. This is more obvious when you are storing thousands of items in a dictionary.
# 
# #### Creating a dictionary
# A dictionary can be created by using the braces operator `{key:value}`. You have to specify the keys and their associated values.
# 
# ##### `int` keys
# Keys can be integer values starting from 0, much like lists and tuples.
# ```python
# >>> D = {0:5.5, 1:10.3, 2:43.2, 3:85.3}
# >>> type(D)
# <class 'dict'>
# ```
# 
# Keys do not have to start from 0, neither do they have to be in order.
# ```python
# >>> D = {1343:5.5, 2:10.3, 3234235234:43.2, -324:85.3}
# >>> type(D)
# <class 'dict'>
# ```
# ##### `float` keys
# Keys can be float.
# ```python
# >>> D = {1.5:5.5, 2.9:10.3, -3.8:43.2, 5:85.3}
# >>> type(D)
# <class 'dict'>
# ```
# 
# ##### `str` keys
# As you might have noticed by now, keys can be of different types, and keys within the same dictionary can be of different types. Generally speaking, a key should be of a hashable type; therefore, you cannot use mutable objects such as lists or other dictionaries.
# 
# ```python
# >>> D = {'Name':'Skye', 'Age':35, 'Temperature':98.7}
# ```
# 
# NOTE: An empty dictionary can be created as `D = {}`.
# 
# #### Accessing dictionary items
# You can access the value associated with a key of a dictionary by using the subscript `[]` operator, in much the same way you did with lists and tuples.
# 
# ```python
# >>> D = {'Name':'Skye', 'Age':35, 'Temperature':98.7}
# >>> print("The name is: {}".format(D['Name']))
# The name is: Skye
# >>> print("Age is:", D['Age'])
# Age is: 35
# ```
# 
# #### Modifying dictionary items
# Dictionaries are mutable objects and can be modified. For example, you can change the value associated with a key by accessing it using the `[]` operator amd then assigning it a new value.
# 
# ```python
# >>> D = {'Name':'Skye', 'Age':35, 'Temperature':98.7}
# >>> D['Name'] = 'Tamara'
# >>> D
# {'Name': 'Tamara', 'Age': 35, 'Temperature': 98.7}
# ```
# 
# #### Adding dictionary items
# You can add a new _key:value_ pair to a dictionary by using the operator `[]`. Just make sure the key doesn't already exist in the dictionary. (You will see later that you can use the containment operator `in` to test a key's existence.)
# 
# ```python
# >>> D = {'Name':'Skye', 'Age':35, 'Temperature':98.7}
# >>> D['Last Name'] = 'Babic'
# >>> D
# {'Name': 'Skye', 'Age': 35, 'Temperature': 98.7, 'Last Name': 'Babic'}
# ```
# 
# #### Deleting dictionary items
# You can delete a dictionary _key:value_ pair using the `pop(key)` method, the _key:value_ pair will be deleted and the method will return the value associated with the key.
# 
# ```python
# >>> D = {'Name':'Skye', 'Age':35, 'Temperature':98.7, 'Last Name': 'Babic'}
# >>> a = D.pop('Age') # remove the key:value ('Age':35) pair
# >>> a # D['Age']
# 35
# >>> D
# {'Name': 'Skye', 'Temperature': 98.7, 'Last Name': 'Babic'}
# ```
# 
# If you try to delete a key:value pair not in the dictionary, a `KeyError` exception will be raised. 
# ```python
# >>> D = {'Name':'Skye', 'Age':35, 'Temperature':98.7, 'Last Name': 'Babic'}
# >>> D.pop('Middle Name') # There is no middle name in D
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'Middle Name'
# ```
# #### Clearing and deleting a dictionary
# You can delete all the elements in a dictionary by using the `.clear()` method.
# 
# ```python
# >>> D = {'Name':'Skye', 'Age':35, 'Temperature':98.7, 'Last Name': 'Babic'}
# >>> D.clear()
# >>> D
# {}
# ```
# 
# You can delete the whole dictionary by using `del` like you would delete any other variable.
# ```python
# >>> D = {'Name':'Skye', 'Age':35, 'Temperature':98.7, 'Last Name': 'Babic'}
# >>> del(D)
# >>> D
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: "name 'D' is not defined"
# ```

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# 

# ## Creating a Contact List
# 
# In the following examples, you will see how to create, search, modify, add, and delete names and phone numbers from a contacts dictionary.

# ### Querying contacts

# In[1]:


# Create a dictionary of contacts; names as keys, phone numbers as values
contacts = {"Suresh Datta": "345-555-0101", "Colette Browning": "483-555-0119", "Skey Homsi": "485-555-0195"}

# Ask user for a name, then display the number
name = input("Enter a name: ")

# If name is not in the contacts dictionary, a KeyError exception will be raised
number = contacts[name]

print("Number is: {:s}".format(number))


# ### Querying contacts with exception handling

# In[2]:


# Create a dictionary of contacts; names as keys, phone numbers as values
contacts = {"Suresh Datta": "345-555-0101", "Colette Browning": "483-555-0119", "Skey Homsi": "485-555-0195"}

# Ask user for a name, then display the number
name = input("Enter a name: ")

# If name is not in the contacts dictionary, the exception message will be displayed
try:
    number = contacts[name]
    print("Number is: {:s}".format(number))
except KeyError as exception_object:
    print("{:s} was not found in contacts".format(name))


# ### Adding or changing a contact

# In[ ]:


# Create a dictionary of contacts; names as keys, phone numbers as values
contacts = {"Suresh Datta": "345-555-0101", "Colette Browning": "483-555-0119", "Skey Homsi": "485-555-0195"}

# Ask user for a name and number
name = input("Enter a name: ")
number = input("Enter a number: ")

# If the name exists in the dictionary, the number will be updated
# If the name does NOT exist in the dictionary, a new name:number pair will be added
contacts[name] = number

print("Updated contact:", contacts)


# ### Deleting a contact

# In[ ]:


# Create a dictionary of contacts; names as keys, phone numbers as values
contacts = {"Suresh Datta": "345-555-0101", "Colette Browning": "483-555-0119", "Skey Homsi": "485-555-0195"}

# Ask user for a name and number
name = input("Enter a name: ")

# If the name is not in the contacts dictionary, display the exception message
try:
    number = contacts.pop(name)
    print("{:s}: {:s} was deleted from contacts".format(name, number))
except KeyError as exception_object:
    print("{:s} was not found in contacts".format(name))
    
print("Updated contact:", contacts)


# ## Tracking Grocery Prices
# In the following example, you will use a dictionary to store and manipulate groceries and their associated prices. Each grocery is represented by a unique item name that is used as the unique dictionary key. The average daily price of a grocery will be used as the associated value.

# In[ ]:


# Create a dictionary of grocery items and associated prices
groceries = {'Bread':2.26, 'Milk':3.62, 'Chocolate':1.59}

# Display the price for the item name
item = 'Bread'
print("{} price = {:.2f}".format(item, groceries[item]))

# Add a new key:value pair to the dictionary
groceries['Banana']= 1.00
print('Adding Banana:')
print(groceries)

# Modify a dictionary element
groceries['Banana'] = 1.10
print('Modifying Banana:')
print(groceries)

# Remove a dictionary element
print("Removing: '{}':{:.2f}".format('Banana', groceries.pop('Banana')))
print(groceries)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Dictionary Basics

# In[2]:


# [ ] The `data` list contains information about a company's employees.
# Use the `data` list and an appropriate loop to create a dictionary of employees.
# Use IDs (as keys) and names (as values).
# Ignore the email addresses for now.

# The created dictionary should look like:
# {57394: 'Suresh Datta', 48539: 'Colette Browning', 58302: 'Skye Homsi', 48502: 'Hiroto Yamaguchi', 48291: 'Tobias Ledford', 48293: 'Jin Xu', 23945: 'Joana Dias', 85823: 'Alton Derosa'}

data = [["Suresh Datta", 57394, "suresh@example.com"], ["Colette Browning", 48539, "colette@example.com"], ["Skye Homsi", 58302, "skye@example.com"], ["Hiroto Yamaguchi", 48502, "hiroto@example.com"], ["Tobias Ledford", 48291, "tobias@example.com", "Tamara Babic", 58201, "tamara@example.com"], ["Jin Xu", 48293, "jin@example.com"], ["Joana Dias", 23945, "joana@example.com"], ["Alton Derosa", 85823, "alton@example.com"]]
d = {}
for x in data:
    d[x[1]] = x[0]
print(d)


# In[6]:


# [ ] Use the `records` dictionary in a program that asks the user for an ID and prints the name of the associated employee.
# Display an appropriate message if the ID is not found in the dictionary.

records = {57394: 'Suresh Datta', 48539: 'Colette Browning', 58302: 'Skye Homsi', 48502: 'Hiroto Yamaguchi', 48291: 'Tobias Ledford', 48293: 'Jin Xu', 23945: 'Joana Dias', 85823: 'Alton Derosa'}
i = int(input('Please enter ID: '))
if i not in records:
    print("!!! ALERT nonperson !!!")
else:
    print(records[i])


# In[17]:


# [ ] Use the `records` dictionary in a program to ask the user for an ID then delete the employee record associated with the ID
# The program should display an appropriate message if the ID is not found in the dictionary.

records = {57394: 'Suresh Datta', 48539: 'Colette Browning', 58302: ['Skye Homsi', 'Joe'], 48502: 'Hiroto Yamaguchi', 48291: 'Tobias Ledford', 48293: 'Jin Xu', 23945: 'Joana Dias', 85823: 'Alton Derosa'}

i = int(input('Please enter ID: '))
if i in records:
    print(records.pop(i))
else:
    print("ERROR: Person not found")


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Looping Over Dictionary Items
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/d028639b-0ba5-48ff-8ae4-89380076d8a9/DEV330x-3_4b_looping_over_dictio.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c5db517f-1803-4af4-9276-597ab34eaad6/DEV330x-3_4b_looping_over_dictionary_items.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# You can traverse the elements of a dictionary in much the same way you loop over the elements of a list or a tuple; however, with dictionaries you can use the keys, the values, or both keys and values when iterating over the dictionary elements.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# ## Dictionary Iterations

# ### Iterating over the keys
# 
# You can iterate over all the keys of a dictionary using the `.keys()` method in a for loop. 
# 

# In[18]:


D = {'Name':'Skye', 'Age':35, 'Temperature':98.7, 'Last Name': 'Babic'}

# Iterate over the keys of D
for key in D.keys():
    print("D[{}] = '{}'".format(key, D[key]))


# ### Iterating over the sorted keys
# Python stores the _key:value_ pairs of a dictionary in an order based on its optimization algorithm. You can use the `sorted` method to traverse the keys of a dictionary in a sorted order.
# 
# In the previous example, the keys were not printed alphabetically. In the following code snippet, we change the order by using the `sorted` method.

# In[19]:


D = {'Name':'Skye', 'Age':35, 'Temperature':98.7, 'Last Name': 'Babic'}

# Iterate over the sorted keys of D 
# Keys sorted alphabetically because they are all strings
for key in sorted(D.keys()):
    print("D[{}] = '{}'".format(key, D[key]))


# ### Iterating over the values
# You can iterate over the elements of a dictionary using the values in the same way you did when iterating using the keys. This can be achieved using the `.values()` method.
# 
# NOTE: Because the values in this example are of different types, you cannot sort them. If they were all of the same type, you could use the `sorted()` method to iterate over them in an ordered way.

# In[20]:


D = {'Name':'Skye', 'Age':35, 'Temperature':98.7, 'Last Name': 'Babic'}
for value in D.values():
    print(value)


# ### Iterating over the keys and values
# You can iterate over the _key:value_ pairs of a dictionary using the `.items()` method. The method returns a tuple as `(key, value)` for each pair in the dictionary.

# In[21]:


D = {'Name':'Skye', 'Age':35, 'Temperature':98.7, 'Last Name': 'Babic'}
for (key, value) in D.items():
    print(key,':', value)


# Of course, because the (key, value) tuple in the `for` loop is just unpacking the returned tuple of `D.items`, you can drop the parentheses.

# In[22]:


D = {'Name':'Skye', 'Age':35, 'Temperature':98.7, 'Last Name': 'Babic'}
for key, value in D.items():
    print(key,':', value)


# ## Tracking Grocery Prices
# 
# In this example, you will create a groceries dictionary, traverse it based on the keys (in a sorted way) and display the price for each of the items.

# In[23]:


# Create a dictionary of grocery items and associated prices
groceries = {'Bread':2.26, 'Milk':3.62, 'Chocolate':1.59}

# Display the price for the items in a sorted order
for item in sorted(groceries.keys()):
    print("{} = {:.2f}".format(item, groceries[item]))


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Looping Over Dictionary Items

# In[26]:


# [ ] The `data` list contains information about a company's employees
# Use the `data` list and an appropriate loop to create a dictionary of
# IDs (as keys): [name, email] (as values)

# The resulting dictionary should look like: 
# {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}

data = [["Suresh Datta", 57394, "suresh@example.com"], ["Colette Browning", 48539, "colette@example.com"], ["Skye Homsi", 58302, "skye@example.com"], ["Hiroto Yamaguchi", 48502, "hiroto@example.com"], ["Tobias Ledford", 48291, "tobias@example.com", "Tamara Babic", 58201, "tamara@example.com"], ["Jin Xu", 48293, "jin@example.com"], ["Joana Dias", 23945, "joana@example.com"], ["Alton Derosa", 85823, "alton@example.com"]]
d = {}
for r in data:
    d[r[1]] = [r[0], r[2]]
print(d)


# In[38]:


# [ ] Write a program to display the content of the `records` dictionary as shown here
# Note the IDs are sorted in an ascending order

'''
        Name         |     ID     |        Email        
________________________________________________________
     Joana Dias      |   23945    |    joana@example.com
   Tobias Ledford    |   48291    |   tobias@example.com
       Jin Xu        |   48293    |      jin@example.com
  Hiroto Yamaguchi   |   48502    |   hiroto@example.com
  Colette Browning   |   48539    |  colette@example.com
    Suresh Datta     |   57394    |   suresh@example.com
     Skye Homsi      |   58302    |     skye@example.com
    Alton Derosa     |   85823    |    alton@example.com
'''
records = {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}
print('        Name         |     ID     |        Email        \n' + (56*'_'))
for x in records:
    print('{:^21s}|{:^12d}|{:>21s}'.format(records[x][0],x,records[x][1]))


# In[40]:


# [ ] The company's domain has changed from (example.com) to (example.org)
# Write a program to modify the email addresses in the `records` dictionary to reflect this change

records = {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}
for x in records:
    records[x][1] = records[x][1][:-4] + '.org'
print('        Name         |     ID     |        Email        \n' + (56*'_'))
for x in records:
    print('{:^21s}|{:^12d}|{:>21s}'.format(records[x][0],x,records[x][1]))


# In[42]:


# [ ] You want to send a mass email to all company employees, so you need a list of all the email addresses in `records`
# Write a program to extract the email addresses from the `records` dictionary and store them in a list

# The output list should look like:
# ['suresh@example.com', 'colette@example.com', 'skye@example.com', 'hiroto@example.com', 'tobias@example.com', 'jin@example.com', 'joana@example.com', 'alton@example.com']

# Hint: use the `.values()` method

records = {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}
e = []
for x in records:
    e += [records[x][1]]
print(e)


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Dictionary Operations and Functions
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/d2352cf1-c9fc-4ce8-802e-9ccfeca618a6/DEV330x-3_4c_dictionary_operatio.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/aa0efac6-d0f9-44da-b80d-d1a22b958033/DEV330x-3_4c_dictionary_operations_and_functions.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# Python supports several functions and dictionary operations such as containment, identity, and dictionary length. You will explore some of them in the following examples.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 

# ### Containment (`in`, `not in`)
# 
# 

# #### _key_ containment
# You can test if a value is one of the dictionary keys by using the (`in`) and (`not in`) containment operators. 
# 
# When testing the containment, you can use the `.keys()` method or just the name of the dictionary, Python will generate the same results. 

# In[44]:


# Create a dictionary of grocery items and associated prices
groceries = {'Bread':2.26, 'Milk':3.62, 'Chocolate':1.59}

item = input("Please enter an item name: ")

# Using .keys()
if (item in groceries.keys()):
    print("Price of {} is: ${:4.2f}".format(item, groceries[item]))
elif (item not in groceries):
    print("Price not in the dictionary")


# In[45]:


# Create a dictionary of grocery items and associated prices
groceries = {'Bread':2.26, 'Milk':3.62, 'Chocolate':1.59}

item = input("Please enter a item: ")

# Without using .keys()
if (item in groceries):
    print("Price of {} is: ${:4.2f}".format(item, groceries[item]))
elif (item not in groceries):
    print("Price not in the dictionary")


# #### _value_ containment
# You can test if a value is one of the dictionary values by using the (`in`) and (`not in`) containment operators and the `.values()` method. Unlike _key_ containment, you cannot use only the dictionary name.

# In[46]:


# Create a dictionary of grocery items and associated prices
groceries = {'Bread':2.26, 'Milk':3.62, 'Chocolate':1.59}

price = float(input("Please enter an exact price: "))

if (price in groceries.values()):
    print("There is a matching grocery")
else:
    print("There are no groceries matching this price")


# ### Identity (`is`) and equality (`==`)
# 
# When comparing two tuples or lists using the equality operator `==`, the result would be `True` if and only if both sequences had the same exact elements and in the same order. Of course, being equal does not indicate that the sequences are identical as you saw earlier.
# 
# For dictionaries, the order of the items is not important. Thus, two dictionaries can be equal despite the fact that they store the elements in a different order. Identity of dictionaries is the same as identities of tuples and lists; changing one of two identical dictionaries will also change the other.

# In[47]:


# Create 2 equal but not identical dictionaries
D1 = {0:'number 0', 1:'number 1', 2:'number 2'}
D2 = {1:'number 1', 0:'number 0', 2:'number 2'}

print("Equality: D1 == D2 ?", D1 == D2)
print("Identity: D1 is D2 ?", D1 is D2)


# In[48]:


# Create 2 equal and identical dictionaries
D1 = {0:'number 0', 1:'number 1', 2:'number 2'}
D2 = D1
D1[0] = 'changed number'

print("Equality: D1 == D2 ?", D1 == D2)
print("Identity: D1 is D2 ?", D1 is D2)

print("D2 after changing D1:", D2)


# ### Length of a dictionary
# The length of a dictionary is the number of key:value pairs it contains. You can find out this number by using the `len()` function.

# In[49]:


# Create a dictionary of grocery items and associated prices
groceries = {'Bread':2.26, 'Milk':3.62, 'Chocolate':1.59}

# The length of a dictionary = how many key:value pairs it has
print("{} groceries total".format(len(groceries)))


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# 
# ## Dictionary Operations and Functions

# In[50]:


# Write a program that can ONLY update the price of an existing grocery
#in the `groceries` dictionary.
# The item and updated price should be entered by the user.
# If the user enters a new item, the program should not create 
# a new dictionary item. It should instead display an error message.

groceries = {'Bread':2.26, 'Milk':3.62, 'Chocolate':1.59}
i = input("Item? ")
if (i in groceries):
    groceries[i] = float(input("Price? "))
    print(groceries)
else:
    print("Item not found")


# In[52]:


# [ ] Write a program to find out the number of employees stored in `records`.

records = {57394: ['Suresh Datta', 'suresh@example.com'], 48539: ['Colette Browning', 'colette@example.com'], 58302: ['Skye Homsi', 'skye@example.com'], 48502: ['Hiroto Yamaguchi', 'hiroto@example.com'], 48291: ['Tobias Ledford', 'tobias@example.com'], 48293: ['Jin Xu', 'jin@example.com'], 23945: ['Joana Dias', 'joana@example.com'], 85823: ['Alton Derosa', 'alton@example.com']}
print(len(records))

