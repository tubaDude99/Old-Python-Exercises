#!/usr/bin/env python
# coding: utf-8

# # Section 4.4: Documenting Functions (`pydoc`)
# * pydoc
# 
# ### Students will be able to:
# * Use pydoc to generate text documentation
# * Use pydoc to generate HTML documentation

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Generating Documentation by Using `pydoc`
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/250ee08c-fd50-4f86-881a-21200af1bb87/DEV330x-4_4a_pydoc.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/23494b98-0fca-4ae3-9101-3c4e1d101b67/DEV330x-4_4a_pydoc.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# `pydoc` is a Python module that can automatically generate documentation using the docstrings in a module. It imports the module to generate its documentation; therefore, you should always use `__name__ == "__main__"` to suppress any function from running when the documentation is being generated. The output of `pydoc` can be in text format or HTML format. 
# 
# To generate text documentation for a module contained in `test.py`, run the following command:
# 
# ```bash
# pydoc test
# ```
# 
# To generate HTML documentation for `test.py`, run the command with the `-w` flag as follows:
# 
# ```bash
# pydoc -w test
# ```

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 

# In[1]:


get_ipython().run_line_magic('cd', 'command_line/')


# ## Converting Celsius to Fahrenheit

# In[2]:


get_ipython().run_cell_magic('writefile', 'c2f.py', '\ndef C2F(degrees_celsius):\n    """ Convert Celsius to Fahrenheit"""\n    return degrees_celsius * (9/5) + 32\n\nprint("Accessing docstrings using __doc__:\\n")\nprint(C2F.__doc__)')


# Running `pydoc` in the terminal generates:

# In[3]:


get_ipython().run_cell_magic('bash', '', '\npydoc c2f')


# ## Converting Kilograms (kg) to Pounds (lb)

# In[2]:


get_ipython().run_cell_magic('writefile', 'kg2lb.py', '\ndef kg2lb(kilograms):\n    """\n    Convert kilograms to pounds\n    \n    args:\n        kilograms: float weight in kg \n    \n    returns:\n        pounds: float weight in lb\n    """\n    \n    pounds = kilograms * 2.20462262185\n    return pounds\n\nif __name__ == "__main__":\n    pass')


# Running `pydoc` in the terminal generates:

# In[3]:


get_ipython().run_cell_magic('bash', '', '\npydoc kg2lb')


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Generating Documentation by Using `pydoc`

# The following program is the currency converter from a previous task. Generate the text documentation.
# 
# NOTE: You do not need to complete the function's code to generate the documentation pages.

# In[4]:


get_ipython().run_cell_magic('writefile', 'currency_converter.py', '\ndef USD2EUR(amount):\n    """\n    Convert amount from US Dollars to Euros.\n    \n    Use 1 USD = 0.831467 EUR\n    \n    args:\n        amount: US dollar amount (float)\n        \n    returns:\n        value: the equivalent of amount in Euros (float)\n    """\n    #TODO: Your code goes here\n    return value\n\ndef EUR2GBP(amount):\n    """\n    Convert amount from Euros to British Pounds.\n    \n    Use 1 EUR = 0.889358 GBP\n    \n    args:\n        amount: Euros amount (float)\n        \n    returns:\n        value: the equivalent of amount in GBP (float)\n    """\n    #TODO: Your code goes here\n    return value\n\ndef USD2GBP(amount):\n    """\n    Convert amount from US Dollars to British Pounds.\n    \n    The conversion rate is unknown, you have to use USD2EUR and EUR2GBP\n    \n    args:\n        amount: US dollar amount (float)\n        \n    returns:\n        value: the equivalent of amount in British Pounds (float)\n    """\n    #TODO: Your code goes here\n \n    return value\n\ndef main():\n    amount = float(input("Enter amount in USD: $"))\n    \n    # In British Pounds\n    gbp = USD2GBP(amount)\n    \n    print("${:.2f} USD = {:.2f} GBP".format(amount, gbp))\n    \nif __name__ == \'__main__\':\n    main()')


# In[5]:


get_ipython().run_cell_magic('bash', '', '\npydoc currency_converter')

