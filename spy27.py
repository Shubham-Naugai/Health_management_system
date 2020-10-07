# diamond star pattern.
row = int(input('enter the number of rows = '))
for i in range(1, row):
    for j in range(1, row*2-2):
        if j >= row-i and j <= row-2+i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
for i in range(2, row):
    for j in range(1, row*2 - 2):
        if j >= i and j <= row*2 - 2 - i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
