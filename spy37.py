# python array/list
# looping an array
cars = ['tata', 'bmw', 'benz', 'honda']
for x in cars:
    print(x)
print()
# replacing element
cars[0] = 'wagon R'
print(cars)
print()
# append() --> adding element to an array
cars.append("wagon R")
print(cars)
print()
# pop() or remove() --> removing an element from array
cars.pop(4)
cars.remove('bmw')
print(cars)
print()
# removing all elements from an array
cars.clear()
print(cars)
# copy() --> returns the copy of the list
cars = ['tata', 'bmw', 'benz', 'honda']
x = cars.copy()       # here we gives a copy of list. So change in x cannot make change in original list
print(x)
x[0] = 'wagon R'
print(cars)
cars[0] = 'wagon R'
print(cars)
print()
cars = ['tata', 'bmw', 'benz', 'honda']
x = cars               # here we give the original list. So change in x can make change in original list
print(x)
x[0] = 'wagon R'
print(cars)
cars[0] = 'wagon R'
print(cars)
