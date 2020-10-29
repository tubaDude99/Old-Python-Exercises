
# [ ] Write a program that reads a date from the command line as numbers (month  then day then year),
# if the date entered is in the past, a message saying "The date has passed" should be printed
# if the date is in the future the program should display the number of days remaining from today till that date,
# there should be an optional command line flag that displays the results in total number of seconds instead of days

# help message should look like:
'''
usage: day_counter.py [-h] [-s] month day year

positional arguments:
  month                Month as a number (1, 12)
  day                  Day as a number (1, 31) depending on the month
  year                 Year as a 4 digits number (2018)

optional arguments:
  -h, --help           show this help message and exit
  -s, --total_seconds  Show the time difference in total number of seconds
'''
import argparse
from datetime import datetime
p = argparse.ArgumentParser()
p.add_argument('month', type = int, help = 'Month as a number (1, 12)')
p.add_argument('day', type = int, help = 'Day as a number (1, 31) depending on the month')
p.add_argument('year', type = int, help = 'Year as a 4 digits number (2018)')
p.add_argument('-s', '--total_seconds', action = 'store_true', help = 'Show the time difference in total number of seconds')
args = p.parse_args()
try:
    inpD = datetime(month = args.month, day = args.day, year = args.year)
except:
    pass
td = datetime.today()
if inpD < td:
    print('The date has passed')
elif inpD > td:
    print('You\'re %s days too early' %str((inpD - td).days))
    if args.total_seconds:
        print('That is %s seconds' %str((inpD-td).total_seconds()))