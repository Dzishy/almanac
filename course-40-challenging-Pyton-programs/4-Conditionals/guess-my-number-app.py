import random

print ('Welcome to the Guess My Number App')

name = input ('\nHello! What is your name: ').title().strip()

print (f'Well {name}, I am thinking of a number between 1 and 20.')
number = random.randint(1,20)

for i in range(1,6):
    guess = int (input('\nTake a guess: '))
    
    if guess == number:
        print (f'\nYou guessed the number in {i} guesses!')  
    elif guess > number:
        print ('Your guess is too high.')
    elif guess < number: 
        print ('Your guess is too low.')         

if i == 5 and guess != number:
    print (f'\nGame over! The number I was thinking of was {number}')  
