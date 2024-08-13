import random

print ('Welcome to the Coin Toss App')

print ('\nI will flip a coin a set number of times.')
num = int (input ('How many times do you want me to flip the coin: '))
answer = input ('Do you want to see the result of each flip (y/n): ').lower()
heads = 0
tails = 0

for flips in range (num):
    result = random.randint(0,1)
    if result == 0:
        heads +=1
        if answer == 'y':
            print ('HEADS')
    else:
        tails +=1
        if answer == 'y':
            print ('TAILS')
        
    if heads == tails:
        print (f'At {flips+1} flips, the number of heads and tails were equal at {heads} each.')
    
        
percHeads = heads*100/num
percTails = tails*100/num
print ((f'\nResults of flipping a coin {num} times:').title())
print ('\nSide\t\tCount\t\tPercentage')
print (f'Heads\t\t{heads}/{num}\t\t{percHeads}%')  
print (f'Tails\t\t{tails}/{num}\t\t{percTails}%')    