# lambda function or anonymous function
# 1 example
addition = lambda x, y: x + y
# def additon(x, y):
#     return x + y
print(addition(9, 4))

print()
# 1 example
def my_func(n):
    return lambda a: a * n
my_double = my_func(2)
print(my_double(11), end='')
