# output format to make output look better
x = 5
y = 10
print('The value of x is {} and y is {}'.format(x,y))
print(end='\n')
print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))
print(end='\n')
print('Hello {name}, {greeting}'.format(greeting='Good morning', name='shubham naugai'))
print(end='\n')
z = 12.3456789
print('The value of z is %1.2f' %z)
print('The value of z is %1.4f' %z)

print(end='\n')
num = input('Enter a number: ')
print('num = ', num, end='')


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference between "is" and "==": this comparison returns True because x is equal to y
