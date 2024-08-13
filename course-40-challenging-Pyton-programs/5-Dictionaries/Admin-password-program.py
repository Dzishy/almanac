
print ('Welcome to Database Admin Program')

loginPassword = {
    'mkelly' : 'kellooo',
    'passibee' : 'pb023',
    'sammin02' : 'samuel0204',
    'admin01' : 'admin',
}

login = input ('Enter your login: ')
password = input ('Enter your password: ')    

if login in loginPassword.keys() and password in loginPassword[login]:
    print (f'\nHello {login}! You are logged in.')
    if login == 'admin01' and password == 'admin':
        print ('\nHere is the current database:')
        for key, value in loginPassword.items():
            print (f'Username: {key}\tPassword: {value}')
    else:
        answer = input ('Would you like to change your password (y/n): ')
        if answer.startswith('y'):
            newPassword = input ('Enter your new password (min 8 characters): ').strip()
            if len(newPassword) >= 8:
                loginPassword[login] = newPassword
                print (f'Your new password is: {loginPassword[login]}')
            else:
                print (f'Your new password is too short. Your password is {loginPassword[login]}')
        else:
            print ('Ok, nothing to change today :)')
elif password not in loginPassword[login]:
    print (f'\nHello {login}! Password incorrect!')
else:
    print ('Sorry, your username is not in database. Goodbye.')        
print (loginPassword['mkelly'])