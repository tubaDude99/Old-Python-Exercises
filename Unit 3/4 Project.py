#!/usr/bin/env python
# coding: utf-8

# # Module 4 Required code  
#   
# 
# ## Note: Students of Dev330x on edX
# 
# > ### It is required to submit your required code for Module 4 within the edX course   
# > The completed code must be copied from the cell below and pasted in to the edX required code page at the end of Module 4 in the course "Introduction to Python: Creating Scalable, Robust, Interactive Code" on edX.  
# >  
# > **REQUIREMENTS**  
# > Submit all of the code for **cipher.py** in working order but you will only be graded on the the 2 functions below:
# - ### parse_command_line()  
#   - **use the following required keywords & functions:** `argparse.ArgumentParser()`, `.add_argument()`, `.parse_args()`, `return`
# - ### read_file()
#   - **use the following required keywords & functions:** `with open`, `try`, `except`, `return`

# ---
# <font size="6" color="#B24C00"  face="verdana"> <B>Required Code Module 4</B></font>
# 
# ## Caesar Cipher
# 
# 
# 
# In this project, you will implement a program to encrypt and decrypt text using Caesar Cipher. The cipher is one of the oldest and simplest known encryption techniques known. It simply relies on substituting each character in a string by another character which is shifted by a certain number of places. For example, with a shift of 1 'a' becomes 'b', 'e' becomes 'f', and 'z' becomes 'a'. In the Caesar cipher, all characters are shifted by the same number of places and we refer to the shift value as key. 
# 
# To decrypt a message, you simply use the same key, which was used during the encryption procedure, to shift the characters back the same number of places. For example, with a key = 1 'b' becomes 'a', 'f' becomes 'e', and 'a' becomes 'z'. 
# 
# Since there are 26 letters in English, there are only 25 keys available for Caesar cipher. Therefore, it is easy to decipher a message without knowing the key. Simply use all possible keys to decrypt a message then read the outputs till one of them makes sense. This process is also implemented in the project.
# 
# 

# ## Environment Setup
# 
# The following code blocks move the working directory to `command_line` and generate the necessary text file:
# * `plain_message.txt` : contains a plain message that will be encrypted
# * `encrypted_message.txt`: contains an encrypted message where the key is unknown

# ### Change working directory to `command_line`
# 
# Necessary so all generated files are saved in this directory, the cell will generate an error message if you are already in the `command_line` directory.

# In[3]:


get_ipython().run_line_magic('cd', '"/home/nbuser/library/3 Unit 3/command_line"')


# ### Writing text files

# In[4]:


get_ipython().run_cell_magic('writefile', 'plain_message.txt', '\nSoftware is a great combination between artistry and engineering.\n\n--Bill Gates')


# In[5]:


get_ipython().run_cell_magic('writefile', 'encrypted_message.txt', '\nMHI LXVKXM!\n\nMabl fxlltzx ptl xgvkrimxw nlbgz dxr = gbgxmxxg.\n\ntuvwxyzabcdefghijklmnopqrs\n\nTUVWXYZABCDEFGHIJKLMNOPQRS')


# ### Complete the Required Code in the Jupyter Notebook Required_Code_Mod01 and then paste the code for cipher.py into edX code submission page   
# 
# This is the same code assignment located as the project at the bottom of 3-1.5_Mod01_Practice.ipynb  
# 
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


