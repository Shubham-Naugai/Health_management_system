# for loop
# program to find the sum of all number stored in a list

numbers = [3, 5, 7, 9, 11, 13]   # list of numbers
total = 0         # variable to store total sum of the numbers
for x in numbers:
    total = total + x
print('the total sum of number is = ', total)   # here print statement is not consider as a statement of loop body
# so this print statement will execute one time after completing the loop
print()

numbers = [3, 5, 7, 9, 11, 13]   # list of numbers
total = 0         # variable to store total sum of the numbers
for x in numbers:
    total = total + x
    print('the total sum of number is = ', total)
# by putting space in 16th print statement, it is consider inside loop
# it means the number of times the loop execute then the print statement will also execute
# it means in output it will show each total(sum)
