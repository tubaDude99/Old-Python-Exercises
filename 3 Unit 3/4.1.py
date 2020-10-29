#!/usr/bin/env python
# coding: utf-8

# # Section 4.1: Script Environment & Command-Line Arguments
# * \_\_name\_\_ == "\_\_main\_\_"
# * sys.argv, import argparse, argparse.ArgumentParser, argparse.parse_args
# * argparse.add_argument: action, nargs, default, type, choices, metavar, help
# 
# ### Students will be able to:
# * Determine whether Python code is running as a script or being imported as a module
# * Recognize the basic structure of a UNIX command line
# * Parse command-line arguments:
#     * Use the add_argument() method to parse command-line arguments
#     * Add positional arguments
#     * Add optional arguments
#     * Utilize the parameters of add_argument() to control how it works
# * Employ parsed command-line arguments in practical applications

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# ## Using the Terminal in Notebooks.Azure.com     
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/5730bbd7-9042-4a47-a0fe-e930bd335e4e/DEV330x-4_1_jupiter_terminal - u.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/4c7643bb-4cfd-49b2-a2eb-718cbbe0bbf0/DEV330x-4_1_jupiter_terminal.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# - Launch the Terminal from the Library page   
# - Identify the Shell **`$ echo $0`**  
# - Print the Working Directory **`$ pwd`**  
# - List the Directory **`$ ls`**  or **`$ dir`** 
# - Clear the Terminal Display **`$ clear`**
# - Change the Directory **`$ cd [directory path]`**  or **`>cd ..`**    
# - Run a Python file **`$ python3 [file_path]`** 
# - Run Python in Terminal **`$ python3 `** and exit Python **`$>>>exit()`**  

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Script Environment
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7c441dd5-7e0d-444e-8b44-45e95aa9de0a/DEV330x-4_1a_script_environment.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c0a1dcbb-36fa-435b-9867-d82e88ce46ab/DEV330x-4_1a_script_environment.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# A Python script can be executed directly or imported as a module in another script. When running a script, a Python interpreter goes through a special setup procedure that defines some environment variables. One of those variables is the `__name__` variable, which can distinguish between the two cases. When the script is executed directly, `__name__` contains the string `"__main__"`; otherwise, it contains the name of the module. This distinction allows you to run parts of the code when the script is run directly, and run other parts when the script is imported as a module.
# 
# ### Running a script directly
# 
# If a script (`main_script.py`) contains the following code: 
# ```python
# print(__name__)
# ```
# 
# Running the script from a terminal window, will give you:
# 
# ```bash
# $ python main_script.py 
# __main__
# ```
# 
# ### Importing the script as a module
# 
# If the script (`main_script.py`) containing:
# 
# ```python
# print(__name__)
# ```
# 
# Is imported into another script (`secondary_script.py`) that contains the following code:
# ```python
# import main_script
# ```
# 
# Running (`secondary_script.py`) will give you the name of the imported module (which is the name of the `main_script.py` file in this case)
# ```bash
# $ python secondary_script.py 
# main_script
# ```
# 
# ### `main()` function
# Generally, you test the value of `__name__` and execute a (`main()`) function if you are running the script directly. Otherwise, you do not run any function.
# 
# ```python
# if __name__ == "__main__":
#     main()
# ```

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 
# ## Script Environment
# 
# In the following example, `main_script.py` is run directly then imported as a module into `secondary_script.py`. You will see the content of `__name__` will change how the `main_script.py` code is executed.

# ### Changing the working directory to `command_line`
# 
# Necessary so all generated files are saved in this directory, the cell will generate an error message if you are already in the `command_line` directory.

# In[10]:


get_ipython().run_line_magic('cd', 'command_line')


# ### Saving the primary script as `main_script.py`
# 
# The first line saves the Python code in the cell as `main_script.py` in the current working directory.

# In[11]:


get_ipython().run_cell_magic('writefile', 'main_script.py', '\n# Start of Python code\n\n# Will be called from another script\ndef func():\n    print("Running func")\n\n# Execute when running the script directly\ndef main():\n    print("Running the main function")\n\nif __name__ == "__main__":\n    main()\n    ')


