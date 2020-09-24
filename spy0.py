print("HELLO! WORLD", end='\n')
# print('shubham 's laptop') --> SyntaxError: invalid syntax
print("shubham 's laptop")
# print("shubham "laptop" ") --> SyntaxError: invalid syntax
print('shubham "laptop" ')
# print("shubham 's "laptop" ") --> SyntaxError: invalid syntax
print("shubham\'s \"laptop\" ")
# print('shubham 's "laptop" ') --> SyntaxError: invalid syntax
print('shubham\'s "laptop" ')
print(end='\n')    # we can also use print() only
# type casting
a = 23
print(type(a))
a = float(a)
print(type(a))
print(end='\n')
# putting the characters btw numbers
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='  ', end='\n')
print(end='\n')
