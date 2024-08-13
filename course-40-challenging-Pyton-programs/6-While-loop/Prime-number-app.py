import time

print ('Welcome to the Prime Number App')

running = True
while running:
    print ('\nEnter 1 to determine if a specific number is prime.')
    print ('\nEnter 2 to determine all prime numbers within a set range.')
    choice = input ('Enter your choice 1 or 2: ').strip()
    if choice == '1':
        number = int (input ('\nEnter a number to determine if it is prime or not: ').strip())
        primeStatus = True
        for i in range (2, number):
            print (i)
            if number % i == 0:
                primeStatus = False
                break
        if primeStatus:
            print (f'{number} is prime!')
        else:
            print (f'{number} is not prime!')
        
        # number = int (input ('\nEnter a number to determine if it is prime or not: ').strip())
        # checkList = []
        # for i in range (1, number+1):
        #     if number % i == 0:
        #         checkList.append (i)      
        # if len (checkList) == 2:
        #     print (f'{number} is prime!')
        # else:
        #     print (f'{number} is not prime!')
       
    elif choice == '2':
        lowerBound = int (input ('Enter the lower bound of your range: '))
        upperBound = int (input ('Enter the upper bound of your range: '))
        
        start = time.time()
        prime = []
        for primeCandidate in range (lowerBound,upperBound+1):
            if primeCandidate > 1:
                primeStatus = True
                for i in range (2, primeCandidate):
                    if primeCandidate % i ==0:
                        primeStatus = False
                        break
            else:
                primeStatus = False
            
            if primeStatus:
                prime.append(primeCandidate)
        end = time.time()
        
        #numbers = []
        #prime = []
        #start = time.time()
        #for i in range (lowerBound, upperBound+1):
        #    numbers.append(i)
        #for number in numbers:
        #    checkList = []
        #    for i in range (1,len(numbers)+1):
        #        if number % i == 0:
        #            checkList.append (i)       
        #    if len (checkList) == 2:
        #        prime.append(number) 
        #end = time.time()
        totalTime = end - start        
        print (f'\nCalculations took a total of {totalTime:7f} seconds.')
        print (f'The following numbers between {lowerBound} and {upperBound} are prime:')
        input ('Press enter to continue.')
        for i in prime:
            print (i)
        
    else:
        print ('\nThat is not a valid option.')
        
    newRun = input ('\nWould you like to run the program again (y/n): ').lower()
    if newRun != 'y':
        running = False
        print ('Thank you for using a program.')