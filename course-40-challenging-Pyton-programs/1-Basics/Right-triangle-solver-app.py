import math

print ("welcome to the Right Triangle Solver App!")

leg_1 = float(input("what is the length of the first leg?\n"))
leg_2 = float(input("what is the length of the second leg?\n"))

hip = math.sqrt(leg_1**2 + leg_2**2)
area = leg_1*leg_2/2

print(f'For the triangle with legs {leg_1:.3f} and {leg_2:.3f} the hipotenuse is: {hip:.3f}.')
print(f'For the triangle with legs {leg_1:.3f} and {leg_2:.3f} the area is: {area:.3f}.')

# diffrence between :.nf and round()

# hip = round(math.sqrt(leg_1**2 + leg_2**2),3)
# area = round(leg_1*leg_2/2, 3)

# print(f'For the triangle with legs {leg_1} and {leg_2} the hipotenuse is: {hip}.')
# print(f'For the triangle with legs {leg_1} and {leg_2} the area is: {area}.')