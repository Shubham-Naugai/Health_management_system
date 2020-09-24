# break statement in for loop
# With the break statement we can stop the loop before it has looped through all the items:

fruits = ['apple', 'banana', 'cherry', 'guava', 'grapes']
for x in fruits:
    print(x)
    if x == 'cherry':
        break

# here loop break when x = cherry but loop will print the items before cherry
fruits = ['apple', 'banana', 'cherry', 'guava', 'grapes']
for x in fruits:
    if x == 'cherry':
        print(x)
        break
