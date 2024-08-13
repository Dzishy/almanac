print ("Welcome to the Grade Sorter App")

# firstGrade = int(input('\nWhat is your first grade (0-100):'))
# secondGrade = int(input('What is your second grade (0-100):'))
# thirdGrade = int(input('What is your third grade (0-100):'))
# fourthGrade = int(input('What is your ffourth grade (0-100):'))

# grades= []
# grades.append (firstGrade)
# grades.append (secondGrade)
# grades.append (thirdGrade)
# grades.append (fourthGrade)

# print ('\nYour grades are:', grades)

# grades.sort(reverse=True)
# print ('\nYour grades from highest to lowest are:', grades)

# print ('\nThe lowest two grades will now be droppped.')
# print ('Removed grade:', grades.pop())
# print ('Removed grade:', grades.pop())
# print ('\nYour remaining grades are: ', grades)
# print ('Nice work! Your highest grade is a ', grades[0])

grades = []
for i in range(4):
    grade = int(input('Enter your grade (0-100) '))
    grades.append(grade)
print ('\nYour grades are:',grades)

grades.sort(reverse=True)
print ('\nYour grades from highest to lowest are:', grades)

print ('\nThe lowest two grades will now be droppped.')
print ('Removed grade:', grades.pop())
print ('Removed grade:', grades.pop())

print ('\nYour remaining grades are: ', grades)
print ('Nice work! Your highest grade is a ', grades[0])