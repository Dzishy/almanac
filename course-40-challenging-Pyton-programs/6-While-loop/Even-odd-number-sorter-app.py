
print ('Welcome to the Even Odd Number Sorter App')
running = True

while running:
    numbers = list (input ('Enter in a string of numbers separated by a comma (,): ').replace(' ','').split(sep=','))
    print (numbers)
    even = []
    odd = []

    for i in numbers:
        if i == ',':
            numbers.remove (i)
    for i in numbers:
        if i == ' ':
            numbers.remove (i)    

    print ('\n----Result Summary----')
    for i in numbers:
        if int (i) % 2 != 0:
            odd.append (i)
            print (f'\t{i} is odd!')
        elif int (i) % 2 == 0:
            even.append (i)
            print (f'\t{i} is even')

    print (f'\nThe following {len(even)} numbers are even:')
    for i in even:
        print(f'\t{i}')

    print (f'\nThe following {len(odd)} numbers are odd:')
    for i in odd:
        print(f'\t{i}')
    
    choice = input ('\nWould you like to run program again (y/n): ').lower()
    if choice != 'y':
        print ('Thank you for using the program. Goodbye.')
        running = False