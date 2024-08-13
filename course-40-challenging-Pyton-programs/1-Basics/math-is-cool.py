

name = input("Hello! What is your name? \n")
number = float(input ("Enter a number you want to work with\n"))
message = "Math is cool!"

print ('\n'f'Multiplication table for {number} is:')
for i in range(1,10):
    mult_result = number * i
    print (f'      {i} * {number} = {mult_result}' )
    
    
print ('\n'f'Exponent table for {number} is:')
for i in range(1,10):    
     exp_result = number **float(i)
     print (f'      {number} ** {i} = {exp_result}' )
     
print ('\n'f'{name.upper()} {message.upper()}\n {name.lower()} {message.lower()}\n  {name.title()} {message.title()}\n')