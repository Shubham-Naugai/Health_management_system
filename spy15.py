# the range function in for loop
# The range() function returns a sequence of numbers,
# starting from 0 by default, and increments by 1 (by default)

for x in range(12):
    print(x)     # 12 is not included

# We can use the range() function in for loops to iterate through a sequence of numbers.
# It can be combined with the len() function to iterate through a sequence using indexing.
# Here is an example.
# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz']     # iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])
