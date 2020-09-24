# continue statement in for loop

fruits = ['apple', 'banana', 'cherry', 'grapes', 'guava', 'orange']
for x in fruits:
    if x == 'cherry':   # when x = cherry loop will not print it and continue loop to next element tp print
        continue
    print(x)

print()

fruits = ['apple', 'banana', 'cherry', 'grapes', 'guava', 'orange']
for x in fruits:
    if x == 'cherry':  # when x = cherry then print it otherwise continue loop
        print(x)
    continue
