#!/usr/bin/env python
# coding: utf-8

# # Module 4 Practice  
# 
# ### Student will be able to
# 
# ## 3-4.1 Script Environment & Command Line Arguments
# * Distinguish if a Python code is running as a script or being imported as a module
# * Recognize the basic structure of a Unix command line
# * Parse command line arguments:
#     * Use add_argument method to parse command line arguments
#     * Add positional arguments
#     * Add optional arguments
#     * Utilize the parameters of add_argument to control how it works
# * Employ the parsed command line argument in a practical application
# 
# ## 3-4.2 Variable Scope
# * Define local variables
# * Read and modify the value of local variables
# * Identify the scope of a variable
# * Define global variables
# * Read the value of global variables from local scopes
# * Modify the value of global variables from local scopes
# 
# ## 3-4.3 Documenting Functions (Docstring)
# * Write one-line docstrings
# * Write multi-line docstrings
# * Access docstrings
# 
# ## 3-4.4 Documenting Functions (`pydoc`) 
# * Use pydoc to generate textual documentation
# * Use pydoc to generate HTML textual documentation

# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Script environment ( `__name__` )

# ## Change working directory to `command_line`
# 
# Necessary so all generated files are saved in this directory, the cell will generate an error message if you are already in the `command_line` directory.

# In[4]:


get_ipython().run_line_magic('cd', 'command_line')


# ## Sentence counter

# In[1]:


# [ ] The following program contains a few functions to count the number of: vowels, consonants, and digits in a sentence.
# Modify the program so it only run the test case when the program is executed directly. 
# In other words, when the program is imported as a module for another program, it shouldn't display the test cases.

def count_vowels(sentence):
    """Count the number of vowels in sentence."""
    vowels = 0
    for c in sentence:
        if c.lower() in "aeiouy":
            vowels = vowels + 1
    return vowels

def count_consonants(sentence):
    """Count the number of consonants in sentence."""
    consonants = 0
    for c in sentence:
        if c.isalpha():
            if c.lower() not in "aeiouy":
                consonants = consonants + 1
    return consonants

def count_digits(sentence):
    """Count the number of digits in sentence."""
    digits = 0
    for c in sentence:
        if c.isdigit():
            digits = digits + 1
    return digits

def main():
    test_sentence = "Plan 2 is not working!"
    print("Number of vowels = {:d}".format(count_vowels(test_sentence)))
    print("Number of consonants = {:d}".format(count_consonants(test_sentence)))
    print("Number of digits = {:d}".format(count_digits(test_sentence)))
    
if __name__ == '__main__':
    main()


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Parsing command line arguments

# ## Change working directory to `command_line`
# 
# Necessary so all generated files are saved in this directory, the cell will generate an error message if you are already in the `command_line` directory.

# In[3]:


get_ipython().run_line_magic('cd', 'command_line')


# ## Character art
# 
# The following program is saved as `stairs.py`. Once you complete the task, you can test it using the next `bash` code cell

# In[8]:


get_ipython().run_cell_magic('writefile', 'stairs.py', '\n# [ ] The following program generates a staircase character art\n# The `size` variable controls the number of steps\n# The `base_shape` defines the characters used to generate the art\n# Modify the program so the `size` is set as a positional command line argument, and base_shape as an optional \n# command line argument with a default value of `[]`\nimport argparse\np = argparse.ArgumentParser()\np.add_argument(\'size\', type = int, help = \'Number of steps\')\np.add_argument(\'-b\', \'--base_shape\', type = str, default = \'[]\', help = \'Base shape used in generation\')\nargs = p.parse_args()\ndef gen_stairs(steps, base_shape):\n    for row in range(steps):\n        for col in range(steps):\n            if(col <= row):\n                print(base_shape, end = "")\n        print()\n\n# Generate a staircase with 6 steps using \'[]` as a base shape\ngen_stairs(args.size, args.base_shape)')


# In[11]:


get_ipython().run_cell_magic('bash', '', "\npython3 stairs.py 7 -b 'x'")


# ## Days counter

# In[24]:


get_ipython().run_cell_magic('writefile', 'day_counter.py', '\n# [ ] Write a program that reads a date from the command line as numbers (month  then day then year),\n# if the date entered is in the past, a message saying "The date has passed" should be printed\n# if the date is in the future the program should display the number of days remaining from today till that date,\n# there should be an optional command line flag that displays the results in total number of seconds instead of days\n\n# help message should look like:\n\'\'\'\nusage: day_counter.py [-h] [-s] month day year\n\npositional arguments:\n  month                Month as a number (1, 12)\n  day                  Day as a number (1, 31) depending on the month\n  year                 Year as a 4 digits number (2018)\n\noptional arguments:\n  -h, --help           show this help message and exit\n  -s, --total_seconds  Show the time difference in total number of seconds\n\'\'\'\nimport argparse\nfrom datetime import datetime\np = argparse.ArgumentParser()\np.add_argument(\'month\', type = int, help = \'Month as a number (1, 12)\')\np.add_argument(\'day\', type = int, help = \'Day as a number (1, 31) depending on the month\')\np.add_argument(\'year\', type = int, help = \'Year as a 4 digits number (2018)\')\np.add_argument(\'-s\', \'--total_seconds\', action = \'store_true\', help = \'Show the time difference in total number of seconds\')\nargs = p.parse_args()\ntry:\n    inpD = datetime(month = args.month, day = args.day, year = args.year)\nexcept:\n    pass\ntd = datetime.today()\nif inpD < td:\n    print(\'The date has passed\')\nelif inpD > td:\n    print(\'You\\\'re %s days too early\' %str((inpD - td).days))\n    if args.total_seconds:\n        print(\'That is %s seconds\' %str((inpD-td).total_seconds()))')


# In[26]:


get_ipython().run_cell_magic('bash', '', '\npython3 day_counter.py 3 2 2025 -s')


# ## Adder
# 

# In[ ]:


