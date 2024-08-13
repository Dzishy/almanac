print ('Welcome to average Calculator App')

name = input ('What is your name? ').title()
grades = []

num = int (input('How many grades would you like to enter: '))
for i in range (num):
    grades.append (int (input('Enter your grade: ')))

grades.sort(reverse=True)
print ('\nGrades highest to lowest:')
for i in grades:
    print (f'\t{i}')
 
average = sum(grades)/len(grades)
average = round (average,2)
   
print (f"{name}'s Grade Summary:")
print (f'\tTotal number of grades: {len(grades)}')
print (f'\tHighest grade: {grades[0]}')
print (f'\tLowest grade: {grades[-1]}')
print (f'\tAverage: {average}')

desire = float (input('What is your desired average: '))
newGrade = desire*(len(grades)+1)-sum(grades)
newGrade = round(newGrade,2)
print (f'You need to get a {newGrade} on your next assignment to earn a {desire} average.')

newGrades = grades [:] #list slicing - ":" means from the first to the last object in a list. But you can also use for example [1:3]
badGrade = int (input ('\nWhat grade would you like to change: '))
change = int (input (f'What grade would you like to change {badGrade} to: '))
newGrades.remove(badGrade)
newGrades.append(change)
print (newGrades)

newGrades.sort(reverse=True)
print ('\nNew grades highest to lowest:')
for i in newGrades:
    print (f'\t{i}')
 
averageNew = sum(newGrades)/len(newGrades)
averageNew = round (averageNew,2)
   
print (f"{name}'s New Grade Summary:")
print (f'\tTotal number of grades: {len(newGrades)}')
print (f'\tHighest grade: {newGrades[0]}')
print (f'\tLowest grade: {newGrades[-1]}')
print (f'\tAverage: {averageNew}')

print (f'\nYour new average would be a {averageNew} compared to your real average of {average}.')
differ = averageNew-average
differ = round(differ,2)
print (f'It is a difference of {differ} points.')