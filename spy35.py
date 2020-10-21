# practice question based on functions
# 1.Maximum of three numbers
a = int(input())
b = int(input())
c = int(input())
def max_of_two(x, y):
    if x > y:
        return x
    return y
def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))
print(max_of_three(a, b, c))

print()
# 2.reverse the string
def string_reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 = rstr1 + str1[index - 1]
        index = index - 1
    return rstr1
print(string_reverse('1 2 3 4 a b c d'))