get_ipython().run_cell_magic('writefile', 'adder.py', '\n# [ ] Write a program that reads an unspecified number of integers from the command line,\n# then prints out the sum of all the numbers\n# the program should also have an optional argument to show the product of the numbers (in addition to the sum)\n\n\n# help message should look like:\n\'\'\'\nusage: adder.py [-h] [-p] [numbers [numbers ...]]\n\npositional arguments:\n  numbers        numbers to be added (or multiplied)\n\noptional arguments:\n  -h, --help     show this help message and exit\n  -p, --product  show the product of the numbers (in addition to the displayed\n                 sum)\n\'\'\'\n\n# --Completed--\n\nimport argparse\n\n# define an argument parser object\nparser = argparse.ArgumentParser()\n\n# Add positional arguments\nparser.add_argument(\'numbers\', type = int, metavar = \'numbers\', nargs = \'*\', help = "numbers to be added (or multiplied)")\n\n# Add optional arguments\nparser.add_argument(\'-p\', \'--product\', action = \'store_true\', help = \'show the product of the numbers (in addition to the displayed sum)\')\n\n# parse command line arguments\nargs = parser.parse_args()\n\n# program\n\na = 0 # accumulate sum\np = 1 # accumulate products\n\nfor num in args.numbers:\n    a = a + num\n    p = p * num\n    \nprint("The sum = {:d}".format(a))\n\nif (args.product):\n    print("The product = {:d}".format(p))')


# In[ ]:


get_ipython().run_cell_magic('bash', '', '\npython3 adder.py 2 3 5 10 -p')


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# 
# ## Local variables

# ## Fix the errors

# In[ ]:


# The following program displays the double of a number
# Fix the error/s in the program so the correct answer is displayed

def double(num):
    answer = num * 2
    return answer

double(6)

print(answer)

# --Completed--
def double(num):
    answer = num * 2
    return answer

answer = double(6)

print(answer)


# ## Length Converter

# In[ ]:


# [ ] The program below converts a length from Centimeters to Inches, Feet, Yards, and Miles
# Complete the functions cent2inches, cent2feet, cent2yards, cent2miles so they all return the expected result


def cent2inches(length):
    """
    Convert length from Centimeters to Inches.
    
    1 Centimeter = 0.393701 Inches
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Inches (float)
    """
    
    #TODO: Your code goes here
    return result

def cent2feet(length):
    """
    Convert length from Centimeters to Feet.
    
    1 Centimeter = 0.0328084 Feet
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Feet (float)
    """
    
    #TODO: Your code goes here
    return result

def cent2yards(length):
    """
    Convert length from Centimeters to Yards.
    
    1 Centimeter = 0.0109361 Yards
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Yards (float)
    """
    
    #TODO: Your code goes here
    return result

def cent2miles(length):
    """
    Convert length from Centimeters to Miles.
    
    1 Centimeter = 6.2137e-6 Miles
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Miles (float)
    """
    
    #TODO: Your code goes here
    return result

def main():
    length = float(input("Enter length in Centimeters: "))
    
    # In Inches
    inches = cent2inches(length)
    
    # In Feet
    feet = cent2feet(length)
    
    # In Yards
    yards = cent2yards(length)
    
    # In Miles
    miles = cent2miles(length)
    
    print('{:.2f} [cm] = {:.2f} [inches]", {:.2f} [feet], {:.2f} [yards], {:.2e} [miles]'.format(length, inches, feet, yards, miles))
    
if __name__ == '__main__':
    main()
    
    
# --Completed--
def cent2inches(length):
    """
    Convert length from Centimeters to Inches.
    
    1 Centimeter = 0.393701 Inches
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Inches (float)
    """
    
    result = length * 0.393701
    return result

def cent2feet(length):
    """
    Convert length from Centimeters to Feet.
    
    1 Centimeter = 0.0328084 Feet
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Feet (float)
    """
    
    result = length * 0.0328084
    return result

def cent2yards(length):
    """
    Convert length from Centimeters to Yards.
    
    1 Centimeter = 0.0109361 Yards
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Yards (float)
    """
    
    result = length * 0.0109361
    return result

def cent2miles(length):
    """
    Convert length from Centimeters to Miles.
    
    1 Centimeter = 6.2137e-6 Miles
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Miles (float)
    """
    
    result = length * 6.2137e-6
    return result

def main():
    length = float(input("Enter length in Centimeters: "))
    
    # In Inches
    inches = cent2inches(length)
    
    # In Feet
    feet = cent2feet(length)
    
    # In Yards
    yards = cent2yards(length)
    
    # In Miles
    miles = cent2miles(length)
    
    print('{:.2f} [cm] = {:.2f} [inches]", {:.2f} [feet], {:.2f} [yards], {:.2e} [miles]'.format(length, inches, feet, yards, miles))
    
if __name__ == '__main__':
    main()
    
    


# In[ ]:


# [ ] The program below converts a length from Centimeters to Feet without using direct conversion
# Complete the functions cent2inches, inches2feet, and cent2feet so they return the expected result
# You should use cent2inches and inchest2feet in cent2feet

def cent2inches(length):
    """
    Convert length from Centimeters to Inches.
    
    1 Centimeter = 0.393701 Inches
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Inches (float)
    """
    
    #TODO: Your code goes here
    return result

def inches2feet(length):
    """
    Convert length from Inches to Feet.
    
    1 Inch = 0.0833333 Feet
    
    args:
        length: in Inches (float)
        
    results:
        result: equivalent length in Feet (float)
    """
    
    #TODO: Your code goes here
    return result

def cent2feet(length):
    """
    Convert length from Centimeters to Yards.
    
    The conversion rate is unknown, you have to use cent2inches and inches2feet
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Yards (float)
    """
    
    #TODO: Your code goes here
    return result

def main():
    length = float(input("Enter length in Centimeters: "))
    
    # In Feet
    feet = cent2feet(length)
    
    print('{:.2f} [cm] = {:.2f} [feet]'.format(length, feet))
    
if __name__ == '__main__':
    main()
    
    
# --Completed--
def cent2inches(length):
    """
    Convert length from Centimeters to Inches.
    
    1 Centimeter = 0.393701 Inches
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Inches (float)
    """
    
    result = length * 0.393701
    return result

def inches2feet(length):
    """
    Convert length from Inches to Feet.
    
    1 Inch = 0.0833333 Feet
    
    args:
        length: in Inches (float)
        
    results:
        result: equivalent length in Feet (float)
    """
    
    result = length * 0.0833333
    return result

