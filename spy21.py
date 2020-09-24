# break statement in while loop
i = 0
while i < 10:
    if i == 8:
        break
    print('i = ', i)
    i = i + 1
print()

# continue statement in while loop
i = 0
while i < 10:
    i = i + 1
    if i == 8:
        continue
    print('i = ', i)
