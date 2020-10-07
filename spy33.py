# factorial of a number
# using iterative approach
# n! = n * (n-1) * (n-2) *...* 1
def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
number = int(input('enter the number'))
print('factorial using iterative method ', factorial_iterative(number))

print()
# using recursion
# n! = n * (n-1)!
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
# number = int(input('enter the number'))
print('factorial using recursion ', factorial_recursive(number))
