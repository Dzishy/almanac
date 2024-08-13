#рекурсия
                                                                                       
import math
print ('Welcome to the Factorial Calculator App')

userInput = int(input ('\nWhat number would you like to compute the factorial of: '))
print (f'{userInput}! = ', end="")   

for i in range (1,userInput):
    print (f'{i}', end="*")
print (userInput, sep="")
 
result1 = math.factorial(userInput)
result2 = 1
for i in range (1, userInput+1):
    result2 *= i

print (f'\nHere is the result from the math library: {result1}')
print (f'Here is the result of my own algoritm: {result2}')
print (f'\nIt is shown twice that {userInput}! = {result1}')