# upper equilateral triangle.
row = int(input('enter odd number of rows = '))
for i in range(1, row):
    for j in range(1, row+row-1):
        if j >= row-i and j <= row-2+i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()
# lower equilateral triangle
for i in range(1, row):
    for j in range(1, row+row-2):
        if j >= i and j <= row+row-2-i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