def cent2feet(length):
    """
    Convert length from Centimeters to Yards.
    
    The conversion rate is unknown, you have to use cent2inches and inches2feet
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Yards (float)
    """
    
    result = cent2inches(length)
    result = inches2feet(result)
    return result

def main():
    length = float(input("Enter length in Centimeters: "))
    
    # In Feet
    feet = cent2feet(length)
    
    print('{:.2f} [cm] = {:.2f} [feet]'.format(length, feet))
    
if __name__ == '__main__':
    main()
    
    


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4</B></font>
# 
# ## Global variables

# ### Formatted Phone Number

# In[ ]:


# [ ] Complete the function `formatted_phone()` so it displays the PHONE number as 777-248-3940

PHONE = "7895550153"

def formatted_phone():
    #TODO: Your code goes here
    pass
    
formatted_phone()

# --Completed--
PHONE = "7772483940"

def formatted_phone():
    print(PHONE[0:3] + '-' + PHONE[3:6] + '-' + PHONE[6:])
    
formatted_phone()


# ### Changing global variables

# In[ ]:


# [ ] In the following program, the function change_x should change the value stored in x from 5 to 7
# modify the function so the value of x is changed from within the function

x = 5

def change_x():
    x = 7
    
print("Before change x =", x) # should be 5
change_x()
print("After change x =", x) # should be 7

# --Completed--
x = 5

def change_x():
    global x #<---------------
    x = 7
    
print("Before change x =", x) # should be 5
change_x()
print("After change x =", x) # should be 7


# In[ ]:


# [ ] The function upper_case should change the NAME to upper case
# correct the function so that NAME is changed permanently

# HINT: Use the string function str.upper()

NAME = "Skye Homsi"

def upper_case():
    return NAME
    

print("Current name case:", NAME)
upper_case()
print("Updated name case:", NAME)

# --Completed--
NAME = "Skye Homsi"

def upper_case():
    global NAME #<-----------
    NAME = NAME.upper()#<-----------
                      #<-----------
    

print("Current name case:", NAME)
upper_case()
print("Updated name case:", NAME)


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 5</B></font>
# 
# ## Docstrings

# In[ ]:


# [ ] The function `average` computes the average of a list (or tuple) T
# Document the function using a one-line docstring

def average(T):
    s = 0
    for num in T:
        s = s + num
    
    return s / len(T)
    
# --Completed--
def average(T):
    """Compute the average of the numbers in list (or tuple) T."""
    s = 0
    for num in T:
        s = s + num
    
    return s / len(T)


# In[ ]:


# [ ] The following functions compute the area and average of a circle with radius r
# Document both function using a one-line docstring

from math import pi

def circle_area(r):
    return pi * r ** 2

def circle_circumference(r):
    return 2 * pi * r

# --Completed--
from math import pi

def circle_area(r):
    """Compute the area of a circle with radius (r)."""
    return pi * r ** 2

def circle_circumference(r):
    """Compute the circumference of a circle with radius (r)"""
    return 2 * pi * r


# In[ ]:


# [ ] As you saw before, the function gen_stairs generates a number of stairs using (base_shape)
# Document the function using a multi-line docstring

def gen_stairs(steps, base_shape):
    for row in range(steps):
        for col in range(steps):
            if(col <= row):
                print(base_shape, end = "")
        print()

# Generate a staircase with 6 steps using '[]` as a base shape               
gen_stairs(6, '[]')

# --Completed--

def gen_stairs(steps, base_shape):
    """
    Generate stairs character with a specific size and base shape.
    
    args:
        steps: number of steps to generate
        base_shape: The string base shape to use in constructing the stairs
        
    returns:
        None
    """
    
    for row in range(steps):
        for col in range(steps):
            if(col <= row):
                print(base_shape, end = "")
        print()

# Generate a staircase with 6 steps using '[]` as a base shape               
gen_stairs(6, '[]')


# In[ ]:


# [ ] The following function returns the minimum and maximum of a tuple (or list) T
# # Document the function using a multi-line docstring

def min_max(T):
    return (min(T), max(T))

# --Completed--

def min_max(T):
    """
    Return the minimum and maximum values of tuple (or list) T
    
    args:
        T: tuple or list of arbitrary length
        
    returns:
        (min, max): a tuple containing the minimum and maximum values of T in order
    """
    
    return (min(T), max(T))


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 6</B></font>
# 
# ## `pydoc`

# The following program is a code from a previous module. Though the working code is not included, the documentation is thorough and complete. Use `pydoc` to generate the textual documentation page.
# 
# NOTE: You do not need to complete the functions' code to generate the documentation pages

# In[ ]:


