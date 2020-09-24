# nesting of loop
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":

fruits = ["apple", "banana", "cherry"]
adj = ["red", "big", "tasty"]
for y in fruits:
    for x in adj:
        print(x, y)


# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content
# put in the pass statement to avoid getting an error.

number = [1, 2, 3]
for x in number:
    pass
