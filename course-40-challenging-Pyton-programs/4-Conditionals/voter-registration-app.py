
print ('Welcome to the Voter Registration App')

name = input ('Please enter your name: ').title().strip()
age = int (input ('Please enter your age: '))
parties = ['Republican', 'Democratic', 'Independent', 'Libertarian', 'Green']
if age < 18:
    print ('You are not old enough to register to vote.')
else:
    print (f'\nCongratulations {name}! You are old enough to register to vote.')
    print ('\nHere is a list of political parties to join:')
    for party in parties:
        print (f'\t- {party.title().strip()}')
    chosenParty = input ('What party would you like to join: ').title().strip()
    if chosenParty in parties:
        print (f'\nCongratulations {name}! You have joined the {chosenParty} party!')
        if chosenParty == 'Republican' or chosenParty == 'Democratic':
            print ('That is a major party.')
        elif chosenParty == 'Independent':
            print ('You are an independent person')
        else:
            print ('That is not a major party.')
    else:
        print ('That is not a given party.')
