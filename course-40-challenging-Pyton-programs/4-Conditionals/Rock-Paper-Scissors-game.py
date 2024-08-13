import random

print ('Welcome to Rock, Paper, Scissors Game')

numRounds = int (input ('How many rounds do you want to play: '))

playerScore = 0
computerScore = 0
choises = ['rock', 'paper', 'scissors']

for round in range (1,numRounds+1):
    print (f'\nRound {round}')
    print (f'Player: {playerScore}\tComputer: {computerScore}')
    
    compChoise = random.choice(choises)
    playerChoice = input ('Time to pick...rock, paper, scissors: ').lower().strip()
    
    print (f'\tComputer: {compChoise}\n\tPlayer: {playerChoice}')
    # players mistake:
    if playerChoice not in choises:
        print ('That is not a valid option.\nComputer gets the point!')
        computerScore +=1
    # player wins:    
    elif compChoise == 'rock' and playerChoice == 'paper':
        playerScore +=1
        print ('\tPaper covers rock!')
        print (f'\tYou win round {round}.')
    elif playerChoice == 'scissors' and compChoise == 'paper':
        playerScore +=1
        print ('\tScissors cut paper!')
        print (f'\tYou win round {round}.')
    elif playerChoice == 'rock' and compChoise == 'scissors':
        playerScore +=1
        print ('\tRock smashes scissors!')
        print (f'\tYou win round {round}.')
    # computer wins:
    elif playerChoice == 'rock' and compChoise == 'paper':
        computerScore +=1
        print ('\tPaper covers rock!')
        print (f'\tComputer wins round {round}.')
    elif compChoise == 'scissors' and playerChoice == 'paper':
        computerScore +=1
        print ('\tScissors cut paper!')
        print (f'\tComputer wins round {round}.')
    elif compChoise == 'rock' and playerChoice == 'scissors':
        computerScore +=1
        print ('\tRock smashes scissors!')
        print (f'\tComputer wins round {round}.')
    # tie:
    else:
        print ('\tIt is a tie!')

if computerScore > playerScore:
    winner = 'Computer :('
elif computerScore < playerScore:
    winner = 'You :)'
else:
    winner = "Tie"
        
print ('\nFinal game results:')
print (f'\tRounds played: {numRounds}\n\tPlayer score: {playerScore}\n\tComputer score: {computerScore}\n\tWinner: {winner}')