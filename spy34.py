# fibonacci series
# 0 1 1 2 3 5 8 13 21 . . .
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)    # n-1 is index
number = int(input('enter the number'))
print('fibonacci series', fibonacci(number))