# ### Running the primary script directly
# 
# The first line is necessary to run the rest of the lines as command lines (more on that later). For now, `main_script.py` is being run directly.

# In[12]:


get_ipython().run_cell_magic('bash', '', '\npython3 main_script.py')


# ### Saving the secondary script as `secondary_script.py`
# 
# The first line saves the Python code in the cell as `secondary_script.py` in the current working directory.
# 
# The secondary script imports the primary script as a module and calls its `func()` function.

# In[13]:


get_ipython().run_cell_magic('writefile', 'secondary_script.py', '\n# Start of Python code\nimport main_script\n\n# call func() from the main script\nmain_script.func()')


# ### Running the secondary script directly
# 
# The first line is necessary to run the rest of the lines as command lines (more on that later). For now, `secondary_script.py` is being run directly.

# In[14]:


get_ipython().run_cell_magic('bash', '', '\npython3 secondary_script.py')


# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Script Environment

# In[15]:


# [ ] The following program asks the user for a circle radius then display the area and circumference
# Modify the program so it only displays the information when executed directly
# The program should not display anything if it is imported as a module 

from math import pi

def circle_area(r):
    return pi * (r ** 2)

def circle_circumference(r):
    return 2 * pi * r

radius = float(input("Enter radius: "))
print("Area =", circle_area(radius))
print("Circumference =", circle_circumference(radius))

# --Completed--

from math import pi

def circle_area(r):
    return pi * (r ** 2)

def circle_circumference(r):
    return 2 * pi * r

def main():
    radius = float(input("Enter radius: "))
    print("Area =", circle_area(radius))
    print("Circumference =", circle_circumference(radius))


if (__name__ == '__main__'):
    main()


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Command-Line Structure
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/671fa4e2-5ccb-4113-aba7-800722295a47/DEV330x-4_1b_command_line_struct.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/fe1f9d76-1343-415a-b227-de33387532af/DEV330x-4_1b_command_line_structure.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# A UNIX command is used to run a program and it has the following syntax: (`command [arguments] [options]`). The arguments and options might be optional depending on the nature and purpose of the program. In the following examples you will go through a very concise UNIX command-line primer that will help you complete the lesson. 

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 

# ## Command-Line Structure
# 
# ### Changing the working directory to `command_line`
# 
# Necessary so all generated files are saved in this directory, the cell will generate an error message if you are already in the `command_line` directory.

# In[16]:


get_ipython().run_line_magic('cd', 'command_line')


# ### `ls`
# This command lists the content of a directory. 
# 
# The command `ls` can be run without options or arguments to display the content of the current working directory.

# In[17]:


get_ipython().run_cell_magic('bash', '', '\nls')


# ### `ls` options
# One or more options can be used with `ls`; options usually start with `-`.
# 
# The `-l` option show more detailed description about the content of the current working directory.

# In[18]:


get_ipython().run_cell_magic('bash', '', '\nls -l')


# The `-a` option displays hidden files and directories. Note the `.` and `..` directories.

# In[19]:


get_ipython().run_cell_magic('bash', '', '\nls -l -a')


# ### `ls` arguments
# `ls` can take arguments; for example, you can pass it a path to a directory to display its content. You can also use the options along with the arguments.

# In[20]:


get_ipython().run_cell_magic('bash', '', '\nls -l ../parent_dir')


# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# 
# 
# ## Parsing Command-Line Arguments
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)](http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ad78170a-b61b-4730-9be3-652a234f69b0/DEV330x-4_1c_parsing_command_lin.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ea275099-0059-4a12-937a-e2dce3249449/DEV330x-4_1c_parsing_command_line_arguments.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# Like any other program, Python scripts can be executed from a terminal. They can also be executed with command-line arguments and options. These arguments and options can be used within the script to control the flow of the program. The arguments and options are captured by an environment variable `argv`, which can be accessed using the `sys` module.
# 
# The `argv` variable captures the command-line arguments and options as a list. The first element `argv[0]` is always the command itself, which is the name of the script file. The rest of the list elements are the arguments and options. It is possible to process these arguments and options by writing code around the `argv` list; however, it is a daunting and tedious task. Command-line arguments are used by many applications; therefore, the Python standard library provides an `argparse` module that is much more robust and versatile and will make parsing command-line arguments very easy.
# 
# You will explore how to use the `argparse` module in the following examples, where you will develop a script `rand.py` that will generate random integers according to the arguments and options passed from the command line.

# ---
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# 

# ## Parsing Command-Line Arguments
# 
# ### Changing the working directory to `command_line`
# 
# Necessary so all generated files are saved in this directory, the cell will generate an error message if you are already in the `command_line` directory.

# In[21]:


get_ipython().run_line_magic('cd', 'command_line')


# ### Using the `argv` environment variable

# In[22]:


get_ipython().run_cell_magic('writefile', 'command_line.py', '\nimport sys\n\n# Number of arguments\nargc = len(sys.argv)\nprint(argc, "arguments and options were passed")\n\n# List of arguments and options\nprint("The arguments and options passed are: ")\nfor i in range(argc):\n    print("argv[{:d}] = {}".format(i, sys.argv[i])) ')


# Running the `command_line.py` script will generate:
# 

# In[23]:


get_ipython().run_cell_magic('bash', '', '\npython3 command_line.py arg1 arg2 -option1 -option2')


# ## Generating random numbers
# 
# In the following examples, you will build a program `rand.py` to:
# * Print a random integer between 0 and 10
# * Print a number of random integers between 0 and 10, with the number of integers passed as a command-line argument
# * Print a number of random integers in a specific range, with the number of integers and range limits passed as command-line arguments
# * Print a number of random integers in a specific range with an optional message; the number of integers, range limits, and  message option are all passed as command-line arguments
# 
# NOTE: In the following examples, the `bash` executions must be run after the code segments that precede them. Changing the order will result in errors and undesired output.

# ### `argparse` module
# 
# _Print a random integer between 0 and 10_ 
# 
# This program imports the `argparse` module to define an object of type `argparse.ArgumentParser`, then parses the command line arguments using `parse_args()`.

# In[24]:


get_ipython().run_cell_magic('writefile', 'rand.py', '\nimport argparse\nfrom random import randint\n\n# Define an argument parser object\nparser = argparse.ArgumentParser()\n\n# Parse command-line arguments\nargs = parser.parse_args()\n\n# Program\nprint(randint(0, 10))')


# Running the script from a terminal will generate:
# 

# In[25]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py')


# The program prints a random number between 0 and 10 as expected. However, if we pass an unrecognized argument to the script, the `argparse` module will generate an appropriate usage message and automatically build a help page. 

# In[26]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py -i')


# In[27]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py -h')

### Adding arguments (`add_argument`)

_Print a number of random integers between 0 and 10, with the number of integers passed as a command-line argument_

This program adds a `count` argument using the `add_argument` method. The `count` argument holds the number of random integers to print.

* If `count` is not provided by the user, the script won't work and the user will be presented with a usage message
* The help is updated accordingly
* The argument passed is stored in `args.count`
* When passing 4 as an argument, the script generates 4 random numbers as expected
* The `add_argument` method takes several parameters:
    * Name of the argument, which is also the name of the variable storing the count.
    * Type of the argument; if not specified, the default is string
    * Message to be displayed when a user requests the help message by using the `-h` option
* The `add_argument` method takes more optional parameters depending on the way you want to capture the arguments. We will explore a few more in the next examples.
# In[28]:


get_ipython().run_cell_magic('writefile', 'rand.py', "\nimport argparse\nfrom random import randint\n\n# Define an argument parser object\nparser = argparse.ArgumentParser()\n\n# Add positional arguments\nparser.add_argument('count', type = int, help = 'Count of random integers to be generated')\n\n# Parse command-line arguments\nargs = parser.parse_args()\n\n# Program\nfor i in range(args.count):\n    print(randint(0, 10))")


# Running the script from a terminal will generate:
# 

# In[29]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py')


# In[30]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py -h')


# In[31]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py 4')


# ### Adding `add_argument` parameters
# 
# _Print a number of random integers in a specific range, with the number of integers and range limits passed as command-line arguments_
# 
# The argument (`count`) is a positional argument because it is required and its position depends on the command itself. In the following example, we add an optional argument to let the user decide the range from which the random integers will be chosen.
# 
# * '-r' is the short notation of the new argument; '--range' is the long notation. You can use them interchangeably.
# * `metavar` is the name that will be used in the help message.
# * `nargs` is the number of expected options after `-r` or `--range`; use `'*'` for unlimited. In this example, it will be 2, the lower and upper integer range limits.
# * `type` is the expected type (string by default).
# * `default` is the default range when not specifying a range.
# * You can access the range options using `args.range[0]` and `args.range[1]`. If `nargs` was larger you could use the appropriate index to access the numbers passed.

# In[32]:


get_ipython().run_cell_magic('writefile', 'rand.py', "\nimport argparse\nfrom random import randint\n\n# Define an argument parser object\nparser = argparse.ArgumentParser()\n\n# Add positional arguments\nparser.add_argument('count', type = int, help = 'Count of random integers to be generated')\n\n# Add optional arguments\nparser.add_argument('-r', '--range', metavar = 'number', nargs = 2, type = int, default = [0, 10], help = 'Integer range [a, b] from which the random numbers will be chosen')\n\n# Parse command-line arguments\nargs = parser.parse_args()\n\n# Program\nfor i in range(args.count):\n    print(randint(args.range[0], args.range[1]))")


# Running the script from a terminal will generate:
# 

# In[33]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py 4')


# In[34]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py 4 -r 500 1000')


# In[35]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py 4 --range 500 1000')


# In[36]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py 10 -r 500 1000')


# In[37]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py')


# In[38]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py -h')


# #### More about `metavar`
# 
# In the previous example, the number of expected arguments after `-r` (or `--range`) was `nargs = 2`. The help message illustrated that by `-r number number` (or `--range number number`). The word `number` was specified using the `metavar` parameter. The `metavar` was repeated 2 times to account for the 2 required arguments. It is also possible to specify different names for each of the required arguments by putting them in a tuple. In this example, the numbers passed to `-r` are renamed to `lower` and `upper` by assigning a tuple to `metavar`.

# In[39]:


get_ipython().run_cell_magic('writefile', 'rand.py', "\nimport argparse\nfrom random import randint\n\n# define an argument parser object\nparser = argparse.ArgumentParser()\n\n# Add positional arguments\nparser.add_argument('count', type = int, help = 'Count of random integers to be generated')\n\n# Add optional arguments\nparser.add_argument('-r', '--range', metavar = ('lower', 'upper'), nargs = 2, type = int, default = [0, 10], help = 'Integer range [a, b] from which the random numbers will be chosen')\n\n# parse command line arguments\nargs = parser.parse_args()\n\n# program\nfor i in range(args.count):\n    print(randint(args.range[0], args.range[1]))")


# In[40]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py -h')


# The `metavar` parameter can also be used with positional arguments to use an alternative name in the help message. However, only the displayed name is changed; the parse_args() attribute still has the original name. In this example, you will see how the `count` argument name is changed in the help message using `metavar`.

# In[41]:


get_ipython().run_cell_magic('writefile', 'rand.py', "\nimport argparse\nfrom random import randint\n\n# Define an argument parser object\nparser = argparse.ArgumentParser()\n\n# Add positional arguments\nparser.add_argument('count', metavar = 'rands', type = int, help = 'Count of random integers to be generated')\n\n# Add optional arguments\nparser.add_argument('-r', '--range', metavar = ('lower', 'upper'), nargs = 2, type = int, default = [0, 10], help = 'Integer range [a, b] from which the random numbers will be chosen')\n\n# Parse command-line arguments\nargs = parser.parse_args()\n\n# Program\nfor i in range(args.count): # still accessed as args.count (not args.rands)\n    print(randint(args.range[0], args.range[1]))")


# In[42]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py -h')


# ### More `add_argument` parameters
# 
# _Print a number of random integers in a specific range with an optional message; the number of integers, range limits, and  message option are all passed as command-line arguments_
# 
# The following program updates the `rand.py` script so that it includes an optional `verbose` flag. When selected, the `verbose` flag will print out general messages about the currently selected options and arguments.
# 
# * Because the value of `--verbose` should be `True` or `False`, the `action = 'store_true'` was used.
# * You can access `verbose` as `args.verbose`.
# * The rest of the argument is almost the same as for `--range` (or `-r`) argument.

# In[43]:


get_ipython().run_cell_magic('writefile', 'rand.py', '\nimport argparse\nfrom random import randint\n\n# Define an argument parser object\nparser = argparse.ArgumentParser()\n\n# Add positional arguments\nparser.add_argument(\'count\', type = int, help = \'Count of random integers to be generated\')\n\n# Add optional arguments\nparser.add_argument(\'-r\', \'--range\', metavar = (\'lower\', \'upper\'), nargs = 2, type = int, default = [0, 10], help = \'Integer range [a, b] from which the random numbers will be chosen\')\n\nparser.add_argument(\'-v\', \'--verbose\', action = \'store_true\', help = \'Verbose mode\')\n\n# Parse command-line arguments\nargs = parser.parse_args()\n\n# Program\nif args.verbose:\n    print("Generating {:d} random integer in the range [{:d}, {:d}]".format(args.count, args.range[0], args.range[1]))\n            \nfor i in range(args.count):\n    print(randint(args.range[0], args.range[1]))')


# In[46]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py 4 --range 500 1000 -v')


# In[47]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py -h')


# #### More about `action`
# 
# In the previous example, the `action = 'store_true'` was used to make `-v` (or `--verbose`) a Boolean flag that can be set to True or False. Python supports other actions:
# * `store`: The default action for all arguments; it stores the value passed on the command line to the argument.
# * `store_true` and `store_false`: Make an argument a Boolean flag and set it to True or False when entered by the user.
# * `store_const`: Stores a value specified by the keyword `const` in the argument. This is a more general form of `store_true` that allows you to store non-Boolean values in the argument.
# * `count`: The number of times an argument is used by the user.
# 
# The following example shows how these actions behave.

# In[48]:


get_ipython().run_cell_magic('writefile', 'rand.py', '\nimport argparse\nfrom random import randint\n\n# Define an argument parser object\nparser = argparse.ArgumentParser()\n\n# Add positional arguments\nparser.add_argument(\'count\', action = \'store\', type = int, help = \'Count of random integers to be generated\')\n\n# Add optional arguments\nparser.add_argument(\'-r\', \'--range\', metavar = (\'lower\', \'upper\'), nargs = 2, type = int, default = [0, 10], help = \'Integer range [a, b] from which the random numbers will be chosen\')\n\nparser.add_argument(\'-c\', \'--const\', action = \'store_const\', const = 10, default = 0, help = \'Generate 10 additional random numbers (in addition to Count)\')\n\nparser.add_argument(\'-m\', \'--multiply\', action = \'count\', help = \'Multiply the number of random numbers by the number of times this flag appears\')\n\nparser.add_argument(\'-v\', \'--verbose\', action = \'store_true\', help = \'Verbose mode\')\n\n# Parse command-line arguments\nargs = parser.parse_args()\n\n# Program\n\n# If args.const is used, add 10 to the count entered by the user\nnum_of_rands = (args.count + args.const)\n\n# When args.multiply is not used, its value is None\nif (args.multiply != None):\n    num_of_rands = num_of_rands * args.multiply\n\nif args.verbose:\n    print("Generating {:d} random integer in the range [{:d}, {:d}]".format(num_of_rands, args.range[0], args.range[1]))\n            \nfor i in range(num_of_rands):\n    print(randint(args.range[0], args.range[1]))')


# In[49]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py 4 --range 500 1000 -v -c')


# In[50]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py 4 --range 500 1000 -v -mmm')


# In[51]:


get_ipython().run_cell_magic('bash', '', '\npython3 rand.py -h')


# NOTE: More information about the parameters and capabilities of the `add_argument` method is available on the Python Documentation site at https://docs.python.org/3/library/argparse.html.

# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Parsing Command-Line Arguments
# 

# ### Finding the day of the week

# In[52]:


get_ipython().run_cell_magic('writefile', 'day_finder.py', '\n# [ ] Write a program that reads a date (month, day, year) as command-line arguments in order\n# then prints the day of the week for that date.\n# If an optional flag (-c or --complete) is specified, the program should print the full date (not only the day of the week).\n\n# The help message should look like:\n\'\'\'\nusage: day_finder.py [-h] [-c] month day year\n\npositional arguments:\n  month           Month as a number (1, 12)\n  day             Day as a number (1, 31) depending on the month\n  year            Year as a 4 digits number (2018)\n\noptional arguments:\n  -h, --help      show this help message and exit\n  -c, --complete  Show complete formatted date\n\'\'\'\n\n# HINT: Use a date object with strftime\n\n\n# --Completed--\n\nimport argparse\nfrom datetime import date\n\n# Define an argument parser object\nparser = argparse.ArgumentParser()\n\n# Add positional arguments\nparser.add_argument(\'month\', type = int, help = \'Month as a number (1, 12)\')\nparser.add_argument(\'day\', type = int, help = \'Day as a number (1, 31) depending on the month\')\nparser.add_argument(\'year\', type = int, help = \'Year as a 4 digits number (2018)\')\n\n# Add optional arguments\nparser.add_argument(\'-c\', \'--complete\', action = \'store_true\', help = \'Show complete formatted date\')\n\n# Parse command-line arguments\nargs = parser.parse_args()\n\n# Program\ntry:\n    d = date(month = args.month, day = args.day, year = args.year)\nexcept Exception as exception_object:\n    print(exception_object)\nelse:\n    if args.complete:\n        print(d.strftime("%A %B %d, %Y"))\n    else:\n        print(d.strftime("%A"))')


# In[53]:


get_ipython().run_cell_magic('bash', '', '\npython3 day_finder.py 12 31 2017 -c')


# In[54]:


get_ipython().run_cell_magic('bash', '', '\npython3 day_finder.py 12 31 2017')


# ### Sorting numbers

# In[55]:


get_ipython().run_cell_magic('writefile', 'sort_numbers.py', '\n# [ ] Write a program that reads an unspecified number of integers from the command line,\n# then prints out the numbers in an ascending order\n# The program should have an optional argument to save the sorted numbers as a file named `sorted_numbers.txt`\n\n# The help message should look like:\n\'\'\'\nusage: sort_numbers.py [-h] [-s] [numbers [numbers ...]]\n\npositional arguments:\n  numbers     int to be sorted\n\noptional arguments:\n  -h, --help  show this help message and exit\n  -s, --save  save the sorted numbers on a file (sorted_numbers.txt)\n\'\'\'\n\n#HINT: use nargs = \'*\' in an add_argument method\n\n# --Completed--\n\nimport argparse\nfrom datetime import date\n\n# Define an argument parser object\nparser = argparse.ArgumentParser()\n\n# Add positional arguments\nparser.add_argument(\'numbers\', type = int, metavar = \'numbers\', nargs = \'*\', help = "int to be sorted")\n\n# Add optional arguments\nparser.add_argument(\'-s\', \'--save\', action = \'store_true\', help = \'save the sorted numbers on a file (sorted_numbers.txt)\')\n\n# Parse command-line arguments\nargs = parser.parse_args()\n\n# Program\nsorted_list = sorted(args.numbers)\nprint(sorted_list)\n\nif args.save:\n    with open(\'sorted_numbers.txt\', \'w\') as f:\n        f.write(str(sorted_list))')


# In[56]:


get_ipython().run_cell_magic('bash', '', '\npython3 sort_numbers.py 23 49 5 300 43 582 58 29 62 69 320 60')

