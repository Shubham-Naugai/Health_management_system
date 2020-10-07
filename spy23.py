# star pattern.
# n = int(input('n = '))
n = 5
for i in range(n):             # i is responsible for print the rows
    for j in range(i+1):       # j is responsible for print the column
        print('* ', end='')
    print()

print()
n = 5
for i in range(n):             # i is responsible for print the rows
    for j in range(5-i):       # j is responsible for print the column
        print("* ", end='')
    print()
print()
# number pattern
n = 5
for i in range(n):             # i is responsible for print the rows
    number = 1
    for j in range(i+1):       # j is responsible for print the column
        # print(j, ' ', end='')
        print(number, ' ', end='')
        # j = j + 1
        number = number +1
    print()
