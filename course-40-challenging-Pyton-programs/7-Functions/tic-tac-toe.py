
def board (charList):
    print ('\n\t   Tic-Tac-Toe')
    print (f'\t~~~~~~~~~~~~~~~~~')
    print (f'\t|| {charList[0]} || {charList[1]} || {charList[2]} ||')
    print (f'\t~~~~~~~~~~~~~~~~~')
    print (f'\t|| {charList[3]} || {charList[4]} || {charList[5]} ||')
    print (f'\t~~~~~~~~~~~~~~~~~')
    print (f'\t|| {charList[6]} || {charList[7]} || {charList[8]} ||')
    print (f'\t~~~~~~~~~~~~~~~~~')
    
def playerMove (player, charList):
    while True:
        character = int(input (f'{player}: Where would you like to place your piece (1-9): ').strip())
        if character > 0 and character < 10:
            if charList[character-1] != '_':
                print ('That spot has already been chosen. Try again.')
            else:
                return character
        else:
            print ('That is not a spot on the board. Try again')        

def replaceChars (playerMove, player, charList):
    charList[playerMove-1] = player

def winner (charList, player):
    return ((charList[0] == player and charList[1] == player and charList[2] == player) or
            (charList[3] == player and charList[4] == player and charList[5] == player) or
            (charList[6] == player and charList[7] == player and charList[8] == player) or
            (charList[0] == player and charList[3] == player and charList[6] == player) or
            (charList[1] == player and charList[4] == player and charList[5] == player) or
            (charList[2] == player and charList[5] == player and charList[8] == player) or
            (charList[0] == player and charList[4] == player and charList[8] == player) or
            (charList[2] == player and charList[4] == player and charList[6] == player))

player1 = 'X'
player2 = 'O'
characters = [1,2,3,4,5,6,7,8,9]
emptychars = ['_']*9    

board (characters)
board (emptychars)

while True:
    move = playerMove (player1, emptychars)
    replaceChars (move, player1,emptychars)
    board (characters)
    board (emptychars)
    
    if winner (emptychars, player1):
        print (f'Player {player1} wins the game.')
        break
    elif '_' not in emptychars:
        print ('It is a tie')
        break
    
    move = playerMove (player2, emptychars)
    replaceChars (move, player2,emptychars)
    board (characters)
    board (emptychars)
    
    if winner (emptychars, player2):
        print (f'Player {player1} wins the game.')
        break
    elif '_' not in emptychars:
        print ('It is a tie')
        break