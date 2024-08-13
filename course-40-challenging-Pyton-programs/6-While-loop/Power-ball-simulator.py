import random
import math

print ('---------------Power-Ball Simulator---------------')
whiteBalls = int(input ('How many white balls to draw from for the 5 winning numbers (Normally 69): '))
redBalls = int(input ('How many red balls to draw from for the 5 winning numbers (Normally 26): '))
if whiteBalls < 5:
    whiteBalls = 5
if redBalls < 1:
    redBalls = 1
    
odds = (math.factorial(whiteBalls)*math.factorial(redBalls))/(math.factorial(5)*math.factorial(whiteBalls-5)*math.factorial(redBalls-1))
print (f'You have a 1 in {odds} chance of winning this lottery.')

interval = int(input('Purchase tickets in what interval: '))

print ('----------Welcome to the Power-Ball----------')

winningNumbers = []
while len (winningNumbers) < 5:
    number = random.randint(1, whiteBalls)
    if number not in winningNumbers:
        winningNumbers.append(number)
winningNumbers.sort()
winningNumbers.append (random.randint(1, redBalls))
    
print ("Tonights winning numbers are: ", end='')
for i in winningNumbers:
    print (i,end=' ')

input ('Press "Enter" to begin purchasing the tickets!')
totalTickets = 0
tickets = []
playing = True
while winningNumbers not in tickets and playing == True:
    
    ticket = []
    while len (ticket) < 5:
        tNumber = random.randint(1, whiteBalls)
        if tNumber not in ticket:
            ticket.append(tNumber)
    ticket.sort()
    ticket.append (random.randint(1, redBalls))
    if ticket not in tickets:
        tickets.append(ticket)
        totalTickets += 1
        print (ticket)
    else:
        print ('Loosing ticket generated. Disregard...')
        
    if totalTickets % interval == 0:
        print (f'{totalTickets} tickets purchased so far with no winners.')
        choice = input ('Do you want to purchase more tickets (y/n): ').lower()
        if choice != 'y':
            playing = False  
           
            #checking numbers in the ticket and comparing with winning numbers:                    
if ticket == winningNumbers:
    ticket = [str(i) for i in ticket]
    print (f'You won the Power-Ball! Winning ticket numbers: {' '.join(ticket)}')
    print (f'Purchased a total of {totalTickets} tickets')
else:
    print (f'\nYou bought {totalTickets} tickets and still lost. Better luck next time!')
        
    
                
          
            
    
    
        
            
        
        
        
       
        