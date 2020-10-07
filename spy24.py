# upper right side right angle triangle (1 method).
row = int(input('enter number of rows = '))
for i in range(row):
    for j in range(row+1):
        if j >= row - i:
            print(' *', end='')
        else:
            print('  ', end='')
    print()

# upper right side right angle triangle (2 method)
def star(row):
    k = 2 * row - 2                   # number of spaces
    for i in range(0, row):           # outer loop to handle number of rows
        for j in range(0, k):         # inner loop to handle number spaces
            print(end=" ")
        k = k - 2                     # decrementing k after each loop
        for j in range(0, i + 1):     # inner loop to handle number of columns
            print("* ", end="")       # printing stars
        print()
    # Driver Code
row
star(row)
