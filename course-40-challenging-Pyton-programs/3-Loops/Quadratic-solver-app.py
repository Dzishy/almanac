import cmath

print ('Welcome to the Quadratic Solver App.')

print ('A quadratic equation is of the form ax^2 + bx + c = 0')
print ('Your solutions can be real or complex numbers.')
print ('A complex number has two parts: a + bj')
print ('Where a is the real portion and bj is the imaginary portion.')

result = 0


for i in range (int(input ('How many equations would you like to solve today: '))):
    print (f'\nSolving equation #{i+1}\n----------------------------------------------------')
    
    a = float(input('Please enter your value of a (coefficient of x^2): '))
    b = float(input('Please enter your value of b (coefficient of x): '))
    c = float(input('Please enter your value of c (coefficient): '))
       
    x1 = (-b+cmath.sqrt(b**2-4*a*c))/2*a
    x2 = (-b-cmath.sqrt(b**2-4*a*c))/2*a
    
    print (f'The solutions to {a}x^2 + {b}x + {c} are:')
    print (f'\tx1 = {x1}\n\tx2 = {x2}')
    