get_ipython().run_cell_magic('writefile', 'weather.py', '\n# [ ] In this project, you will read a CSV file containing about 25K lines of weather information \n# and store the information in a Python dictionary. You will then use the dictionary to find out\n# the hottest, coldest, rainiest years and so on...\n# You will see that the dictionary\'s search optimization algorithms will allow you to explore \n# this large dataset without any noticeable delays.\n\n# The logic of the program is in the `main` function, read it before writing any code.\n\n# Use the description and examples under each of the following functions to implement them:\n# 1) convert_file(file_path)\n# 2) add_rainy(weather)\n# 3) consolidate(weather)\n# 4) year_info(year, yearly_weather)\n# 5) hottest(yearly_weather)\n# 6) coldest(yearly_weather)\n# 7) rainiest_days(yearly_weather)\n# 8) highest_prcp(yearly_weather)\n\n\nfrom datetime import date, datetime\n\ndef convert_file(file_path):\n    """\n    Convert CSV file to a Python dictionary.\n    \n    The CSV file contains daily weather information arranged in rows,\n    the rows contain  (date, precipitation (inches), maximum temperature (F), minimum temperature (F)) in order.\n    First line in CSV file is a header (DATE, PRCP, TMAX, TMIN), the rest contain the weather data.\n    \n    The function should read the data in the file and generate a dictionary where:\n        1) keys are date objects (from the datetime module), using the daily date info in the file\n        2) values are lists containing [TMAX, TMIN, PRCP] in order\n        \n    args:\n        file_path: path to the CSV file\n    \n    returns:\n        weather: the generated dictionary using date objects as keys and lists of weather info as values\n        \n    examples:\n    Input CSV file:\n    DATE,PRCP,TMAX,TMIN\n    12/10/2017,0,49,34\n    12/11/2017,0,49,29\n    12/12/2017,0,46,32\n    12/13/2017,0,48,34\n    12/14/2017,0,50,36\n    12/15/2017,0.06,43,37\n    12/16/2017,0.14,45,37\n    12/17/2017,0.03,50,42\n    12/18/2017,0.7,49,41\n    12/19/2017,1,50,40\n    12/20/2017,0.13,49,32\n    12/21/2017,0.01,41,29\n    12/22/2017,0.09,40,35\n    12/23/2017,0,38,29\n    12/24/2017,0.12,38,28\n\n    Output dictionary (weather):\n    {datetime.date(2017, 12, 10): [49, 34, 0.0],\n     datetime.date(2017, 12, 11): [49, 29, 0.0],\n     datetime.date(2017, 12, 12): [46, 32, 0.0],\n     datetime.date(2017, 12, 13): [48, 34, 0.0],\n     datetime.date(2017, 12, 14): [50, 36, 0.0],\n     datetime.date(2017, 12, 15): [43, 37, 0.06],\n     datetime.date(2017, 12, 16): [45, 37, 0.14],\n     datetime.date(2017, 12, 17): [50, 42, 0.03],\n     datetime.date(2017, 12, 18): [49, 41, 0.7],\n     datetime.date(2017, 12, 19): [50, 40, 1.0],\n     datetime.date(2017, 12, 20): [49, 32, 0.13],\n     datetime.date(2017, 12, 21): [41, 29, 0.01],\n     datetime.date(2017, 12, 22): [40, 35, 0.09],\n     datetime.date(2017, 12, 23): [38, 29, 0.0],\n     datetime.date(2017, 12, 24): [38, 28, 0.12]}\n    """\n    #TODO: Your code goes here, see hints below\n    \n    # open the file for reading (HINT: use `with` statement)\n\n    # ignore the first header line (DATE, PRCP, TMAX, TMIN)\n\n    # remove newline characters from end of each line (HINT: use str.rstrip())\n\n    # split line into a list (HINT: use str.split(\',\'))\n\n    # create the date object from the first list element (HINT: use the date_creater(date_string) function provided below)\n\n    # read the weather related variables\n    # precipitation\n    # maximum temperature\n    # minimum temperature\n    \n    # create dictionary key:value pair\n    pass\n\ndef add_rainy(weather):\n    """\n    Emphasize rainy days using Boolean values.\n    \n    Modify the weather dictionary by adding another Boolean element to the values\' lists. \n    If precipitation is observed on a day (more than 0"), the associated list is appended by True.\n    If precipitation is not observed (0"), the associated list is appended by False.\n    \n    args:\n        weather: dictionary, keys are date objects and values are lists [TMAX, TMIN, PRCP]\n        \n    returns:\n        None: the weather dictionary is modified directly, keys are date objects and values are lists [TMAX, TMIN, PRCP, RAINY_DAY]\n        \n    examples:\n    Input weather dictionary:\n    {datetime.date(2017, 12, 10): [49, 34, 0.0],\n     datetime.date(2017, 12, 11): [49, 29, 0.0],\n     datetime.date(2017, 12, 12): [46, 32, 0.0],\n     datetime.date(2017, 12, 13): [48, 34, 0.0],\n     datetime.date(2017, 12, 14): [50, 36, 0.0],\n     datetime.date(2017, 12, 15): [43, 37, 0.06],\n     datetime.date(2017, 12, 16): [45, 37, 0.14],\n     datetime.date(2017, 12, 17): [50, 42, 0.03],\n     datetime.date(2017, 12, 18): [49, 41, 0.7],\n     datetime.date(2017, 12, 19): [50, 40, 1.0],\n     datetime.date(2017, 12, 20): [49, 32, 0.13],\n     datetime.date(2017, 12, 21): [41, 29, 0.01],\n     datetime.date(2017, 12, 22): [40, 35, 0.09],\n     datetime.date(2017, 12, 23): [38, 29, 0.0],\n     datetime.date(2017, 12, 24): [38, 28, 0.12]}\n    \n    Updated weather dictionary with Boolean values\n    {datetime.date(2017, 12, 10): [49, 34, 0.0, False],\n     datetime.date(2017, 12, 11): [49, 29, 0.0, False],\n     datetime.date(2017, 12, 12): [46, 32, 0.0, False],\n     datetime.date(2017, 12, 13): [48, 34, 0.0, False],\n     datetime.date(2017, 12, 14): [50, 36, 0.0, False],\n     datetime.date(2017, 12, 15): [43, 37, 0.06, True],\n     datetime.date(2017, 12, 16): [45, 37, 0.14, True],\n     datetime.date(2017, 12, 17): [50, 42, 0.03, True],\n     datetime.date(2017, 12, 18): [49, 41, 0.7, True],\n     datetime.date(2017, 12, 19): [50, 40, 1.0, True],\n     datetime.date(2017, 12, 20): [49, 32, 0.13, True],\n     datetime.date(2017, 12, 21): [41, 29, 0.01, True],\n     datetime.date(2017, 12, 22): [40, 35, 0.09, True],\n     datetime.date(2017, 12, 23): [38, 29, 0.0, False],\n     datetime.date(2017, 12, 24): [38, 28, 0.12, True]}\n    """\n    #TODO: Your code goes here\n    pass\n\ndef consolidate(weather):\n    """\n    Consolidate the daily weather information by year.\n    \n    Use the weather dictionary to generate a new consolidated dictionary (yearly_weather). \n    The new dictionary uses years as keys, and the associated values are lists containing (in order):\n        1) The average of the highest recorded temperatures in the year (AVG_TMAX)\n        2) The average of the lowest recorded temperatures in the year (AVG_TMIN)\n        3) The total recorded precipitation in the year (TOTAL_PRCP)\n        4) The total number of rainy days in the year (TOTAL_RAINY_DAYS)\n        5) The number of recorded days (TOTAL_DAYS). \n           This element is necessary to account for days where the station breaks (missing recordings),\n           or if the year hasn\'t finished yet.\n           \n    args: \n        weather: dictionary, keys are date objects and values are lists [TMAX, TMIN, PRCP, RAINY_DAY]\n    \n    returns:\n        yearly_weather: consolidated dictionary, keys are years (int), values are lists \n                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS]\n                        \n    examples:\n    Input weather dictionary:\n    {datetime.date(2017, 12, 10): [49, 34, 0.0, False],\n     datetime.date(2017, 12, 11): [49, 29, 0.0, False],\n     datetime.date(2017, 12, 12): [46, 32, 0.0, False],\n     datetime.date(2017, 12, 13): [48, 34, 0.0, False],\n     datetime.date(2017, 12, 14): [50, 36, 0.0, False],\n     datetime.date(2017, 12, 15): [43, 37, 0.06, True],\n     datetime.date(2017, 12, 16): [45, 37, 0.14, True],\n     datetime.date(2017, 12, 17): [50, 42, 0.03, True],\n     datetime.date(2017, 12, 18): [49, 41, 0.7, True],\n     datetime.date(2017, 12, 19): [50, 40, 1.0, True],\n     datetime.date(2017, 12, 20): [49, 32, 0.13, True],\n     datetime.date(2017, 12, 21): [41, 29, 0.01, True],\n     datetime.date(2017, 12, 22): [40, 35, 0.09, True],\n     datetime.date(2017, 12, 23): [38, 29, 0.0, False],\n     datetime.date(2017, 12, 24): [38, 28, 0.12, True]}\n     \n     Output yearly_weather dictionary:\n     {2017: [45.666666666666664, 34.333333333333336, 2.28, 9, 15]}\n    """    \n    #TODO: Your code goes here\n    pass\n\ndef year_info(year, yearly_weather):\n    """\n    Convert the year\'s weather information to a formatted string.\n    \n    Look for the weather information of `year` in the `yearly_weather` dictionary.\n    If it exists, convert the information list into a formatted string:\n            YEAR | AVG_TMAX | AVG_TMIN | TOTAL_PRCP | TOTAL_RAINY_DAYS | TOTAL_DAYS\n    If it does not exist, the formatted string should be:\n            N/A  |    N/A   |    N/A   |     N/A    |        N/A       |    N/A   \n    \n    args:\n        year: int value to look for in the yearly_weather dictionary\n        \n        yearly_weather: consolidated dictionary, keys are years (int), values are lists \n                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS] \n    \n    returns:\n        formatted_string: containing the year\'s weather information\n                          \n    examples:\n    Input yearly weather dictionary:\n    {2017: [45.666666666666664, 34.333333333333336, 2.28, 9, 15]}\n    \n    Output formatted string:\n    == year_info(2017, yearly_weather) == (contained in the dictionary)\n    \' 2017 |         45.67 |        34.33 |   2.28" |            9 |             15 \'\n    \n    == year_info(2055, yearly_weather) == (not contained in the dictionary)\n    \' N/A  |      N/A      |     N/A      |   N/A   |     N/A      |      N/A       \'\n    """\n    #TODO: Your code goes here\n    pass\n\ndef hottest(yearly_weather):\n    """\n    Find the hottest year in yearly_weather.\n    \n    Look through all the years in the yearly_weather dictionary and return the year with \n    the highest average maximum temperature (highest AVG_TMAX)\n    \n    args:\n        yearly_weather: consolidated dictionary, keys are years (int), values are lists \n                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS] \n    \n    returns:\n        hottest_year: the year with the highest maximum temperature average (AVG_TMAX)\n    """\n    #TODO: Your code goes here\n    pass\n\ndef coldest(yearly_weather):\n    """\n    Find the coldest year in yearly_weather.\n    \n    Look through all the years in the yearly_weather dictionary and return the year with \n    the lowest average minimum temperature (lowest AVG_TMIN)\n    \n    args:\n        yearly_weather: consolidated dictionary, keys are years (int), values are lists \n                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS] \n    \n    returns:\n        coldest_year: the year with the lowest minimum temperature average (AVG_TMIN)\n    """\n    #TODO: Your code goes here\n    pass\n\ndef rainiest_days(yearly_weather):\n    """\n    Find the year with the largest number of rainy days in yearly_weather.\n    \n    Look through all the years in the yearly_weather dictionary and return the year with \n    the largest TOTAL_RAINY_DAYS\n    \n    args:\n        yearly_weather: consolidated dictionary, keys are years (int), values are lists \n                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS] \n    \n    returns:\n        rainiest_year: the year with the largest number of rainy days\n    """\n    #TODO: Your code goes here\n    pass\n\ndef highest_prcp(yearly_weather):\n    """\n    Find the year with the highest total precipitation in yearly_weather.\n    \n    Look through all the years in the yearly_weather dictionary and return the year with \n    the largest TOTAL_PRCP\n    \n    args:\n        yearly_weather: consolidated dictionary, keys are years (int), values are lists \n                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS] \n    \n    returns:\n        rainiest_year: the year with the highest total precipitation\n    """\n    #TODO: Your code goes here\n    pass\n\ndef date_creater(date_string):\n    """Convert the date_string (formatted as m/d/yyyy) to a date object."""\n    d = datetime.strptime(date_string, "%m/%d/%Y")\n    return d.date()\n\ndef dashes(count):\n    """Print a fancy line of `count` dashes"""\n    print("o" + count *\'-\' + "o")\n\ndef page_header(title):\n    """Print a page header with a title surrounded by dashes"""\n    dashes(78)\n    print("|{:^78s}|".format(title))\n    dashes(78)\n\ndef table_header():\n    """Print the first row in a table  (header row)"""\n    print()\n    print(\' {0:^4s} | {1:^13s} | {2:^12s} | {3:^7s} | {4:^12s} | {5:^14s} \'.format("Year", "Avg High Temp", "Avg Low Temp", "Percip", "# Rainy days", "# Recorded days"))\n    dashes(78)\n    \ndef display(title, years, yearly_weather):\n    """Print a page with a header, title, and the weather information of all years as found in yearly_weather"""\n    clear_output()\n    page_header(title)\n    table_header()\n    \n    # if years contain a single int, convert to a single item list\n    if type(years) is not list: years = [years]\n    \n    # print weather information for all years\n    for year in years:\n        print(year_info(year, yearly_weather)) \n        \n    # display this page till you go back to the main menu\n    while True:\n        m = input("Return to main menu [y/n]?")\n        if m in \'yesYesYES\':\n            break\n            \n\ndef main():\n    # convert the data in the (csv) file into a Python dictionary\n    weather = convert_file("data/seattle_weather.csv")\n    \n    # highlight rainy days by adding a Boolean entry to the dictionary\'s values\n    add_rainy(weather)\n    \n    # consolidate the weather data by year then store the result in a new dictionary\n    yearly_weather = consolidate(weather)\n    \n    # earliest and latest years on record\n    min_year = min(yearly_weather)\n    max_year = max(yearly_weather)\n    \n    # menus functionality\n    while True:\n        clear_output()\n\n        # display header\n        page_header("Weather Records")\n\n        # display main menu\n        print()\n        print("Main Menu (choose an option to display):\\n")\n        print("1. Summary of a certain year")\n        print("2. All years summary table")\n        print("3. Hottest year on record")\n        print("4. Coldest year on record")\n        print("5. Year with most rainy days")\n        print("6. Year with the highest precipitation")\n        print("7. Quit")\n        print()\n\n        # display footer with user input message\n        dashes(78)\n        while True:\n            try:\n                option = input("Select an option (1, 7): ")\n                option = int(option)\n                if 1 <= option <= 7:\n                    break # break the user input loop only, main loop does NOT break\n            except ValueError:\n                print("Cannot convert {:} to int".format(type(option)))\n        \n        \n        # execute relevant function\n        # 1. Summary of a certain year\n        if option == 1:\n            # ask the user for a valid year\n            while True:\n                try:\n                    year = input("Enter a year ({} - {})".format(min_year, max_year))\n                    year = int(year)\n                    if min_year <= year <= max_year:\n                        break\n                except ValueError:\n                    print("Cannot convert {:} to int".format(type(option)))\n            display("Year Summary", year, yearly_weather)\n\n        # 2. All years summary table \n        elif option == 2:\n            years = list(sorted(yearly_weather))\n            display("Tabular Summary", years, yearly_weather)\n       \n        # 3. Hottest year on record\n        elif option == 3:\n            year = hottest(yearly_weather)\n            display("Hottest year on record", year, yearly_weather)\n            \n        # 4. Coldest year on record   \n        elif option == 4:\n            year = coldest(yearly_weather)\n            display("Coldest year on record", year, yearly_weather)\n            \n        # 5. Year with most rainy days    \n        elif option == 5:\n            year = rainiest_days(yearly_weather)\n            display("Year with most rainy days", year, yearly_weather)\n        \n        # 6. Year with the highest precipitation\n        elif option == 6:\n            year = highest_prcp(yearly_weather)\n            display("Year with the highest precipitation", year, yearly_weather)\n            \n        # 7. Quit    \n        elif option == 7:\n            clear_output()\n            break\n    \n\n\n')


