# upper hollow right triangle star pattern.
n = int(input('n = '))
for i in range(1, n):
    for j in range(1, n):
        if j == n-1 or j == n-i:
            print('* ', end='')
        elif i == n-1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()

# lower hollow right triangle star pattern
for i in range(1, n):
    for j in range(1, n):
        if i == 1:
            print('* ', end='')
        elif j == i or j == n-1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
