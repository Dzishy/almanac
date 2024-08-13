from matplotlib import pyplot

def loanInfo ():
    loan = {}
    loan ['Principal'] = float (input ('Enter the loan amount: '))
    loan ['Rate'] = float (input ('Enter the interest rate: ')) * 0.01
    loan ['Monthly Payment'] = float (input ('Enter the desired monthly payment amount: '))
    loan ['Money Paid'] = 0
    return loan

def showLoan (loan, month):
    print (f'\n---Loan Information after {month} months---')
    for key, value in loan.items():
        print (f'{key}: {value}')
        
def addInterest (loan):
    loan ['Principal'] = loan ['Principal'] + loan ['Principal'] * loan ['Rate'] / 12
    
def makePayment (loan):
    loan ['Principal'] = loan ['Principal'] - loan ['Monthly Payment']
    if loan ['Principal'] > 0:
        loan ['Money Paid'] += loan ['Monthly Payment']
    else:
        loan ['Money Paid'] += loan ['Monthly Payment'] + loan ['Principal']
        loan ['Principal'] = 0

def summary (loan, month, principal):
    print (f'\nCongratulations! You paid off your loan in {month} months!')
    print (f'Your loan was ${principal} at a rate of {100*loan ['Rate']}%.')
    print (f'Your monthly payment was ${loan ['Monthly Payment']}.')
    print (f'You spent {round(loan ['Money Paid'], 2)} in total.')
    interest = round (loan['Money Paid'] - principal, 2)
    print (f'You spent ${interest} on interest.')
    
def graph (data, loan):
    x = []
    y = []
    for point in data:
        x.append (point[0])
        y.append (point[1])
    
    pyplot.plot(x, y)
    pyplot.title (f'{100*loan['Rate']}% Interest With $ {loan['Monthly Payment']} Monthly Payment.')
    pyplot.xlabel ('Month Number')
    pyplot.ylabel ('Loan Principal')
    pyplot.show()

month = 0

loan = loanInfo ()
loanAmount = loan ['Principal']
graphData = []
showLoan (loan, month)
start = input ('\nPress "Enter" to  start paying the loan: ')

while loan ['Principal'] > 0:
    month += 1
    addInterest (loan)
    makePayment (loan)
    graphData.append ((month, loan['Principal']))
    showLoan(loan, month)
    if loan ['Principal'] > loanAmount:
        print ('You will NEVER pay off your loan!!!\nYou cannot get ahead of the interest! :-)')
        break
    
    elif loan ['Principal'] <= 0:
        summary (loan, month, loanAmount)
        graph (graphData, loan)
        break