# In[ ]:


get_ipython().run_cell_magic('bash', '', '\npydoc weather')


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Module 4 Project</B></font>
# 
# ## Caesar Cipher
# 
# In this project, you will implement a program to encrypt and decrypt text using Caesar Cipher. The cipher is one of the oldest and simplest known encryption techniques known. It simply relies on substituting each character in a string by another character which is shifted by a certain number of places. For example, with a shift of 1 'a' becomes 'b', 'e' becomes 'f', and 'z' becomes 'a'. In the Caesar cipher, all characters are shifted by the same number of places and we refer to the shift value as key. 
# 
# To decrypt a message, you simply use the same key, which was used during the encryption procedure, to shift the characters back the same number of places. For example, with a key = 1 'b' becomes 'a', 'f' becomes 'e', and 'a' becomes 'z'. 
# 
# Since there are 26 letters in English, there are only 25 keys available for Caesar cipher. Therefore, it is easy to decipher a message without knowing the key. Simply use all possible keys to decrypt a message then read the outputs till one of them makes sense. This process is also implemented in the project.
# 

# ## Environment Setup
# 
# The following code blocks move the working directory to `command_line` and generate the necessary text file:
# * `plain_message.txt` : contains a plain message that will be encrypted
# * `encrypted_message.txt`: contains an encrypted message where the key is unknown

