# example 2
# program to display student's marks from record
student_name = 'rahul'

marks = {'ashok': 90, 'rahul': 55, 'yogi': 77}

for student in marks:
    if student_name == student:
        print(marks[student])
        break
else:
    print('No entry with that name found.')
