
# [ ] Write a program that reads an unspecified number of integers from the command line,
# then prints out the numbers in an ascending order
# The program should have an optional argument to save the sorted numbers as a file named `sorted_numbers.txt`

# The help message should look like:
'''
usage: sort_numbers.py [-h] [-s] [numbers [numbers ...]]

positional arguments:
  numbers     int to be sorted

optional arguments:
  -h, --help  show this help message and exit
  -s, --save  save the sorted numbers on a file (sorted_numbers.txt)
'''

#HINT: use nargs = '*' in an add_argument method

# --Completed--

import argparse
from datetime import date

# Define an argument parser object
parser = argparse.ArgumentParser()

# Add positional arguments
parser.add_argument('numbers', type = int, metavar = 'numbers', nargs = '*', help = "int to be sorted")

# Add optional arguments
parser.add_argument('-s', '--save', action = 'store_true', help = 'save the sorted numbers on a file (sorted_numbers.txt)')

# Parse command-line arguments
args = parser.parse_args()

# Program
sorted_list = sorted(args.numbers)
print(sorted_list)

if args.save:
    with open('sorted_numbers.txt', 'w') as f:
        f.write(str(sorted_list))