# ### Change working directory to `command_line`
# 
# Necessary so all generated files are saved in this directory, the cell will generate an error message if you are already in the `command_line` directory.

# In[ ]:


get_ipython().run_line_magic('cd', '"/home/nbuser/library/parent_dir/command_line"')


# ### Writing text files

# In[ ]:


get_ipython().run_cell_magic('writefile', 'plain_message.txt', '\nSoftware is a great combination between artistry and engineering.\n\n--Bill Gates')


# In[ ]:


get_ipython().run_cell_magic('writefile', 'encrypted_message.txt', '\nMHI LXVKXM!\n\nMabl fxlltzx ptl xgvkrimxw nlbgz dxr = gbgxmxxg.\n\ntuvwxyzabcdefghijklmnopqrs\n\nTUVWXYZABCDEFGHIJKLMNOPQRS')


# ## Program
# 
# To finish this project, run the environment setup code, read the `main` function, then use the description and examples under each of the following functions to implement them:
# * `parse_command_line()`
# * `read_file(file_path)`
# * `write_file(message, file_path)`
# * `transform(message, key, decrypt)`
# 
# Once you are done, use the terminal command line to:
# * Display the program's help message
# * Encrypt the text file `plain_message.txt` by key = 23 and save the result in `cipher_message.txt`
# * Find the key used to decrypt `encrypted_message.txt`

# In[ ]:


