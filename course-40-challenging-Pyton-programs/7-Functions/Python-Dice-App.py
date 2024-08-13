import random

print ('Welcome to the Python Dice App')

def diceRoll (sides, rolls):
    print ('\n----------Results are as followed:----------')
    total = [] 
    for i in range (rolls):
        i = random.randint(1,sides)
        print (i)
        total.append (i)
    return sum(total)

rolling = True
while rolling:
    numSides = int (input ('\nHow many sides would you like on your dice: '))
    numRolls = int (input ('How many dice would you like to roll: '))
    print (f'\nYou rolled {numRolls} a {numSides} sided dice.')
    totalValue = diceRoll(numSides,numRolls)
    print (f'The total value od your roll is {totalValue}.')
    
    choice = input ('\nWould you like to roll again (y/n):').lower()
    if choice != 'y':
        print ('Thank you for using the Python Dice App.')
        rolling = False
        
# alternative function:
#def diceRoll (sides, rolls):
#    print ('\n----------Results are as followed:----------')
#    total = 0 
#    for i in range (rolls):
#        i = random.randint(1,sides+1)
#        print (i)
#        total += i
#    return total