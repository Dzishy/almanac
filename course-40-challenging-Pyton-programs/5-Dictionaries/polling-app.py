
print ('Welcome to the Yes or No Polling App')

poll = {}
yes = 0
no = 0

issue = input ('\nWhat is the Yes or No issue you will be voting on today: ')
numVoters = int(input ('What is the number of voters you will allow on the issue: '))
password = input ('Enter a password for polling pesults: ')

for i in range (numVoters):
    name = input ('\nEnter your full name: ').title()
    if name not in poll.keys():
        print (f'Here is our issue: {issue}')
        vote = input ('What do you think...yes or no: ').lower()
        poll [name] = vote
        if vote == 'yes':
            yes +=1
            print (f'Thank you {name}! Your vote of {vote} has been recorded.')
        elif vote == 'no':
            no +=1
            print (f'Thank you {name}! Your vote of {vote} has been recorded.')
        else:
            print ('That is not a yes or no answer, but okay...')
            print (f'Thank you {name}! your vote of {vote} has been recorded.')    
    else:
        print ('Sorry, it seems that someone with that name has already voted.')    

numVotes = len(poll.keys())    
print (f'\nThe following {numVotes} people voted: ')            
for key in poll.keys():
    print (key)
print (f'On the following issue: {issue}')

if yes > no:
    print (f'Yes wins. {yes} votes to {no}.')
elif yes < no:
    print (f'No wins. {no} votes to {yes}.')    
else:    
    print (f'It was a tie! {yes} votes to {no}.')
    
adminLogin = input ('\nTo see the voting results enter the admin password: ')
if adminLogin == password:
    for keys, values in poll.items():
        print (f'Voter: {keys}\tVote: {values}')
else:
    print ('Wrong password.')

print ('\nThank you for using the Yes or No Polling App.')