get_ipython().run_cell_magic('writefile', 'cipher.py', '\nimport argparse\n\ndef parse_command_line():\n    """\n    Parse the command line arguments and return the parse_args object.\n    \n    There should be 1 positional argument and 6 optional arguments.\n    The help message generated by the parser should look like:\n    \n    usage: cipher.py [-h] [-o outfile_path] [-k KEY] [-d] [-a] [-v] infile\n\n    positional arguments:\n      infile                input file to be encrypted or decrypted\n\n    optional arguments:\n      -h, --help            show this help message and exit\n      -o outfile_path, --outfile outfile_path\n                            output file\n      -k KEY, --key KEY     encryption/decryption key (must be positive) (default\n                            = 1)\n      -d, --decrypt         decrypt the input file\n      -a, --all             decrypt using all keys [1, 25], save outputs in\n                            different files. (useful in case the key is lost or\n                            unknown)\n      -v, --verbose         verbose mode\n\n\n    args:\n        None\n        \n    returns:\n        args: generated argparse object with all the passed command line arguments      \n    """\n    \n    #TODO: Your code goes here\n    #HINTS: Reveiw Jupyter Notebook 3-4.1  \n    pass\n\ndef read_file(file_path):\n    """\n    Read file_path and return the content as string.\n    \n    The file must be opened and closed and the function should handle exceptions when they are raised.\n    \n    args:\n        file_path: path to file\n        \n    returns:\n        message: content of file in file_path as a string\n    """\n    \n    #TODO: Your code goes here\n    pass\n            \ndef write_file(message, file_path):\n    """\n    Write the message in file_path.\n    \n    The file must be opened and closed and the function should handle exceptions when they are raised.\n    \n    args:\n        message: string to write in file\n        file_path: path to file\n        \n    returns:\n        None\n    """\n    \n    #TODO: Your code goes here\n    pass\n\ndef transform(message, key, decrypt):\n    """\n    Encrypt or decrypt a message using Caesar cipher.\n    \n    Encryption and decryption is determined by the Boolean value in decrypt. Key determines the number of \n    places a character is shifted. When encrypting, use the positive value of key to shift the characters forward; \n    when decrypting, use the negative key to shift the characters backward. \n    \n    The function should maintain characters that are not letters without change; for example, spaces, punctuations, \n    and numbers should not be encrypted or decrypted. Additionally, the case of the letters should be preserved, \n    small letters are transformed to other small letters and capital letters are transformed to capital letters.\n    \n    Use the function `shift` (provided later) to shift each character in message by the number in key.\n    \n    args:\n        message: string to be encrypted or decrypted\n        key: number of places to shift the characters (always positive)\n        decrypt: Boolean; when False the message is encrypted,  when True the message is decrypted\n        \n    returns:\n        transformed_message: encrypted (or decrypted) message\n        \n    examples:\n        Encryption\n        ==  transform("deal", 1, False) returns:\n            "efbm"\n        \n        ==  transform("deal", 2, False) returns:\n            "fgcn"\n        \n        ==  transform("deal", 30, False) is equivalent to transform(message, 4, False)\n            "hiep"\n        \n        Decryption\n        ==  transform("efbm", 1, True) returns:\n            "deal"\n            \n        ==  transform("fgcn", 2, True) returns:\n            "deal"\n            \n        ==  transform("hiep", 30, True) returns:\n            "deal"    \n        \n    """\n    \n    #TODO: Your code goes here\n    pass\n \ndef shift(char, key):    \n    """\n    Shift char by the value in key while maintaining the case (small/capital).\n    \n    If char contains non-letters (i.e. digits, punctuations, and white spaces), it is ignored.\n    \n    args:\n        char: character to shift\n        key: number of places to shift char\n        \n    returns:\n        shifted character\n        \n    examples:\n        shfit(\'a\', 1) ==> \'b\'\n        shift(\'z\', -1) ==> \'y\'\n        shift(\'A\', 5) ==> \'F\'\n        shift(\'H\', 7) ==> \'O\'\n        shift(\'o\', -10) ==> \'e\'\n        shift(\'a\', 30) ==> \'e\'\n    """\n    \n    # ordered lower case alphabet\n    alphabet = "abcdefghijklmnopqrstuvwxyz"\n    \n    # will contain shifted lower case alphabet\n    shifted_alphabet = \'\'\n    for i in range(len(alphabet)):\n        shifted_alphabet = shifted_alphabet + alphabet[(i + key) % 26]\n \n    if char.isalpha():\n        char_index = alphabet.index(char.lower())\n        shifted_char = shifted_alphabet[char_index]\n    \n        # keep char\'s case (upper or lower)\n        if char.isupper():\n            return shifted_char.upper()\n        else:\n            return shifted_char\n\ndef main():\n    # parse command line arguments\n    args = parse_command_line()\n    \n    # read content of infile to a string\n    instring = read_file(args.infile)\n    \n    # verbose\n    if args.verbose:\n        print("Input file:")\n        print("------------")\n        print(instring)\n        print()\n    \n    # key is specified\n    if not args.all:\n        # encrypt/decrypt content of infile\n        outstring = transform(instring, args.key, args.decrypt)\n    \n        # verbose\n        if args.verbose:\n            print("Output file:")\n            print("------------")\n            print(outstring)\n\n        # write content of outstring to outfile\n        write_file(outstring, args.outfile)\n    \n    # key is not specified, try all keys from 1 to 25 to decrypt infile\n    else:\n        for k in range(1, 26):\n            # decrypt content of infile\n            outstring = transform(instring, k, True)\n\n            # verbose\n            if args.verbose:\n                print("Key =", k)\n                print("------------")\n                print(outstring)\n                print()\n\n            # write content of outstring to outfile\n            write_file(outstring, "decrypted_by_" + str(k) + ".txt")\n    \nif __name__ == \'__main__\':\n    main()')


# In[ ]:


# --Completed--
%%writefile cipher.py

import argparse

def parse_command_line():
    """
    Parse the command line arguments and return the parse_args object.
    
    There should be 1 positional argument and 6 optional arguments.
    The help message generated by the parser should look like:
    
    usage: cipher.py [-h] [-o outfile_path] [-k KEY] [-d] [-a] [-v] infile

    positional arguments:
      infile                input file to be encrypted or decrypted

    optional arguments:
      -h, --help            show this help message and exit
      -o outfile_path, --outfile outfile_path
                            output file
      -k KEY, --key KEY     encryption/decryption key (must be positive) (default
                            = 1)
      -d, --decrypt         decrypt the input file
      -a, --all             decrypt using all keys [1, 25], save outputs in
                            different files. (useful in case the key is lost or
                            unknown)
      -v, --verbose         verbose mode


    args:
        None
        
    returns:
        args: generated argparse object with all the passed command line arguments      
    """
    
    # define an argument parser object
    parser = argparse.ArgumentParser()

    # Add positional arguments
    parser.add_argument('infile', type = str, help = "input file to be encrypted or decrypted")
    
    # Add optional arguments
    parser.add_argument('-o', '--outfile', metavar = "outfile_path", type = str, default = 'transformed_file.txt', help = "output file")
    parser.add_argument('-k', '--key', type = int, default = 1, help = "encryption/decryption key (must be positive) (default = 1)")
    parser.add_argument('-d', '--decrypt', action = 'store_true', default = False, help = 'decrypt the input file')
    parser.add_argument('-a', '--all', action = 'store_true', default = False, help = 'decrypt using all keys [1, 25], save outputs in different files. (useful in case the key is lost or unknown)')
    parser.add_argument('-v', '--verbose', action = 'store_true', default = False, help = 'verbose mode')

    # parse command line arguments
    args = parser.parse_args()
    
    return args

