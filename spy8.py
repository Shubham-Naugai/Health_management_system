# 4. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

classes_held = input('enter the number of classes held: ')
classes_attend = input('enter the number of classes attend: ')

classes_held = int(classes_held)
classes_attend = int(classes_attend)

percentage = (classes_attend/classes_held) * 100
print('Your percentage of attending classes = {}%'.format(percentage))

if percentage >= 75:
    print('you are eligible to sit in the exam', end='')
else:
    print('you are not eligible to sit in the exam', end='')
