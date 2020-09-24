# upper right triangle with its vertical mirror image star pattern
n = int(input('n'))
for i in range(1, n):
    for j in range(1, n+n-2):
        if j <= i or j >= n+n-2-i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()
# lower right triangle with its vertical mirror image star pattern
for i in range(1, n):
    for j in range(1, n+n-2):
        if j <= n-i or j >= n-2+i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

