# hollow right triangle star pattern
n = int(input('n='))
for i in range(1, n):
    for j in range(1, n):
        if j == 1 or j == i:
            print('* ', end='')
        elif i == n-1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
