# star pattern
n = int(input('n = '))
for i in range(n):             # i is responsible for print the rows
    for j in range(i+1):       # j is responsible for print the column
        print("* ", end='')
    print()
print()
# invert star pattern
# n = int(input('n = '))
for i in range(n):             # i is responsible for print the rows
    for j in range(n-i):       # j is responsible for print the column
        print("* ", end='')
    print()
