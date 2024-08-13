
print ('Welcome to the Factor Generator App')

running = True

while running:
    number = int (input ('\nEnter a number to determine all factors of that number: '))
    factors = []
    
    print (f'\nFactors of {number} are:') 
    for i in range (1,number+1):
        if number % i == 0:
            factors.append(i)
            print (i)
# check if it is correct:
    print ('\nIn summary:')
    while factors:
        print (f'{factors[0]} * {factors[-1]} = {factors[0]*factors[-1]}')
        factors.pop(0)
        if factors:
            factors.pop(-1)
        
    choice = input ('Run again (y/n): ').lower()
    if choice != 'y':
        running = False
    