get_ipython().run_cell_magic('writefile', 'cipher.py', '\nimport argparse\n\ndef parse_command_line():\n    """\n    Parse the command line arguments and return the parse_args object.\n    \n    There should be 1 positional argument and 6 optional arguments.\n    The help message generated by the parser should look like:\n    \n    usage: cipher.py [-h] [-o outfile_path] [-k KEY] [-d] [-a] [-v] infile\n\n    positional arguments:\n      infile                input file to be encrypted or decrypted\n\n    optional arguments:\n      -h, --help            show this help message and exit\n      -o outfile_path, --outfile outfile_path\n                            output file\n      -k KEY, --key KEY     encryption/decryption key (must be positive) (default\n                            = 1)\n      -d, --decrypt         decrypt the input file\n      -a, --all             decrypt using all keys [1, 25], save outputs in\n                            different files. (useful in case the key is lost or\n                            unknown)\n      -v, --verbose         verbose mode\n\n\n    args:\n        None\n        \n    returns:\n        args: generated argparse object with all the passed command line arguments      \n    """\n    \n    #TODO: Your code goes here\n    #HINTS: Reveiw Jupyter Notebook 3-4.1\n    pass\n\ndef read_file(file_path):\n    """\n    Read file_path and return the content as string.\n    \n    The file must be opened and closed and the function should handle exceptions when they are raised.\n    \n    args:\n        file_path: path to file\n        \n    returns:\n        message: content of file in file_path as a string\n    """\n    \n    #TODO: Your code goes here\n    pass\n            \ndef write_file(message, file_path):\n    """\n    Write the message in file_path.\n    \n    The file must be opened and closed and the function should handle exceptions when they are raised.\n    \n    args:\n        message: string to write in file\n        file_path: path to file\n        \n    returns:\n        None\n    """\n    \n    #TODO: Your code goes here\n    pass\n\ndef transform(message, key, decrypt):\n    """\n    Encrypt or decrypt a message using Caesar cipher.\n    \n    Encryption and decryption is determined by the Boolean value in decrypt. Key determines the number of \n    places a character is shifted. When encrypting, use the positive value of key to shift the characters forward; \n    when decrypting, use the negative key to shift the characters backward. \n    \n    The function should maintain characters that are not letters without change; for example, spaces, punctuations, \n    and numbers should not be encrypted or decrypted. Additionally, the case of the letters should be preserved, \n    small letters are transformed to other small letters and capital letters are transformed to capital letters.\n    \n    Use the function `shift` (provided later) to shift each character in message by the number in key.\n    \n    args:\n        message: string to be encrypted or decrypted\n        key: number of places to shift the characters (always positive)\n        decrypt: Boolean; when False the message is encrypted,  when True the message is decrypted\n        \n    returns:\n        transformed_message: encrypted (or decrypted) message\n        \n    examples:\n        Encryption\n        ==  transform("deal", 1, False) returns:\n            "efbm"\n        \n        ==  transform("deal", 2, False) returns:\n            "fgcn"\n        \n        ==  transform("deal", 30, False) is equivalent to transform(message, 4, False)\n            "hiep"\n        \n        Decryption\n        ==  transform("efbm", 1, True) returns:\n            "deal"\n            \n        ==  transform("fgcn", 2, True) returns:\n            "deal"\n            \n        ==  transform("hiep", 30, True) returns:\n            "deal"    \n        \n    """\n    \n    #TODO: Your code goes here\n    pass\n \ndef shift(char, key):    \n    """\n    Shift char by the value in key while maintaining the case (small/capital).\n    \n    If char contains non-letters (i.e. digits, punctuations, and white spaces), it is ignored.\n    \n    args:\n        char: character to shift\n        key: number of places to shift char\n        \n    returns:\n        shifted character\n        \n    examples:\n        shfit(\'a\', 1) ==> \'b\'\n        shift(\'z\', -1) ==> \'y\'\n        shift(\'A\', 5) ==> \'F\'\n        shift(\'H\', 7) ==> \'O\'\n        shift(\'o\', -10) ==> \'e\'\n        shift(\'a\', 30) ==> \'e\'\n    """\n    \n    # ordered lower case alphabet\n    alphabet = "abcdefghijklmnopqrstuvwxyz"\n    \n    # will contain shifted lower case alphabet\n    shifted_alphabet = \'\'\n    for i in range(len(alphabet)):\n        shifted_alphabet = shifted_alphabet + alphabet[(i + key) % 26]\n \n    if char.isalpha():\n        char_index = alphabet.index(char.lower())\n        shifted_char = shifted_alphabet[char_index]\n    \n        # keep char\'s case (upper or lower)\n        if char.isupper():\n            return shifted_char.upper()\n        else:\n            return shifted_char\n\ndef main():\n    # parse command line arguments\n    args = parse_command_line()\n    \n    # read content of infile to a string\n    instring = read_file(args.infile)\n    \n    # verbose\n    if args.verbose:\n        print("Input file:")\n        print("------------")\n        print(instring)\n        print()\n    \n    # key is specified\n    if not args.all:\n        # encrypt/decrypt content of infile\n        outstring = transform(instring, args.key, args.decrypt)\n    \n        # verbose\n        if args.verbose:\n            print("Output file:")\n            print("------------")\n            print(outstring)\n\n        # write content of outstring to outfile\n        write_file(outstring, args.outfile)\n    \n    # key is not specified, try all keys from 1 to 25 to decrypt infile\n    else:\n        for k in range(1, 26):\n            # decrypt content of infile\n            outstring = transform(instring, k, True)\n\n            # verbose\n            if args.verbose:\n                print("Key =", k)\n                print("------------")\n                print(outstring)\n                print()\n\n            # write content of outstring to outfile\n            write_file(outstring, "decrypted_by_" + str(k) + ".txt")\n    \nif __name__ == \'__main__\':\n    main()')


# In[ ]:


# --Completed--  
# remove the comments above the %% line 
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