def read_file(file_path):
    """
    Read file_path and return the content as string.
    
    The file must be opened and closed and the function should handle exceptions when they are raised.
    
    args:
        file_path: path to file
        
    returns:
        message: content of file in file_path as a string
    """
    
    with open(file_path, 'r') as f:
        try:
            message = f.read()
        except Exception as exception_object:
            print("Unexpected error:", exception_object)
            return ''
        else:
            return message
            
def write_file(message, file_path):
    """
    Write the message in file_path.
    
    The file must be opened and closed and the function should handle exceptions when they are raised.
    
    args:
        message: string to write in file
        file_path: path to file
        
    returns:
        None
    """
    
    with open(file_path, 'w') as f:
        try:
            f.write(message)
        except Exception as exception_object:
            print("Unexpected error:", exception_object)

def transform(message, key, decrypt):
    """
    Encrypt or decrypt a message using Caesar cipher.
    
    Encryption and decryption is determined by the Boolean value in decrypt. Key determines the number of 
    places a character is shifted. When encrypting, use the positive value of key to shift the characters forward; 
    when decrypting, use the negative key to shift the characters backward. 
    
    The function should maintain characters that are not letters without change; for example, spaces, punctuations, 
    and numbers should not be encrypted or decrypted. Additionally, the case of the letters should be preserved, 
    small letters are transformed to other small letters and capital letters are transformed to capital letters.
    
    Use the function `shift` (provided later) to shift each character in message by the number in key.
    
    args:
        message: string to be encrypted or decrypted
        key: number of places to shift the characters (always positive)
        decrypt: Boolean; when False the message is encrypted,  when True the message is decrypted
        
    returns:
        transformed_message: encrypted (or decrypted) message
        
    examples:
        Encryption
        ==  transform("deal", 1, False) returns:
            "efbm"
        
        ==  transform("deal", 2, False) returns:
            "fgcn"
        
        ==  transform("deal", 30, False) is equivalent to transform(message, 4, False)
            "hiep"
        
        Decryption
        ==  transform("efbm", 1, True) returns:
            "deal"
            
        ==  transform("fgcn", 2, True) returns:
            "deal"
            
        ==  transform("hiep", 30, True) returns:
            "deal"    
        
    """
    
    # when decrypting shift char to left
    if decrypt:
        key = -key
        
    transformed_message = ''
    for c in message:
        if c.isalpha():
            transformed_message = transformed_message + shift(c, key)
        # whitespaces, punctuations...etc.
        else:
            transformed_message = transformed_message + c
    
    return transformed_message
 
def shift(char, key):    
    """
    Shift char by the value in key while maintaining the case (small/capital).
    
    If char contains non-letters (i.e. digits, punctuations, and white spaces), it is ignored.
    
    args:
        char: character to shift
        key: number of places to shift char
        
    returns:
        shifted character
        
    examples:
        shfit('a', 1) ==> 'b'
        shift('z', -1) ==> 'y'
        shift('A', 5) ==> 'F'
        shift('H', 7) ==> 'O'
        shift('o', -10) ==> 'e'
        shift('a', 30) ==> 'e'
    """
    
    # ordered lower case alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # will contain shifted lower case alphabet
    shifted_alphabet = ''
    for i in range(len(alphabet)):
        shifted_alphabet = shifted_alphabet + alphabet[(i + key) % 26]
 
    if char.isalpha():
        char_index = alphabet.index(char.lower())
        shifted_char = shifted_alphabet[char_index]
    
        # keep char's case (upper or lower)
        if char.isupper():
            return shifted_char.upper()
        else:
            return shifted_char

def main():
    # parse command line arguments
    args = parse_command_line()
    
    # read content of infile to a string
    instring = read_file(args.infile)
    
    # verbose
    if args.verbose:
        print("Input file:")
        print("------------")
        print(instring)
        print()
    
    # key is specified
    if not args.all:
        # encrypt/decrypt content of infile
        outstring = transform(instring, args.key, args.decrypt)
    
        # verbose
        if args.verbose:
            print("Output file:")
            print("------------")
            print(outstring)

        # write content of outstring to outfile
        write_file(outstring, args.outfile)
    
    # key is not specified, try all keys from 1 to 25 to decrypt infile
    else:
        for k in range(1, 26):
            # decrypt content of infile
            outstring = transform(instring, k, True)

            # verbose
            if args.verbose:
                print("Key =", k)
                print("------------")
                print(outstring)
                print()

            # write content of outstring to outfile
            write_file(outstring, "decrypted_by_" + str(k) + ".txt")
    
if __name__ == '__main__':
    main()


# ## Terminal commands
# * Display the program's help message
# * Encrypt the text file `plain_message.txt` by key = 23 and save the result in `cipher_message.txt`
# * Find the key used to decrypt `encrypted_message.txt`

# ## Terminal commands

# ### Help message

# In[ ]:


get_ipython().run_cell_magic('bash', '', '\npython3 cipher.py -h')


# ### Encrypt `plain_message.txt` by key = 23

# In[ ]:


get_ipython().run_cell_magic('bash', '', '\npython3 cipher.py plain_message.txt -k 23 -v -o cipher_message.txt')


# ### Finding the key to decrypt `encrypted_message.txt`

# In[ ]:


get_ipython().run_cell_magic('bash', '', '\npython3 cipher.py encrypted_message.txt -a -v')

