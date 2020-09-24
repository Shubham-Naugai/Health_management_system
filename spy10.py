# 2. Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print
# their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".

age = int(input('age of employee: '))
gender = input('gender of employee (M / F): ')
marital_status = input('marital status of employee (Y / N): ')

if gender == 'f' and 20 <= age <= 40:
    print('employee will work in urban areas only')
elif gender == 'm' and 20 <= age <= 40:
    print('employee can work anywhere')
elif gender == 'm' and 40 <= age <= 60:
    print('employee will work in urban areas only')
else:
    print('...ERROR...')
