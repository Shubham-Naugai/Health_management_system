# looping techniques in python
# 1. enumerate()
for key, value in enumerate(['the', 'big', 'bang', 'theory']):
    print(key, value)

print()
# 2. zip()
questions= ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']
for question, answer in zip(questions, answers):
    print('what is your {}? i am {}'. format(question, answer))

print()
# 3. items()
d = {"geeks": "for", "only": "geeks"}
print("The key value pair using items is : ")   # using items to print the dictionary key-value pair
for i, j in d.items():
    print(i, j)

print()
# 4. sorted() (without set())
lis = [1, 1, 4, 3, 3, 6, 2]
print("the list in sorted order is: ")
for i in sorted(lis):
    print(i, end=' ')

print()
# 5. sorted() (with set())
lis = [1, 1, 4, 3, 3, 6, 2]
print("the list in sorted order(without duplicates) is: ")
for i in sorted(set(lis)):
    print(i, end=' ')

print()
# 6. reversed()
lis = [1, 2, 3, 4, 5, 6]
print("the list in reversed order is: ")
for i in reversed(lis):
    print(i, end=' ')
