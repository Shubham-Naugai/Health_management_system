# while loop
# 1. print the sum of natural numbers up to n

n = int(input('enter the number = '))
add = 0
i = 1
while i <= n:
    add = add +i
    i = i + 1
print('total sum of {} natural numbers is: {}'.format(n, add))


# Example to illustrate
# the use of else statement with the while loop
counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
