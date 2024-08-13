import random

thesaurus = { "hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
            "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
            "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
            "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
}

print ('Welcome to the Thesaurus App')
print ("\nChoose a word and I'll give you a synonim")
print ('\nHere are the words in the thesaurus:')
for keys in thesaurus.keys():
    print (f'\t-{keys}')

userInput = input ('What word would you like a synonim for: ').lower().strip()

if userInput in thesaurus.keys():
    l = len(thesaurus[userInput])
    num = random.randint(0,l-1)
    print (f'The synonim for {userInput} is {thesaurus[userInput][num]}')
else:
    print (f'Sorry, the word {userInput} is not currently in the thesaurus.')
    
again = input ('\nWould you like to see the whole thesaurus (yes/no): ').lower()
if again.startswith('y'):
    for keys, values in thesaurus.items():
        print(f'\n{keys.title()} synonims are:')
        for value in values:
            print (f'\t- {value}')
else:
    print ('\nI hope you enjoyed the program. Thank you!')