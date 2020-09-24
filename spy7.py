# 3. Take input of age of 3 people by user and determine oldest and youngest among them

print('enter the age of first person: ', end='')
age1 = input()
print('enter the age of second person: ', end='')
age2 = input()
print('enter the age of third person: ', end='')
age3 = input()

age1 = int(age1)
age2 = int(age2)
age3 = int(age3)

if age1 > age2 and age1 > age3:
    print('first person is elder')
elif age2 > age1 and age2 > age3:
    print('second person is elder')
elif age3 > age1 and age3 > age1:
    print('third person is elder')
else:
    print('they have equal ages')
