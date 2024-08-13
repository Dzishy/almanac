import collections
print ('Welcome to the Frequency Analysis App')


nonLetters = ['1','2','3','4','5','6','7','8','9','0',' ','.',',','?','!','"',"'", ':',';','(',')','%','&','$','#','@','*','/','[',']']
phrase1 = input ('\nEnter a word or phrase to count the occurrence of each letter: ').lower().strip()

for nonLetter in nonLetters:
    phrase1 = phrase1.replace(nonLetter,'')
    
frequency = collections.Counter(phrase1)
totalOccur = sum(frequency.values())

print ('\nHere is the frequency analysis from phrase 1: ')
print ('\tLetter\tOccurrence\tPercentage')
for key, value in frequency.items():
    percentage = value * 100 / totalOccur
    print (f'\t{key}\t{value}\t\t{percentage:.2f}')

print ('\nLetters ordered from highest occurrence to lowest:')
ordered = (frequency.most_common())
for i in ordered:
    print (i[0],end='')
    
phrase2 = input ('\nEnter a word or phrase to count the occurrence of each letter: ').lower().strip()

for nonLetter in nonLetters:
    phrase2 = phrase2.replace(nonLetter,'')
    
frequency2 = collections.Counter(phrase2)
totalOccur2 = sum(frequency2.values())

print ('\nHere is the frequency analysis from phrase 2: ')
print ('\tLetter\tOccurrence\tPercentage')
for key, value in frequency2.items():
    percentage2 = value * 100 / totalOccur2
    print (f'\t{key}\t{value}\t\t{percentage2:.2f}')

print ('\nLetters ordered from highest occurrence to lowest:')
ordered2 = (frequency2.most_common())
for i in ordered2:
    print (i[0],end='')
