# Level 2 question on if/else
# 1. Write a program to check if a year is leap year or not.

year = int(input('enter the year: '))
year_check1 = year % 4       # fro non century years
year_check2 = year % 400     # for century  years like 2000, 2200, 2300

if year_check1 == 0:
    print('the year is leap year')
elif year_check2 == 0:
    print('the year is leap year')
else:
    print('the year is not a leap year')
