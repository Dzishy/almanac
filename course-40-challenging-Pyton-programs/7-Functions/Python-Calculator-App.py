
print ('Welcome to the Python Calculator App')

def add (num1,num2):
    sum = num1 + num2
    return sum

def sub (num1,num2):
    difference = num1 - num2
    return difference

def mult (num1,num2):
    product = num1 * num2
    return product

def division (num1,num2):
    quotient = num1 / num2
    return quotient

def exp (num1,num2):
    power = num1 ** num2
    return power

def calculation ():
    operName = input ('Enter an operation (addition, subtraction, multiplication, division, exponentiation): ').lower()
    
    if operName.startswith ('a'):
        result = round(add (num1,num2),2)
        print (f'The sum of {num1} and {num2} is {result}')
        summary.append(f'{num1} + {num2} = {result}')
    elif operName.startswith ('s'):
        result = round(sub (num1,num2),2)
        print (f'The difference of {num1} and {num2} is {result}')
        summary.append(f'{num1} - {num2} = {result}')
    elif operName.startswith ('m'):
        result = round(mult (num1,num2),2)
        print (f'The product of {num1} and {num2} is {result}')
        summary.append(f'{num1} * {num2} = {result}')
    elif operName.startswith ('d'):
        if num2 == 0:
            result = ''
            print ('You cannot divide by 0')
            summary.append('DIV ERROR')
        else:
            result = round(division (num1,num2),2)
            print (f'The quotient of {num1} and {num2} is {result}')
            summary.append(f'{num1} / {num2} = {result}')
    elif operName.startswith ('e'):
        result = round(exp (num1,num2),2)
        print (f'The result of {num1} raised to the {num2} power is {result}')
        summary.append(f'{num1} ** {num2} = {result}')
    else:
        result = ''
        print ('That is not a valid operation. Try again.')
        summary.append('OP ERROR')
    return result

summary = []

calculating = True
while calculating:
        
    num1 = float(input ('\nEnter a number '))
    num2 = float(input ('Enter a number '))

    calc = calculation()
    
    choice = input ('\nWould you like to run the program again (y/n): ').lower()
    if choice != 'y':
        calculating = False

print ('\nCalculation Summary:')
for i in summary:
    print (i)
print ('\nThank you for using the Python Calculator App. Goodbye.')
