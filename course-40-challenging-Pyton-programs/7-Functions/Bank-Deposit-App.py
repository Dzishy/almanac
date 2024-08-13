
print ('Welcome to the Python First National Bank')

def bankAccount ():
    '''Creating a dictionary with account information'''
    accountInfo = {}
    accountInfo ['name'] =  input ('\nEnter your name: ').title().strip()
    accountInfo ['savings'] = round (float (input ('How much money would you like to set up your savings account with: ').strip()),2)
    accountInfo ['checking'] = round (float (input ('How much money would you like to set up your checking account with: ').strip()),2)
    return accountInfo

def currentInfo ():
    print ('\nCurrent Account Information')
    for key, value in accountInfo.items():
        if key == 'name':
            print (f'{key.title()}: {value}')
        else:
            print (f'{key.title()}: ${value}')
        
def deposit (accountInfo, account, depAmount):
    accountInfo [account] += depAmount
    print (f"Deposited ${depAmount} into {accountInfo['name']}'s {account.title()} account.")
    currentInfo()
    
def withdrawal (accountInfo, account, withdrawAmount):
    if withdrawAmount <= accountInfo [account]:
        accountInfo [account] -= withdrawAmount
        print (f"Withdrew ${withdrawAmount} from {accountInfo['name']}'s {account.title()} account.")
        currentInfo()
    else:
        print (f'Sorry, by withdrawing ${withdrawAmount} you will have a negative balance')
        
def transactionType ():
    if transaction == 'deposit':
        deposit (accountInfo, account, money)          
    elif transaction == 'withdrawal':
        withdrawal (accountInfo, account, money)            
    else:
        print ('Sorry, we cannot do that for you today.')

accountInfo = bankAccount()    
banking = True
while banking:
    
    currentInfo()
    account = input ('What account would you like to access (savings or checking): ').lower().strip()
    transaction = input ('What type of transaction would you like to make (deposit or withdrawal): ').lower().strip()
    money = round (float (input ('How much money: ')),2)
    
    if account == 'savings' or account == 'checking':        
        transactionType()                     
    else:
        print (f'There is no {account} account')
        
    choice = input ('Would you like to make another transaction (y/n): ')
    if choice != 'y':
        banking = False
        
        
