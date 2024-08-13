import random

print ('Welcome to the Guess My Word App')

gameDict = {
    'sports' : ['basketball', 'tennis', 'football', 'hockey', 'swinning', 'skiing'],
    'fruits' : ['strawberry', 'orange', 'banana', 'watermelon', 'apple', 'kiwi'],
    'colors' : ['green', 'grey', 'yellow', 'red', 'purple', 'blue']
}

categories = []
for key in gameDict.keys():
    categories.append(key)
    
playing = True
while playing:
    category = categories[random.randint(0,len(categories)-1)]
    word = gameDict[category][random.randint (0, len(gameDict[category])-1)]
        
    blankWord = []
    for i in word:
        blankWord.append('-')
    
    print (f'Guess a {len(word)} letter word from the following category: {category.title()}')  
    guess = ''
    guessCount = 0
    
    while guess != word:
        print (''.join(blankWord))
        guess = input ('Enter your quess: ').lower()
        guessCount += 1
        if guess == word:
            print (f'That is correct! You won the game in {guessCount} tries.')
            break
        
        else:
            print ('That is not correct. Let us reveal a letter to help you!')
            revealing = True
            while revealing:
                numLetter = random.randint (0, len(word)-1)
                if blankWord[numLetter] == '-':   
                    blankWord[numLetter] = word[numLetter]
                    revealing = False 
                                                      
    choice = input ('Do you want to keep playing (y/n): ').lower()    
    if choice != 'y':
        playing = False
        print ('Thank you for playing!')